from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Document, DocumentCollection
from .serializers import (
    DocumentSerializer, 
    DocumentUploadSerializer, 
    DocumentCollectionSerializer, 
    DocumentChunkSerializer
)
from rest_framework import generics

# Create your views here.
class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]  # Changed for testing
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'file_type', 'collection']
    search_fields = ['title']
    ordering = ['-created_at']
    
    def get_queryset(self):
        # Changed for testing - return all documents
        return Document.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'upload']:  # Fixed: check both actions
            return DocumentUploadSerializer
        return DocumentSerializer
    
    def perform_create(self, serializer):
        # Create test user if needed
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = User.objects.first()
        if not user:
            user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
        
        document = serializer.save(user=user)
        # Commented out - task doesn't exist yet
        # from .tasks import process_document
        # process_document.delay(str(document.id))
        
    @action(detail=True, methods=['get'])
    def chunks(self, request, pk=None):  # Fixed: pk=None (capital N)
        """Get all chunks for a document"""
        document = self.get_object()
        chunks = document.chunks.all()
        serializer = DocumentChunkSerializer(chunks, many=True)
        return Response(serializer.data)

    
class DocumentCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentCollectionSerializer
    permission_classes = [AllowAny]  # Changed for testing
    
    def get_queryset(self):  # Fixed typo: get_quesryset -> get_queryset
        # Changed for testing - return all collections
        return DocumentCollection.objects.all()
    
    def perform_create(self, serializer):
        # Create test user if needed
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = User.objects.first()
        if not user:
            user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
        serializer.save(user=user)

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DocumentUploadSerializer
        return DocumentSerializer