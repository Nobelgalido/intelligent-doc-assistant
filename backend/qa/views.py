from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import time

from .models import Conversation, Question
from .serializers import ConversationSerializer, AskQuestionSerializer
from .services.rag_service import RAGService

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    @action(detail=False, methods=['post'])
    def ask(self, request):
        """Ask a question with RAG"""
        serializer = AskQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question_text = serializer.validated_data['question']
        document_ids = serializer.validated_data.get('document_ids')
        conversation_id = serializer.validated_data.get('conversation_id')
        
        start_time = time.time()
        
        try:
            # Get or create conversation
            if conversation_id:
                conversation = Conversation.objects.get(
                    id=conversation_id,
                    user=request.user
                )
            else:
                conversation = Conversation.objects.create(
                    user=request.user,
                    title=question_text[:100]  # Use first 100 chars as title
                    )

            # RAG: Search similar chunks
            rag_service = RAGService()
            similar_chunks = rag_service.search_similar_chunks(
                query=question_text,
                user_id=str(request.user.id),
                document_ids=document_ids,
                top_k=5
            )
            
            if not similar_chunks:
                return Response({
                    'error': 'No documents found. Please upload documents first.'
                }, status=status.HTTP_400_BAD_REQUEST)
                
            # RAG: Generate answer
            result = rag_service.generate_answer(
                question=question_text,
                context_chunks=similar_chunks,
            )
            
            processing_time = int((time.time() - start_time) * 1000)  # in ms
            
            # Save question and answer
            question = Question.objects.create(
                conversation=conversation,
                question_text=question_text,
                answer_text=result['answer'],
                source_documents=result['sources'],
                processing_time_ms=processing_time,
            )
            
            # Update user stats
            request.user.total_questions += 1
            request.user.save()
            
            return Response({
                'question_id': question.id,
                'conversation_id': conversation.id,
                'question': question_text,
                'answer': result['answer'],
                'sources': result['sources'],
                'processing_time_ms': processing_time,
            })
            
        
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


