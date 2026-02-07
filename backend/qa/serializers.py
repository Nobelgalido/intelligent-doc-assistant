from rest_framework import serializers
from .models import Conversation, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id', 'question_text', 'answer_text', 'source_documents',
            'processing_time_ms', 'created_at', 'is_helpful'
        )
        read_only_fields = ('id', 'created_at')
        
class AskQuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=1000)
    document_ids = serializers.ListField(
        child=serializers.UUIDField(),
        required=False,
        allow_empty=True,
    )
    conversation_id = serializers.UUIDField(required=False, allow_null=True)

class ConversationSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'questions_count', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    def get_questions_count(self, obj):
        return obj.questions.count()