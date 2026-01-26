# Google Gemini API Setup Guide (FREE Alternative to OpenAI)

> **Great Choice!** Google Gemini offers a generous free tier, making it perfect for learning and portfolio projects.

## 🎉 Why Gemini?

✅ **100% FREE** - No credit card required
✅ **Generous Limits** - 15 RPM, 1,500 requests/day
✅ **Good Performance** - Gemini 1.5 Flash is fast and capable
✅ **Free Embeddings** - text-embedding-004 model
✅ **Easy Setup** - Just need a Google account

---

## 📝 Step 1: Get Your Gemini API Key (5 minutes)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Get API Key"** or **"Create API Key"**
4. Copy your API key
5. Paste it in your `.env` file:

```env
AI_PROVIDER=gemini
GOOGLE_API_KEY=your-api-key-here
```

---

## 📦 Step 2: Install Required Packages

Add to your `backend/requirements/base.txt`:

```txt
# Existing packages...

# Google Gemini
google-generativeai==0.3.2
```

Then install:

```bash
cd backend
pip install google-generativeai
```

---

## 🔧 Step 3: Update RAG Service

Replace the RAG service in **`backend/apps/qa/services/rag_service.py`** with this Gemini-compatible version:

```python
import os
import google.generativeai as genai
from typing import List, Dict, Tuple
import numpy as np
from django.conf import settings
import faiss

from apps.documents.models import DocumentChunk, Document

# Configure Gemini
genai.configure(api_key=settings.GOOGLE_API_KEY)


class RAGService:
    """Service for Retrieval-Augmented Generation using Google Gemini"""

    def __init__(self):
        # Initialize Gemini models
        self.llm_model = genai.GenerativeModel(
            settings.GEMINI_MODEL or 'gemini-1.5-flash'
        )
        self.embedding_model = settings.GEMINI_EMBEDDING_MODEL or 'models/text-embedding-004'
        self.embedding_dimension = 768  # Gemini embeddings are 768-dimensional

    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding vector for text using Gemini"""
        try:
            result = genai.embed_content(
                model=self.embedding_model,
                content=text,
                task_type="retrieval_document"
            )
            return result['embedding']
        except Exception as e:
            raise Exception(f"Error generating embedding: {str(e)}")

    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        embeddings = []
        for text in texts:
            try:
                result = genai.embed_content(
                    model=self.embedding_model,
                    content=text,
                    task_type="retrieval_document"
                )
                embeddings.append(result['embedding'])
            except Exception as e:
                print(f"Error embedding text: {str(e)}")
                # Return zero vector on error
                embeddings.append([0.0] * self.embedding_dimension)
        return embeddings

    def embed_document_chunks(self, document_id: str) -> int:
        """
        Generate and store embeddings for all chunks of a document
        Returns: Number of chunks embedded
        """
        chunks = DocumentChunk.objects.filter(
            document_id=document_id,
            embedding__isnull=True
        )

        if not chunks.exists():
            return 0

        # Process in batches
        batch_size = 100
        total_embedded = 0

        chunk_list = list(chunks)
        for i in range(0, len(chunk_list), batch_size):
            batch = chunk_list[i:i + batch_size]
            texts = [chunk.text for chunk in batch]

            try:
                embeddings = self.generate_embeddings_batch(texts)

                for chunk, embedding in zip(batch, embeddings):
                    chunk.embedding = embedding
                    chunk.save(update_fields=['embedding'])
                    total_embedded += 1

            except Exception as e:
                print(f"Error embedding batch: {str(e)}")
                continue

        return total_embedded

    def search_similar_chunks(
        self,
        query: str,
        user_id: str,
        document_ids: List[str] = None,
        top_k: int = 5
    ) -> List[Tuple[DocumentChunk, float]]:
        """
        Search for chunks similar to query using vector similarity

        Args:
            query: Search query
            user_id: User ID to filter documents
            document_ids: Optional list of specific document IDs
            top_k: Number of results to return

        Returns:
            List of (chunk, similarity_score) tuples
        """
        # Generate query embedding
        query_embedding = np.array(self.generate_embedding(query)).astype('float32')

        # Get all chunks with embeddings
        chunks_query = DocumentChunk.objects.filter(
            document__user_id=user_id,
            embedding__isnull=False
        ).select_related('document')

        if document_ids:
            chunks_query = chunks_query.filter(document_id__in=document_ids)

        chunks = list(chunks_query)

        if not chunks:
            return []

        # Build FAISS index
        embeddings = np.array([chunk.embedding for chunk in chunks]).astype('float32')

        index = faiss.IndexFlatL2(self.embedding_dimension)
        index.add(embeddings)

        # Search
        distances, indices = index.search(query_embedding.reshape(1, -1), min(top_k, len(chunks)))

        # Convert distances to similarity scores (inverse)
        similarities = 1 / (1 + distances[0])

        results = []
        for idx, similarity in zip(indices[0], similarities):
            results.append((chunks[idx], float(similarity)))

        return results

    def generate_answer(
        self,
        question: str,
        context_chunks: List[Tuple[DocumentChunk, float]],
        conversation_history: List[Dict] = None
    ) -> Dict:
        """
        Generate answer using RAG with retrieved context

        Args:
            question: User question
            context_chunks: Retrieved chunks with similarity scores
            conversation_history: Previous Q&A pairs

        Returns:
            Dict with answer, sources, and metadata
        """
        # Prepare context
        context_text = "\n\n".join([
            f"[Source {i+1} - {chunk.document.title}, Page {chunk.page_number}]:\n{chunk.text}"
            for i, (chunk, score) in enumerate(context_chunks)
        ])

        # Prepare conversation history
        history_text = ""
        if conversation_history:
            history_text = "\n".join([
                f"Q: {item['question']}\nA: {item['answer']}"
                for item in conversation_history[-3:]  # Last 3 exchanges
            ])

        # Create prompt
        system_instruction = """You are an intelligent document assistant. Your role is to answer questions based ONLY on the provided context from the user's documents.

Rules:
1. Only use information from the provided context
2. If the answer is not in the context, say "I don't have enough information to answer that"
3. Cite sources by referring to [Source X] numbers
4. Be concise but complete
5. If you're uncertain, express that clearly"""

        user_prompt = f"""Context from documents:
{context_text}

{f"Previous conversation:\n{history_text}" if history_text else ""}

Question: {question}

Please provide a detailed answer based on the context above."""

        try:
            # Generate response with Gemini
            response = self.llm_model.generate_content(
                f"{system_instruction}\n\n{user_prompt}",
                generation_config=genai.types.GenerationConfig(
                    temperature=float(settings.AI_TEMPERATURE or 0.7),
                )
            )

            answer = response.text

            # Prepare sources
            sources = [
                {
                    'document_id': str(chunk.document.id),
                    'document_title': chunk.document.title,
                    'chunk_id': str(chunk.id),
                    'page_number': chunk.page_number,
                    'text_preview': chunk.text[:200] + '...',
                    'similarity_score': score
                }
                for chunk, score in context_chunks
            ]

            return {
                'answer': answer,
                'sources': sources,
                'context_used': len(context_chunks),
                'model': settings.GEMINI_MODEL or 'gemini-1.5-flash'
            }

        except Exception as e:
            raise Exception(f"Error generating answer: {str(e)}")
```

