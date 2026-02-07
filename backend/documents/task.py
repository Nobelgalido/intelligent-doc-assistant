from celery import shared_task
from django.utils import timezone
from .models import Document, DocumentChunk
from .utils import DocumentProcessor

@shared_task
def process_document(document_id: str):
    """Process uploaded document: extract text and create chunks."""
    try:
        document = Document.objects.get(id=document_id)
        document.status = 'processing'
        document.save()
        
        file_path = document.file.path
        processor = DocumentProcessor()
        
        # Extract text based on file type
        if document.file_type == 'pdf':
            extracted_text, page_count = processor.extract_text_from_pdf(file_path)
        elif document.file_type == 'docx':
            extracted_text, page_count = processor.extract_text_from_docx(file_path)
        elif document.file_type in ['txt', 'md']:
            extracted_text, page_count = processor.extract_text_from_txt(file_path)
        else:
            raise ValueError(f"Unsupported file type: {document.file_type}")
        
        # Update document with extracted content
        document.extracted_text = extracted_text
        document.page_count = page_count
        document.word_count = processor.count_words(extracted_text)
        
        # Create chunks
        chunks = processor.chunk_text(extracted_text)
        
        for idx, chunk_text in enumerate(chunks):
            DocumentChunk.objects.create(
                document=document,
                text=chunk_text,
                chunk_index=idx,
                page_number=(idx * page_count) // len(chunks) + 1 if page_count > 0 else 1,
            )
            
        document.status = 'completed'
        document.processed_at = timezone.now()
        document.save()
        
        # Update user stats
        user = document.user
        user.total_documents += 1
        user.save()
        
        # Trigger embedding generation
        generate_embeddings.delay(str(document_id))
        
        return f"Document {document_id} processed successfully."
    
    except Document.DoesNotExist:
        return f"Document with ID {document_id} does not exist."
    except Exception as e:
        document.status = 'failed'
        document.processing_error = str(e)
        document.save()
        return f"Error processing document {document_id}: {str(e)}"

@shared_task
def generate_embeddings(document_id: str):
    """Generate embeddings for a document chunks"""
    from qa.services.rag_service import RAGService
    
    try:
        rag_service = RAGService()
        count = rag_service.embed_document_chunks(document_id)
        return  f"Generate {count} embeddings for document {document_id}"
    except Exception as e:
        return f"Error generating embeddings: {str(e)}"