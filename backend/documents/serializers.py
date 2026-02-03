from rest_framework import serializers
from .models import Document, DocumentCollection, DocumentChunk

class DocumentChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentChunk
        fields = ('id', 'text', 'chunk_index', 'page_number', 'created_at')
        

class DocumentSerializer(serializers.ModelSerializer):
    chunks_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Document
        fields = ('id', 'title', 'file_type', 'file_size', 'status', 'processing_error', 'page_count', 'word_count', 'chunks_count', 'created_at', 'processed_at')
        read_only_fields = ('id', 'file_size', 'status', 'created_at')
    
    def get_chunks_count(self, obj):
        return obj.chunks.count()
    

class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'file', 'file_type', 'collection')
    
    def validate_file(self, value):
        if value.size > 50 * 1024 * 1024:  # 50 MB limit
            raise serializers.ValidationError("File size exceeds the 50MB limit.")
        return value
    
    def create(self, validated_data):
        validated_data['file_size'] = validated_data['file'].size
        
        # Get or create a test user (since authentication is disabled)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = User.objects.first()
        if not user:
            user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
        validated_data['user'] = user
        
        return super().create(validated_data)
    

class DocumentCollectionSerializer(serializers.ModelSerializer):
    documents_count = serializers.SerializerMethodField()
    
    class Meta:
        model = DocumentCollection
        fields = ('id', 'name', 'description', 'documents_count', 'created_at')
    
    def get_documents_count(self, obj):
        return obj.documents.count()