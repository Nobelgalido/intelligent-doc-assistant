import google.generativeai as genai
from typing import List, Dict, Tuple
import numpy as np
from django.conf import settings
import faiss
from documents.models import DocumentChunk



class RAGService:
    """RAG service using Google Gemini"""
    
    def __init__(self):
        # Configure Gemini
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        
        self.llm_model = genai.GenerativeModel(settings.GEMINI_MODEL_NAME)
        self.embedding_model = settings.GEMINI_EMBEDDING_MODEL
        self.embedding_dimension = 3072  # gemini-embedding-001 uses 3072 dimensions
        
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for a given text."""
        try:
            result = genai.embed_content(
                model=self.embedding_model,
                content=text, 
                task_type = "retrieval_document",
                )
            return result['embedding']
        except Exception as e:
            raise Exception(f"Error generating embedding: {str(e)}")
        
    def embed_document_chunks(self, document_id: str) -> int:
        """Generate Embeddings for all chunks of a document"""
        chunks = DocumentChunk.objects.filter(
            document_id=document_id,
            embedding__isnull=True,
        )
        
        if not chunks.exists():
            return 0
        
        total_embedded = 0
        
        for chunk in chunks:
            try:
                embedding = self.generate_embedding(chunk.text)
                chunk.embedding = embedding
                chunk.save(update_fields=['embedding'])
                total_embedded += 1
            except Exception as e:
                print(f"Error embedding chunk {chunk.id}: {str(e)}")
                continue
        return total_embedded
    
    def search_similar_chunks(self, query: str, user_id: str, document_ids: List[str] = None, top_k: int = 5) -> List[Tuple[DocumentChunk, float]]:
        """Search for similar chunks using vector similarity."""
        query_embedding = np.array(self.generate_embedding(query)).astype('float32')
        
        chunks_query = DocumentChunk.objects.filter(
           document__user_id=user_id,
           embedding__isnull=False,
         ).select_related('document')
        
        if document_ids:
            chunks_query = chunks_query.filter(document_id__in=document_ids)
            
        chunks = list(chunks_query)
        
        if not chunks:
            return []
        
        embeddings =  np.array([chunk.embedding for chunk in chunks]).astype('float32')
        index = faiss.IndexFlatL2(self.embedding_dimension)
        index.add(embeddings)
        distances, indices = index.search(query_embedding.reshape(1, -1), min(top_k, len(chunks)))
        similarities = 1 / (1 + distances[0])  # Convert L2 distance to similarity score
        results = []
        for idx, sim in zip(indices[0], similarities):
            results.append((chunks[idx], float(sim)))
            
        return results
    
    def generate_answer(self, question: str, context_chunks: List[Tuple[DocumentChunk, float]], conversation_history: List[Dict] = None) -> Dict:
        """Generate answer using RAG"""
        context_text = "\n\n".join([f"[Source {i+1} - {chunk.document.title}, Page {chunk.page_number}]:\n{chunk.text}"
                                    for i, (chunk, score) in enumerate(context_chunks)])
        
        system_instruction = """You are an intelligent document assistant. Answer questions based ONLY on the provided context.
        Rules:
        1. Only use information from the context
        2. If answer not in context, say "I don't have enough information"
        3. Cite sources by referring to [Source X]
        4. Be concise and clear"""
        
        user_prompt = f"""Context:{context_text}
        Question: {question}
        Answer based on the context above"""
        
        try:
            response = self.llm_model.generate_content(
                f"{system_instruction}\n\n{user_prompt}",
                generation_config=genai.types.GenerationConfig(
                    temperature=float(settings.AI_TEMPERATURE),
                )
            )

            sources = [
                {
                    'document_id': str(chunk.document.id),
                    'document_title': chunk.document.title,
                    'chunk_id': str(chunk.id),
                    'page_number': chunk.page_number,
                    'text_preview': chunk.text[:200] + '...',
                    'similarity_score': score,
                }
                for chunk, score in context_chunks
            ]
            
            return {
                'answer': response.text,
                'sources': sources,
                'context_used': len(context_chunks),
                'model': settings.GEMINI_MODEL_NAME,
            }
            
        except Exception as e:
            raise Exception(f"Error generating answer: {str(e)}")