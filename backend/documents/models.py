from django.db import models
import uuid
from django.conf import settings
from pgvector.django import VectorField

# Create your models here.
class DocumentCollection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'document_collections'
        ordering = ['-created_at']
        

    def __str__(self):
        return self.name
    
class Document(models.Model):
    
    FILE_TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('docx', 'Word Document'),
        ('txt', 'Text File'),
        ('md', 'Markdown'),
    ]
    
    Status_CHOICES = [
        ('pending', 'Pending Processing'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')
    collection = models.ForeignKey(DocumentCollection, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    
    # File info
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    file_size = models.BigIntegerField(help_text='File size in bytes')
    
    # Processing status
    status = models.CharField(max_length=20, choices=Status_CHOICES, default='pending')
    processing_error = models.TextField(blank=True, null=True)
    
    # Content
    extracted_text = models.TextField(blank=True)
    page_count = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'documents'
        ordering = ['-created_at']
        indexes = [models.Index(fields=['user', '-created_at']),
                   models.Index(fields=['status']),
                   ]
    
    def __str__(self):
        return self.title
    
class DocumentChunk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chunks')
    
    # Chunk content
    text = models.TextField()
    chunk_index = models.IntegerField(help_text='Index of the chunk within the document')
    page_number = models.IntegerField(null=True, blank=True, help_text='Page number from which the chunk was extracted, if applicable')
    
    # Vector embedding (768 dimensions for Gemini)
    embedding = VectorField(dimensions=768, null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'document_chunks'
        ordering = ['document', 'chunk_index']
        indexes = [models.Index(fields=['document', 'chunk_index'])]
    
    def __str__(self):
        return f'Chunk {self.chunk_index} of Document {self.document.id}'