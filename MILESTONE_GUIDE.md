# 🎯 Complete Milestone Guide - Step by Step

> Your comprehensive guide to building the Intelligent Document Q&A Platform

**Progress Tracking:** Check off each step as you complete it!

---

## Table of Contents
- [Milestone 1: Project Setup & Django Foundation](#milestone-1)
- [Milestone 2: Database Models & Authentication](#milestone-2)
- [Milestone 3: Document Upload & Processing](#milestone-3)
- [Milestone 4: RAG Implementation](#milestone-4)
- [Milestone 5: React Frontend Foundation](#milestone-5)
- [Milestone 6: Frontend-Backend Integration](#milestone-6)
- [Milestone 7: Docker Containerization](#milestone-7)
- [Milestone 8: CI/CD Pipeline](#milestone-8)
- [Milestone 9: Testing & Quality Assurance](#milestone-9)
- [Milestone 10: Production Deployment](#milestone-10)

---

<a name="milestone-1"></a>
# 🎯 MILESTONE 1: Project Setup & Django Foundation

**Time Estimate:** 2-3 hours
**Goal:** Set up Django backend and make your first GitHub commit

## Step 1: Create Backend Structure

```bash
# Navigate to project root
cd /c/Users/monst/PROJECTS/intelligent-doc-assistant

# Create backend directory
mkdir backend
cd backend
```

## Step 2: Create Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (Git Bash)
source venv/Scripts/activate

# Verify activation - you should see (venv) in prompt
which python
```

## Step 3: Create Requirements File

Create `backend/requirements.txt`:

```txt
Django==5.0.0
djangorestframework==3.14.0
django-cors-headers==4.3.0
psycopg2-binary==2.9.9
python-decouple==3.8
django-environ==0.11.2
pillow==10.1.0
```

## Step 4: Install Dependencies

```bash
# Make sure venv is activated!
pip install -r requirements.txt

# Verify installation
pip list
```

## Step 5: Create Django Project

```bash
# Create project (the . means current directory)
django-admin startproject config .

# Verify structure:
# backend/
#   ├── venv/
#   ├── config/
#   ├── manage.py
#   └── requirements.txt
```

## Step 6: Create Django Apps

```bash
# Create all apps
python manage.py startapp users
python manage.py startapp documents
python manage.py startapp qa
python manage.py startapp core

# Verify they were created
ls -la
```

## Step 7: Create Backend .env File

Create `backend/.env`:

```env
# Django Settings
DEBUG=True
SECRET_KEY=django-insecure-change-this-key-12345!@#$%
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (Docker)
DATABASE_NAME=intelligent_doc_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/0

# AI Provider
AI_PROVIDER=gemini
GOOGLE_API_KEY=your-actual-gemini-key-here

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

**🔑 Important:** Add your real Gemini API key!

## Step 8: Configure Django Settings

Edit `backend/config/settings.py`:

### Add imports at top:
```python
from pathlib import Path
from decouple import config
import os
```

### Update these sections:

**SECRET_KEY and DEBUG:**
```python
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
```

**INSTALLED_APPS (replace the entire list):**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',

    # Local apps
    'users',
    'documents',
    'qa',
    'core',
]
```

**MIDDLEWARE (add corsheaders near top):**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

**DATABASES (replace entire section):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default='5432'),
    }
}
```

**Add at bottom of file:**
```python
# CORS Settings
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='').split(',')
CORS_ALLOW_CREDENTIALS = True

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## Step 9: Test Database Connection

```bash
# Make sure Docker containers are running
cd ..
docker ps

# Should see intelligent-doc-db and intelligent-doc-redis

# Go back to backend
cd backend

# Run migrations
python manage.py migrate

# Should see: "Applying migrations... OK"
```

## Step 10: Create Superuser

```bash
python manage.py createsuperuser

# Enter:
# Email: your@email.com
# Username: admin (or your choice)
# Password: (choose a strong password)
```

## Step 11: Test Server

```bash
# Start server
python manage.py runserver

# Open browser: http://localhost:8000
# You should see Django welcome page!

# Press Ctrl+C to stop server
```

## Step 12: Initialize Git & Push

```bash
# Go to project root
cd ..

# Initialize git (if not done)
git init

# Add all files
git add .

# Check what will be committed
git status

# Make first commit
git commit -m "Milestone 1: Django project setup

- Created Django 5.0 project with DRF
- Configured PostgreSQL connection
- Set up apps: users, documents, qa, core
- Configured CORS for React frontend
- Environment variables with python-decouple
- Initial migrations successful

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Create GitHub repo (do this on github.com first!)
# Then add remote:
git remote add origin https://github.com/YOUR-USERNAME/intelligent-doc-assistant.git
git branch -M main
git push -u origin main
```

## ✅ Milestone 1 Checklist

- [ ] Virtual environment created and activated
- [ ] Django and dependencies installed
- [ ] Django project created
- [ ] Four apps created (users, documents, qa, core)
- [ ] .env file created with credentials
- [ ] settings.py configured
- [ ] Database migrations successful
- [ ] Superuser created
- [ ] Server runs without errors
- [ ] Git repository initialized
- [ ] First commit made
- [ ] Pushed to GitHub

## 🎉 Success Criteria

You've completed Milestone 1 when:
✅ Django server runs on http://localhost:8000
✅ No errors in terminal
✅ Database connection works
✅ Code is on GitHub

**Take a break! Then move to Milestone 2.** ☕

---

<a name="milestone-2"></a>
# 🎯 MILESTONE 2: Database Models & Authentication

**Time Estimate:** 3-4 hours
**Goal:** Create database models and implement JWT authentication

## Prerequisites
- ✅ Milestone 1 complete
- ✅ Virtual environment activated
- ✅ Docker containers running

## Step 1: Update Requirements

Add to `backend/requirements.txt`:

```txt
djangorestframework-simplejwt==5.3.0
django-filter==23.5
pgvector==0.2.3
```

Install new packages:
```bash
cd backend
source venv/Scripts/activate
pip install djangorestframework-simplejwt django-filter pgvector
```

## Step 2: Enable pgvector Extension

```bash
# Connect to PostgreSQL
docker exec -it intelligent-doc-db psql -U postgres -d intelligent_doc_db

# Inside psql:
CREATE EXTENSION IF NOT EXISTS vector;

# Verify
\dx

# You should see 'vector' in the list
# Exit
\q
```

## Step 3: Create Custom User Model

Create `backend/users/models.py`:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom User model with additional fields"""

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    # Professional info
    github_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    # Usage stats
    total_documents = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
```

## Step 4: Create Document Models

Create `backend/documents/models.py`:

```python
import uuid
from django.db import models
from django.conf import settings
from pgvector.django import VectorField


class DocumentCollection(models.Model):
    """Group of related documents"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='collections'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'document_collections'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.user.email}"


class Document(models.Model):
    """Uploaded document"""

    FILE_TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('docx', 'Word Document'),
        ('txt', 'Text File'),
        ('md', 'Markdown'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending Processing'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    collection = models.ForeignKey(
        DocumentCollection,
        on_delete=models.CASCADE,
        related_name='documents',
        null=True,
        blank=True
    )

    # File info
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    file_size = models.BigIntegerField(help_text='File size in bytes')

    # Processing status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
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
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title


class DocumentChunk(models.Model):
    """Text chunks with vector embeddings for RAG"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='chunks'
    )

    # Chunk content
    text = models.TextField()
    chunk_index = models.IntegerField()
    page_number = models.IntegerField(null=True, blank=True)

    # Vector embedding (768 dimensions for Gemini)
    embedding = VectorField(dimensions=768, null=True, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'document_chunks'
        ordering = ['document', 'chunk_index']
        indexes = [
            models.Index(fields=['document', 'chunk_index']),
        ]

    def __str__(self):
        return f"Chunk {self.chunk_index} of {self.document.title}"
```

## Step 5: Create Q&A Models

Create `backend/qa/models.py`:

```python
import uuid
from django.db import models
from django.conf import settings


class Conversation(models.Model):
    """Q&A conversation thread"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations'
    )
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'conversations'
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.title} - {self.user.email}"


class Question(models.Model):
    """User question with RAG-generated answer"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    # Question
    question_text = models.TextField()

    # Answer
    answer_text = models.TextField(blank=True)

    # RAG metadata
    sources = models.JSONField(default=list, help_text='Source document chunks')
    confidence_score = models.FloatField(null=True, blank=True)

    # Timing
    processing_time_ms = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Feedback
    is_helpful = models.BooleanField(null=True, blank=True)
    feedback_text = models.TextField(blank=True)

    class Meta:
        db_table = 'questions'
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['conversation', 'created_at']),
            models.Index(fields=['user', '-created_at']),
        ]

    def __str__(self):
        return f"Q: {self.question_text[:50]}..."
```

## Step 6: Update Django Settings

Edit `backend/config/settings.py`:

Add to bottom:
```python
# Custom User Model
AUTH_USER_MODEL = 'users.User'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

# JWT Settings
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

## Step 7: Register Models in Admin

Edit `backend/users/admin.py`:
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'created_at']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'created_at']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering = ['-created_at']

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'avatar', 'bio', 'github_profile', 'linkedin_profile', 'portfolio_url')}),
        ('Statistics', {'fields': ('total_documents', 'total_questions', 'is_verified')}),
    )
```

Edit `backend/documents/admin.py`:
```python
from django.contrib import admin
from .models import DocumentCollection, Document, DocumentChunk


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
    readonly_fields = ['file_size', 'page_count', 'word_count', 'processed_at']


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ['document', 'chunk_index', 'page_number']
    list_filter = ['document']
    search_fields = ['text']
```

Edit `backend/qa/admin.py`:
```python
from django.contrib import admin
from .models import Conversation, Question


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['title', 'user__email']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'user', 'conversation', 'created_at', 'is_helpful']
    list_filter = ['created_at', 'is_helpful']
    search_fields = ['question_text', 'answer_text']
```

## Step 8: Create and Run Migrations

```bash
# Make migrations
python manage.py makemigrations

# Check migration plan
python manage.py showmigrations

# Run migrations
python manage.py migrate

# You should see all tables created successfully
```

## Step 9: Create New Superuser

```bash
# Your old superuser won't work with new User model
python manage.py createsuperuser

# Enter email (not username!)
# Choose password
```

## Step 10: Test Admin Panel

```bash
# Start server
python manage.py runserver

# Open: http://localhost:8000/admin
# Login with new superuser credentials
# You should see: Users, Documents, Document Collections, Conversations, Questions

# Stop server: Ctrl+C
```

## Step 11: Commit Changes

```bash
cd ..
git add .
git commit -m "Milestone 2: Database models and authentication

- Custom User model with extended fields
- Document models with pgvector support
- Q&A conversation models
- Admin panel configuration
- JWT authentication setup
- PostgreSQL migrations successful

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin main
```

## ✅ Milestone 2 Checklist

- [ ] pgvector extension enabled
- [ ] Custom User model created
- [ ] Document models created
- [ ] Q&A models created
- [ ] settings.py updated with AUTH_USER_MODEL
- [ ] REST Framework configured
- [ ] JWT settings added
- [ ] Admin panels registered
- [ ] Migrations created and applied
- [ ] New superuser created
- [ ] Admin panel works
- [ ] Changes committed and pushed

## 🎉 Success Criteria

✅ Admin panel shows all models
✅ Can create users in admin
✅ Database has all tables
✅ No migration errors

**Great job! Ready for Milestone 3!** 🚀

---

<a name="milestone-3"></a>
# 🎯 MILESTONE 3: Document Upload & Processing

**Time Estimate:** 4-5 hours
**Goal:** Implement document upload, text extraction, chunking, and Celery processing

## Prerequisites
- ✅ Milestone 2 complete
- ✅ Models created and migrated
- ✅ Docker containers running

## Step 1: Update Requirements

Add to `backend/requirements.txt`:

```txt
celery==5.3.4
redis==5.0.1
PyPDF2==3.0.1
python-docx==1.1.0
python-magic-bin==0.4.14
```

Install:
```bash
cd backend
source venv/Scripts/activate
pip install celery redis PyPDF2 python-docx python-magic-bin
```

## Step 2: Configure Celery

Create `backend/config/celery.py`:

```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('intelligent_doc_assistant')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

Update `backend/config/__init__.py`:

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

## Step 3: Add Celery Settings

Add to `backend/config/settings.py`:

```python
# Celery Configuration
CELERY_BROKER_URL = config('REDIS_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = config('REDIS_URL', default='redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# File Upload Settings
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB
ALLOWED_DOCUMENT_TYPES = ['pdf', 'docx', 'txt', 'md']
```

## Step 4: Create Document Processing Utilities

Create `backend/documents/utils.py`:

```python
import PyPDF2
from docx import Document as DocxDocument
from typing import Tuple, List
import re


class DocumentProcessor:
    """Utility for document text extraction and processing"""

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> Tuple[str, int]:
        """Extract text from PDF"""
        text = ""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                page_count = len(pdf_reader.pages)

                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n\n"

            return text.strip(), page_count
        except Exception as e:
            raise Exception(f"Error extracting PDF: {str(e)}")

    @staticmethod
    def extract_text_from_docx(file_path: str) -> Tuple[str, int]:
        """Extract text from DOCX"""
        try:
            doc = DocxDocument(file_path)
            text = "\n\n".join([para.text for para in doc.paragraphs if para.text])
            page_count = len(doc.paragraphs) // 20
            return text, max(1, page_count)
        except Exception as e:
            raise Exception(f"Error extracting DOCX: {str(e)}")

    @staticmethod
    def extract_text_from_txt(file_path: str) -> Tuple[str, int]:
        """Extract text from TXT"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return text, 1
        except Exception as e:
            raise Exception(f"Error reading TXT: {str(e)}")

    @staticmethod
    def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """Split text into overlapping chunks"""
        text = re.sub(r'\s+', ' ', text).strip()

        if len(text) <= chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size

            if end < len(text):
                last_period = text.rfind('.', start, end)
                if last_period > start:
                    end = last_period + 1

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            start = end - overlap

        return chunks

    @staticmethod
    def count_words(text: str) -> int:
        """Count words in text"""
        return len(text.split())
```

## Step 5: Create Celery Tasks

Create `backend/documents/tasks.py`:

```python
from celery import shared_task
from django.utils import timezone
from .models import Document, DocumentChunk
from .utils import DocumentProcessor


@shared_task
def process_document(document_id: str):
    """Process uploaded document: extract text and create chunks"""
    try:
        document = Document.objects.get(id=document_id)
        document.status = 'processing'
        document.save()

        file_path = document.file.path
        processor = DocumentProcessor()

        # Extract text based on file type
        if document.file_type == 'pdf':
            text, page_count = processor.extract_text_from_pdf(file_path)
        elif document.file_type == 'docx':
            text, page_count = processor.extract_text_from_docx(file_path)
        elif document.file_type in ['txt', 'md']:
            text, page_count = processor.extract_text_from_txt(file_path)
        else:
            raise ValueError(f"Unsupported file type: {document.file_type}")

        # Update document
        document.extracted_text = text
        document.page_count = page_count
        document.word_count = processor.count_words(text)

        # Create chunks
        chunks = processor.chunk_text(text)

        for idx, chunk_text in enumerate(chunks):
            DocumentChunk.objects.create(
                document=document,
                text=chunk_text,
                chunk_index=idx,
                page_number=(idx * page_count) // len(chunks) + 1 if page_count > 0 else 1
            )

        document.status = 'completed'
        document.processed_at = timezone.now()
        document.save()

        # Update user stats
        user = document.user
        user.total_documents += 1
        user.save()

        return f"Document {document_id} processed successfully"

    except Document.DoesNotExist:
        return f"Document {document_id} not found"
    except Exception as e:
        document.status = 'failed'
        document.processing_error = str(e)
        document.save()
        return f"Error: {str(e)}"
```

## Step 6: Create Serializers

Create `backend/documents/serializers.py`:

```python
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
        fields = (
            'id', 'title', 'file', 'file_type', 'file_size',
            'status', 'processing_error', 'page_count', 'word_count',
            'chunks_count', 'created_at', 'processed_at'
        )
        read_only_fields = ('id', 'file_size', 'status', 'created_at')

    def get_chunks_count(self, obj):
        return obj.chunks.count()


class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'file', 'file_type', 'collection')

    def validate_file(self, value):
        if value.size > 50 * 1024 * 1024:
            raise serializers.ValidationError("File must be under 50MB")
        return value

    def create(self, validated_data):
        validated_data['file_size'] = validated_data['file'].size
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class DocumentCollectionSerializer(serializers.ModelSerializer):
    documents_count = serializers.SerializerMethodField()

    class Meta:
        model = DocumentCollection
        fields = ('id', 'name', 'description', 'documents_count', 'created_at')

    def get_documents_count(self, obj):
        return obj.documents.count()
```

## Step 7: Create Views

Create `backend/documents/views.py`:

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Document, DocumentCollection
from .serializers import (
    DocumentSerializer, DocumentUploadSerializer,
    DocumentCollectionSerializer, DocumentChunkSerializer
)
from .tasks import process_document


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'file_type', 'collection']
    search_fields = ['title']
    ordering = ['-created_at']

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return DocumentUploadSerializer
        return DocumentSerializer

    def perform_create(self, serializer):
        document = serializer.save()
        # Trigger background processing
        process_document.delay(str(document.id))

    @action(detail=True, methods=['get'])
    def chunks(self, request, pk=None):
        """Get all chunks for a document"""
        document = self.get_object()
        chunks = document.chunks.all()
        serializer = DocumentChunkSerializer(chunks, many=True)
        return Response(serializer.data)


class DocumentCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentCollectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DocumentCollection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

## Step 8: Create URLs

Create `backend/documents/urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, DocumentCollectionViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'collections', DocumentCollectionViewSet, basename='collection')

urlpatterns = [
    path('', include(router.urls)),
]
```

Update `backend/config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/documents/', include('documents.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Step 9: Test Document Upload

```bash
# Terminal 1: Start Django
python manage.py runserver

# Terminal 2: Start Celery
celery -A config worker -l info

# Terminal 3: Test API
# Use Postman or curl to upload a document
```

## Step 10: Commit Changes

```bash
cd ..
git add .
git commit -m "Milestone 3: Document upload and processing

- Celery task queue with Redis
- Document text extraction (PDF, DOCX, TXT)
- Text chunking for RAG
- Document upload API endpoints
- Collection management
- Background processing with Celery

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin main
```

## ✅ Milestone 3 Checklist

- [ ] Celery configured
- [ ] Document processor utilities created
- [ ] Celery tasks for processing
- [ ] Serializers created
- [ ] ViewSets implemented
- [ ] URLs configured
- [ ] Can upload documents via API
- [ ] Celery worker processes documents
- [ ] Text extraction works
- [ ] Chunks created correctly
- [ ] Committed and pushed

---

<a name="milestone-4"></a>
# 🎯 MILESTONE 4: RAG Implementation (Google Gemini)

**Time Estimate:** 5-6 hours
**Goal:** Implement RAG with Google Gemini AI for Q&A

## Prerequisites
- ✅ Milestone 3 complete
- ✅ Google Gemini API key in .env

## Step 1: Update Requirements

Add to `backend/requirements.txt`:

```txt
google-generativeai==0.3.2
faiss-cpu==1.7.4
numpy==1.26.2
```

Install:
```bash
pip install google-generativeai faiss-cpu numpy
```

## Step 2: Create RAG Service

Create `backend/qa/services/rag_service.py`:

```python
import google.generativeai as genai
from typing import List, Dict, Tuple
import numpy as np
from django.conf import settings
import faiss

from documents.models import DocumentChunk

# Configure Gemini
genai.configure(api_key=settings.GOOGLE_API_KEY)


class RAGService:
    """RAG service using Google Gemini"""

    def __init__(self):
        self.llm_model = genai.GenerativeModel(
            settings.GEMINI_MODEL or 'gemini-1.5-flash'
        )
        self.embedding_model = settings.GEMINI_EMBEDDING_MODEL or 'models/text-embedding-004'
        self.embedding_dimension = 768

    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for text"""
        try:
            result = genai.embed_content(
                model=self.embedding_model,
                content=text,
                task_type="retrieval_document"
            )
            return result['embedding']
        except Exception as e:
            raise Exception(f"Error generating embedding: {str(e)}")

    def embed_document_chunks(self, document_id: str) -> int:
        """Generate embeddings for all chunks of a document"""
        chunks = DocumentChunk.objects.filter(
            document_id=document_id,
            embedding__isnull=True
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
                print(f"Error embedding chunk: {str(e)}")
                continue

        return total_embedded

    def search_similar_chunks(
        self,
        query: str,
        user_id: str,
        document_ids: List[str] = None,
        top_k: int = 5
    ) -> List[Tuple[DocumentChunk, float]]:
        """Search for similar chunks using vector similarity"""
        query_embedding = np.array(self.generate_embedding(query)).astype('float32')

        chunks_query = DocumentChunk.objects.filter(
            document__user_id=user_id,
            embedding__isnull=False
        ).select_related('document')

        if document_ids:
            chunks_query = chunks_query.filter(document_id__in=document_ids)

        chunks = list(chunks_query)

        if not chunks:
            return []

        embeddings = np.array([chunk.embedding for chunk in chunks]).astype('float32')

        index = faiss.IndexFlatL2(self.embedding_dimension)
        index.add(embeddings)

        distances, indices = index.search(query_embedding.reshape(1, -1), min(top_k, len(chunks)))

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
        """Generate answer using RAG"""
        context_text = "\n\n".join([
            f"[Source {i+1} - {chunk.document.title}, Page {chunk.page_number}]:\n{chunk.text}"
            for i, (chunk, score) in enumerate(context_chunks)
        ])

        system_instruction = """You are an intelligent document assistant. Answer questions based ONLY on the provided context.

Rules:
1. Only use information from the context
2. If answer not in context, say "I don't have enough information"
3. Cite sources by referring to [Source X]
4. Be concise but complete"""

        user_prompt = f"""Context:
{context_text}

Question: {question}

Answer based on the context above."""

        try:
            response = self.llm_model.generate_content(
                f"{system_instruction}\n\n{user_prompt}",
                generation_config=genai.types.GenerationConfig(
                    temperature=float(settings.AI_TEMPERATURE or 0.7),
                )
            )

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
                'answer': response.text,
                'sources': sources,
                'context_used': len(context_chunks),
                'model': settings.GEMINI_MODEL or 'gemini-1.5-flash'
            }

        except Exception as e:
            raise Exception(f"Error generating answer: {str(e)}")
```

## Step 3: Update Document Task

Update `backend/documents/tasks.py` - add at end:

```python
from qa.services.rag_service import RAGService

@shared_task
def generate_embeddings(document_id: str):
    """Generate embeddings for document chunks"""
    rag_service = RAGService()
    count = rag_service.embed_document_chunks(document_id)
    return f"Generated {count} embeddings"
```

Update the `process_document` task to call embeddings:

```python
# At the end of process_document, before return:
generate_embeddings.delay(str(document.id))
```

## Step 4: Add Settings

Add to `backend/config/settings.py`:

```python
# AI Configuration
GOOGLE_API_KEY = config('GOOGLE_API_KEY')
GEMINI_MODEL = config('GEMINI_MODEL', default='gemini-1.5-flash')
GEMINI_EMBEDDING_MODEL = config('GEMINI_EMBEDDING_MODEL', default='models/text-embedding-004')
AI_TEMPERATURE = config('AI_TEMPERATURE', default=0.7, cast=float)
```

## Step 5: Create Q&A Serializers

Create `backend/qa/serializers.py`:

```python
from rest_framework import serializers
from .models import Conversation, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id', 'question_text', 'answer_text', 'sources',
            'confidence_score', 'processing_time_ms', 'created_at'
        )


class AskQuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=1000)
    document_ids = serializers.ListField(
        child=serializers.UUIDField(),
        required=False
    )
    conversation_id = serializers.UUIDField(required=False, allow_null=True)


class ConversationSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('id', 'title', 'questions_count', 'created_at')

    def get_questions_count(self, obj):
        return obj.questions.count()
```

## Step 6: Create Q&A Views

Create `backend/qa/views.py`:

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
            if conversation_id:
                conversation = Conversation.objects.get(
                    id=conversation_id,
                    user=request.user
                )
            else:
                conversation = Conversation.objects.create(
                    user=request.user,
                    title=question_text[:100]
                )

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

            result = rag_service.generate_answer(
                question=question_text,
                context_chunks=similar_chunks
            )

            processing_time = int((time.time() - start_time) * 1000)

            avg_confidence = sum(s['similarity_score'] for s in result['sources']) / len(result['sources'])

            question = Question.objects.create(
                conversation=conversation,
                user=request.user,
                question_text=question_text,
                answer_text=result['answer'],
                sources=result['sources'],
                confidence_score=avg_confidence,
                processing_time_ms=processing_time
            )

            request.user.total_questions += 1
            request.user.save()

            return Response({
                'question_id': question.id,
                'conversation_id': conversation.id,
                'question': question_text,
                'answer': result['answer'],
                'sources': result['sources'],
                'confidence_score': avg_confidence,
                'processing_time_ms': processing_time
            })

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## Step 7: Create Q&A URLs

Create `backend/qa/urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

urlpatterns = [
    path('', include(router.urls)),
]
```

Update `backend/config/urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/documents/', include('documents.urls')),
    path('api/v1/qa/', include('qa.urls')),  # Add this
]
```

## Step 8: Test RAG

```bash
# Upload a document first, then:
# POST to /api/v1/qa/conversations/ask/
# Body: {"question": "What is this document about?"}
```

## Step 9: Commit

```bash
git add .
git commit -m "Milestone 4: RAG implementation with Google Gemini

- Gemini API integration (FREE!)
- Vector embeddings generation
- FAISS similarity search
- Q&A conversation endpoints
- Context retrieval and answer generation
- Source citation

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin main
```

## ✅ Milestone 4 Checklist

- [ ] Gemini API configured
- [ ] RAG service implemented
- [ ] Embeddings generation working
- [ ] Vector search functional
- [ ] Q&A endpoint works
- [ ] Answers include sources
- [ ] Committed and pushed

**Congratulations! The core backend is complete! Next: Frontend** 🎉

---

<a name="milestone-5"></a>
# 🎯 MILESTONE 5-10: Summary Guides

**Note:** Milestones 5-10 cover Frontend, Docker, CI/CD, Testing, and Deployment. These are well-documented in the main Claude.md file with complete code examples.

## Quick Reference

### Milestone 5: React Frontend (Week 3)
- Initialize React with Vite + TypeScript
- Set up Redux Toolkit
- Material-UI configuration
- Auth pages (Login/Register)
- **Estimated time:** 6-8 hours

### Milestone 6: Frontend Integration (Week 3)
- Document upload UI
- Chat interface
- API integration with Axios
- State management
- **Estimated time:** 8-10 hours

### Milestone 7: Docker (Week 4)
- Dockerfiles for backend/frontend
- docker-compose.yml
- Container orchestration
- **Estimated time:** 4-6 hours

### Milestone 8: CI/CD (Week 4)
- GitHub Actions workflow
- Automated testing
- Linting and formatting
- **Estimated time:** 4-6 hours

### Milestone 9: Testing (Week 5)
- Backend tests with pytest
- Frontend tests with Jest
- Integration tests
- **Estimated time:** 6-8 hours

### Milestone 10: Production (Week 5-6)
- Production configuration
- Deployment to cloud
- Monitoring setup
- **Estimated time:** 6-10 hours

**For detailed instructions on Milestones 5-10, refer to [Claude.md](./Claude.md)** starting at each respective milestone section.

---

## 🎓 Learning Tips

### For Each Milestone:
1. **Read the entire milestone** before starting
2. **Understand why** each step is needed
3. **Test frequently** - after every major change
4. **Commit often** - small, meaningful commits
5. **Take breaks** - this is a marathon!

### If You Get Stuck:
1. Re-read the step carefully
2. Check error messages (they tell you what's wrong!)
3. Review the code you just wrote
4. Search the error on Stack Overflow
5. Ask for help

### Time Management:
- **Don't rush** - understanding is more important than speed
- **One milestone per week** is a good pace
- **Review previous milestones** to reinforce learning
- **Celebrate progress** - each milestone is an achievement!

---

## 📊 Progress Tracker

Track your overall progress:

- [ ] ✅ **Milestone 1:** Django Setup (2-3 hours)
- [ ] ✅ **Milestone 2:** Models & Auth (3-4 hours)
- [ ] ✅ **Milestone 3:** Document Processing (4-5 hours)
- [ ] ✅ **Milestone 4:** RAG Implementation (5-6 hours)
- [ ] ⬜ **Milestone 5:** React Frontend (6-8 hours)
- [ ] ⬜ **Milestone 6:** Frontend Integration (8-10 hours)
- [ ] ⬜ **Milestone 7:** Docker (4-6 hours)
- [ ] ⬜ **Milestone 8:** CI/CD (4-6 hours)
- [ ] ⬜ **Milestone 9:** Testing (6-8 hours)
- [ ] ⬜ **Milestone 10:** Production (6-10 hours)

**Total Time:** 48-66 hours (6-10 weeks part-time)

---

## 🎉 Final Checklist

When you complete all milestones, verify:

### Backend ✅
- [ ] Django REST API running
- [ ] PostgreSQL + pgvector working
- [ ] Document upload and processing
- [ ] RAG Q&A functional
- [ ] Gemini API integrated
- [ ] Celery tasks processing
- [ ] Admin panel working

### Frontend ✅
- [ ] React app running
- [ ] Login/Register working
- [ ] Document upload UI
- [ ] Chat interface functional
- [ ] Real-time updates
- [ ] Responsive design

### DevOps ✅
- [ ] Docker containers working
- [ ] CI/CD pipeline passing
- [ ] Tests passing (>80% coverage)
- [ ] Deployed to production
- [ ] Monitoring configured

### Documentation ✅
- [ ] README.md complete
- [ ] Code documented
- [ ] API documentation
- [ ] GitHub repository polished

---

## 🚀 You're Ready!

You now have:
- ✅ Complete milestone roadmap
- ✅ Step-by-step instructions for Milestones 1-4
- ✅ Reference to detailed guides for Milestones 5-10
- ✅ Progress tracking system
- ✅ Learning tips and best practices

**Start with Milestone 1 and work your way through!**

Remember: **You're building a production-grade AI application!** This is impressive work that will showcase your skills to Full Scale and other companies.

**Good luck, and enjoy the journey!** 💪🎉

---

*Last updated: January 2026*
*For Full Scale Python Developer Position*
