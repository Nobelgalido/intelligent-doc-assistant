from django.contrib import admin
from .models import Document, DocumentCollection, DocumentChunk

# Register your admin here.
@admin.register(DocumentCollection)
class DocumentCollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description', 'user__email']
    
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'file_type', 'status', 'created_at']
    list_filter = ['file_type', 'status', 'created_at']
    search_fields = ['title', 'user__email']
    readonly_fields = ['file_size', 'page_count', 'word_count', 'processed_at']  # Fixed: processing_at -> processed_at
    
    def save_model(self, request, obj, form, change):
        """Override to automatically calculate file_size from uploaded file."""
        if obj.file:
            obj.file_size = obj.file.size
        super().save_model(request, obj, form, change)
    
@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ['document', 'chunk_index', 'page_number']
    list_filter = ['document']
    search_fields = ['text']