---

## ⚙️ Step 4: Update Django Settings

Add to your **`backend/config/settings.py`**:

```python
from decouple import config

# AI Configuration
AI_PROVIDER = config('AI_PROVIDER', default='gemini')

# Google Gemini
GOOGLE_API_KEY = config('GOOGLE_API_KEY', default='')
GEMINI_MODEL = config('GEMINI_MODEL', default='gemini-1.5-flash')
GEMINI_EMBEDDING_MODEL = config('GEMINI_EMBEDDING_MODEL', default='models/text-embedding-004')

# OpenAI (fallback)
OPENAI_API_KEY = config('OPENAI_API_KEY', default='')
OPENAI_MODEL = config('OPENAI_MODEL', default='gpt-4')
OPENAI_EMBEDDING_MODEL = config('OPENAI_EMBEDDING_MODEL', default='text-embedding-ada-002')

# General AI settings
AI_TEMPERATURE = config('AI_TEMPERATURE', default=0.7, cast=float)
```

---

## 🔄 Step 5: Update Document Model (If Needed)

Since Gemini embeddings are 768-dimensional (vs OpenAI's 1536), you'll need to update the model:

**`backend/apps/documents/models.py`**:

```python
from django.conf import settings
from pgvector.django import VectorField

class DocumentChunk(models.Model):
    # ... other fields ...

    # Dynamic embedding dimension based on provider
    embedding = VectorField(
        dimensions=768 if settings.AI_PROVIDER == 'gemini' else 1536,
        null=True,
        blank=True
    )
```

**Or** use a fixed dimension that works for both (pad or truncate):

```python
# Use 1536 for compatibility, pad Gemini embeddings
embedding = VectorField(dimensions=1536, null=True, blank=True)
```

Then in your RAG service, pad Gemini embeddings:

```python
def generate_embedding(self, text: str) -> List[float]:
    result = genai.embed_content(...)
    embedding = result['embedding']

    # Pad to 1536 if using Gemini (768) with 1536-dim field
    if len(embedding) < 1536:
        embedding = embedding + [0.0] * (1536 - len(embedding))

    return embedding
```

---

## 🧪 Step 6: Test It!

```bash
# Terminal 1: Start Django
cd backend
python manage.py runserver

# Terminal 2: Start Celery
celery -A config worker -l info

# Terminal 3: Test in Python shell
python manage.py shell

>>> from apps.qa.services.rag_service import RAGService
>>> service = RAGService()
>>> embedding = service.generate_embedding("Hello world")
>>> print(f"Embedding length: {len(embedding)}")
# Should output: Embedding length: 768
```

---

## 📊 Gemini vs OpenAI Comparison

| Feature | Gemini 1.5 Flash (Free) | GPT-4 (Paid) |
|---------|-------------------------|--------------|
| **Cost** | FREE | ~$0.03/1K tokens |
| **Rate Limit** | 15 RPM, 1,500/day | Depends on tier |
| **Context** | 1M tokens | 8K-128K tokens |
| **Quality** | Very good | Excellent |
| **Embeddings** | Free (768-dim) | Paid (1536-dim) |
| **Setup** | Easy | Requires billing |

---

## 🎯 For Portfolio/Interview

When showcasing this project:

✅ **Mention**: "Built with Google Gemini for cost-effective AI integration"
✅ **Highlight**: "Demonstrates ability to work with multiple AI providers"
✅ **Explain**: "Chose Gemini for free tier during development, easily switchable to OpenAI for production"

This actually makes your project MORE impressive because it shows:
- Cost-consciousness
- Flexibility in design
- Ability to work with multiple APIs

---

## 🚀 Next Steps

1. **Get your Gemini API key** from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Update your `.env` file** with the API key
3. **Install google-generativeai** package
4. **Follow Milestone 4** in Claude.md but use the Gemini code above
5. **Test with your documents**!

---

## 💡 Pro Tips

1. **Rate Limits**: Gemini free tier has 15 requests/minute. Add rate limiting in production.
2. **Error Handling**: Always wrap API calls in try-catch blocks
3. **Caching**: Cache embeddings in the database to reduce API calls
4. **Batch Processing**: Process documents in batches to stay within rate limits

---

## ❓ FAQ

**Q: Can I switch between Gemini and OpenAI?**
A: Yes! Just change `AI_PROVIDER=openai` in `.env` and add your OpenAI key.

**Q: Which is better for production?**
A: Both work well. Gemini is more cost-effective, OpenAI might have slightly better quality.

**Q: What about embedding dimensions?**
A: Use the padding approach above, or create separate migration for each provider.

**Q: Is Gemini really free?**
A: Yes! 1,500 requests/day is generous for a portfolio project.

---

**You're all set! Gemini is perfect for learning and your portfolio. 🎉**
