from django.db import models
import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class Conversation(models.Model):
    """Q&A conversation thread."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversations')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'conversations'
        ordering = ['-updated_at']
        

    def __str__(self):
        return f"{self.title} ({self.user.email})"
    
class Question(models.Model):
    """User question with RAG-generated answer."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='questions')
    
    # Question
    question_text = models.TextField()
    
    # Answer
    answer_text = models.TextField(blank=True)
    
    # RAG metadata
    source_documents = models.JSONField(blank=True, null=True, help_text='List of source documents used for the answer')

    # Timing
    processing_time_ms = models.IntegerField(null=True, blank=True, help_text='Time taken to generate the answer in milliseconds')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Feedback
    is_helpful = models.BooleanField(null=True, blank=True, help_text='User feedback on whether the answer was helpful')
    
    class Meta:
        db_table = 'questions'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['conversation', 'created_at']),
        ]
        
    def __str__(self):
        return f"Q: {self.question_text[:50]}..."