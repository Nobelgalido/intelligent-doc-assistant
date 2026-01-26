# Intelligent Document Q&A Platform - Production Grade Tutorial

**Your Senior Software Engineer Mentor: Claude**

Welcome! I'll guide you through building a production-grade RAG-powered application that showcases all the skills from the Full Scale job posting. We'll build this step-by-step, and you'll push to GitHub after each milestone.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Prerequisites](#prerequisites)
4. [Architecture](#architecture)
5. [Development Roadmap](#development-roadmap)
6. [Milestones](#milestones)
7. [Best Practices](#best-practices)
8. [Common Pitfalls](#common-pitfalls)

---

## Project Overview

### What We're Building
An intelligent document Q&A system where users can:
- Upload documents (PDF, DOCX, TXT)
- Ask questions about their documents
- Get AI-powered answers using RAG (Retrieval-Augmented Generation)
- Manage document collections
- View chat history and analytics

### Why This Project?
This demonstrates:
- ✅ Full-stack development (Django + React)
- ✅ RESTful API design
- ✅ Database management (PostgreSQL with pgvector)
- ✅ AI/ML integration (LLMs + RAG)
- ✅ Modern DevOps practices
- ✅ Production-ready code quality

---

## Technology Stack

### Backend
- **Framework:** Django 5.0 + Django REST Framework
- **Language:** Python 3.11+
- **Database:** PostgreSQL 15 + pgvector extension
- **AI/ML:**
  - LangChain (RAG orchestration)
  - OpenAI GPT-4 (LLM)
  - FAISS or ChromaDB (vector store)
  - Sentence Transformers (embeddings)
- **Task Queue:** Celery + Redis
- **Storage:** AWS S3 / MinIO (for documents)

### Frontend
- **Framework:** React 18 + TypeScript
- **State Management:** Redux Toolkit
- **UI Library:** Material-UI (MUI) v5
- **HTTP Client:** Axios
- **Build Tool:** Vite
- **Testing:** Jest + React Testing Library

### DevOps
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Code Quality:**
  - Black (Python formatter)
  - Flake8, pylint (Python linters)
  - ESLint, Prettier (JS/TS)
  - Pre-commit hooks
- **Testing:**
  - pytest (backend)
  - Jest (frontend)
  - coverage.py
- **Documentation:** Swagger/OpenAPI

---

## Prerequisites

### Required Knowledge
- Python fundamentals
- JavaScript/TypeScript basics
- Git & GitHub
- Basic terminal/command line
- REST API concepts

### Tools to Install
```bash
# Python 3.11+
python --version

# Node.js 18+ and npm
node --version
npm --version

# PostgreSQL 15+
psql --version

# Docker & Docker Compose
docker --version
docker-compose --version

# Git
git --version
```

### Accounts Needed
1. **GitHub** - Version control & CI/CD
2. **OpenAI** - API key for GPT-4
3. **Docker Hub** (optional) - Container registry

---

## Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Client Layer                        │
│                    (React + TypeScript)                     │
└───────────────────────────┬─────────────────────────────────┘
                            │ HTTPS/REST API
┌───────────────────────────▼─────────────────────────────────┐
│                      API Gateway Layer                      │
│              (Django REST Framework + CORS)                 │
└───────────────────────────┬─────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼──────┐  ┌────────▼────────┐  ┌──────▼──────┐
│   Business   │  │   RAG Service   │  │    Auth     │
│    Logic     │  │   (LangChain)   │  │   Service   │
└───────┬──────┘  └────────┬────────┘  └──────┬──────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼──────┐  ┌────────▼────────┐  ┌──────▼──────┐
│  PostgreSQL  │  │  Vector Store   │  │    Redis    │
│   (Primary   │  │ (FAISS/Chroma)  │  │   (Cache/   │
│   Database)  │  │                 │  │    Queue)   │
└──────────────┘  └─────────────────┘  └─────────────┘
                            │
                    ┌───────▼────────┐
                    │   S3/MinIO     │
                    │  (Documents)   │
                    └────────────────┘
```

### Data Flow (RAG Pipeline)

```
User Question → API → Document Retrieval → Vector Search →
Context Extraction → LLM Prompt → GPT-4 → Response → API → User
```

---

## Development Roadmap

### Phase 1: Foundation (Weeks 1-2)
- Project structure setup
- Django backend scaffolding
- Database design & models
- Basic authentication
- GitHub repository setup

### Phase 2: Core Features (Weeks 3-4)
- Document upload & processing
- RAG implementation
- Vector embeddings
- Q&A endpoints

### Phase 3: Frontend (Weeks 5-6)
- React app setup
- UI components
- State management
- API integration

### Phase 4: Production Ready (Weeks 7-8)
- Docker containerization
- CI/CD pipeline
- Testing suite
- Documentation
- Performance optimization

---

## Milestones

### 🎯 MILESTONE 1: Project Setup & Django Foundation

**Goal:** Set up the project structure, initialize Django backend, and create GitHub repository

**Tasks:**
1. Create project directory structure
2. Set up Python virtual environment
3. Initialize Django project with DRF
4. Configure PostgreSQL
5. Set up environment variables (.env)
6. Create .gitignore
7. Initialize Git repository
8. Create GitHub repository
9. First commit & push

**Commands:**
```bash
# 1. Create project directory
mkdir intelligent-doc-assistant
cd intelligent-doc-assistant

# 2. Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Create requirements.txt
touch requirements.txt
```

**requirements.txt (Initial):**
```
Django==5.0.0
djangorestframework==3.14.0
django-cors-headers==4.3.0
psycopg2-binary==2.9.9
python-decouple==3.8
django-environ==0.11.2
pillow==10.1.0
```

**Backend Directory Structure:**
```
intelligent-doc-assistant/
├── backend/
│   ├── config/              # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── apps/
│   │   ├── users/           # User management
│   │   ├── documents/       # Document handling
│   │   ├── qa/              # Q&A functionality
│   │   └── core/            # Shared utilities
│   ├── requirements/
│   │   ├── base.txt
│   │   ├── development.txt
│   │   └── production.txt
│   ├── manage.py
│   └── .env.example
├── frontend/                 # (Milestone 5)
├── docker/                   # (Milestone 7)
├── .github/                  # (Milestone 8)
│   └── workflows/
├── docs/
├── .gitignore
├── .env.example
├── docker-compose.yml       # (Milestone 7)
├── README.md
└── Claude.md                # This file
```

**Django Setup Commands:**
```bash
# Install dependencies
pip install -r requirements.txt

# Create Django project
django-admin startproject config backend
cd backend

# Create apps
python manage.py startapp users apps/users
python manage.py startapp documents apps/documents
python manage.py startapp qa apps/qa
python manage.py startapp core apps/core
```

**Environment Variables (.env.example):**
```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_NAME=intelligent_doc_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# OpenAI
OPENAI_API_KEY=sk-...

# Redis
REDIS_URL=redis://localhost:6379/0

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

**PostgreSQL Database Setup:**
```sql
-- Run in psql or PostgreSQL client
CREATE DATABASE intelligent_doc_db;
CREATE USER doc_user WITH PASSWORD 'your-password';
ALTER ROLE doc_user SET client_encoding TO 'utf8';
ALTER ROLE doc_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE doc_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE intelligent_doc_db TO doc_user;

-- Enable pgvector extension (for vector embeddings)
\c intelligent_doc_db
CREATE EXTENSION IF NOT EXISTS vector;
```

**Updated config/settings.py (Key sections):**
```python
import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Application definition
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
    'apps.users',
    'apps.documents',
    'apps.qa',
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database
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

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# CORS Settings
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='').split(',')
CORS_ALLOW_CREDENTIALS = True

# Custom User Model (we'll create this)
AUTH_USER_MODEL = 'users.User'
```

**.gitignore:**
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
*.egg-info/
dist/
build/

# Django
*.log
db.sqlite3
db.sqlite3-journal
media/
staticfiles/

# Environment
.env
.env.local
.env.*.local

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.coverage
htmlcov/
.pytest_cache/

# Node
node_modules/
npm-debug.log
yarn-error.log

# Docker
*.pid
```

**Git & GitHub Setup:**
```bash
# Initialize Git
git init
git add .
git commit -m "Initial commit: Django project setup with DRF"

# Create GitHub repository (via GitHub CLI or web interface)
# Option 1: GitHub CLI
gh repo create intelligent-doc-assistant --public --source=. --remote=origin

# Option 2: Manual (create repo on GitHub.com, then:)
git remote add origin https://github.com/YOUR-USERNAME/intelligent-doc-assistant.git
git branch -M main
git push -u origin main
```

**✅ Milestone 1 Checklist:**
- [ ] Project directory created
- [ ] Virtual environment set up
- [ ] Django project initialized
- [ ] All apps created (users, documents, qa, core)
- [ ] PostgreSQL database configured
- [ ] .env file created (from .env.example)
- [ ] .gitignore configured
- [ ] GitHub repository created
- [ ] Initial commit pushed

**🎓 What You Learned:**
- Django project structure best practices
- Environment variable management
- PostgreSQL setup and configuration
- Git workflow fundamentals

---

### 🎯 MILESTONE 2: Database Models & Authentication

**Goal:** Design database schema, implement custom user model, and set up JWT authentication

**Tasks:**
1. Create custom User model
2. Design document and Q&A models
3. Set up JWT authentication
4. Create user registration/login endpoints
5. Write database migrations
6. Test authentication flow

**New Dependencies (add to requirements/base.txt):**
```
djangorestframework-simplejwt==5.3.0
django-filter==23.5
```

**User Model (apps/users/models.py):**
```python
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model with additional fields
    """
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    # Professional information (relevant for job application)
    github_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    # Usage tracking
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

**Document Model (apps/documents/models.py):**
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

    # File information
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    file_size = models.BigIntegerField(help_text='File size in bytes')

    # Processing status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
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
    """Text chunks from documents with vector embeddings for RAG"""
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

    # Vector embedding (1536 dimensions for OpenAI text-embedding-ada-002)
    embedding = VectorField(dimensions=1536, null=True, blank=True)

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

**Q&A Models (apps/qa/models.py):**
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
    sources = models.JSONField(default=list, help_text='List of source document chunks')
    confidence_score = models.FloatField(null=True, blank=True)

    # Timing
    processing_time_ms = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # User feedback
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

**User Serializers (apps/users/serializers.py):**
```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'password_confirm',
            'first_name', 'last_name', 'phone'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'phone', 'avatar', 'bio', 'github_profile', 'linkedin_profile',
            'portfolio_url', 'created_at', 'is_verified',
            'total_documents', 'total_questions'
        )
        read_only_fields = ('id', 'created_at', 'is_verified', 'total_documents', 'total_questions')
```

**Authentication Views (apps/users/views.py):**
```python
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from .serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'user': UserSerializer(user).data,
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
```

**API URLs (backend/config/urls.py):**
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/v1/auth/', include([
        path('register/', include('apps.users.urls')),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ])),

    path('api/v1/documents/', include('apps.documents.urls')),
    path('api/v1/qa/', include('apps.qa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Run Migrations:**
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

**Testing Authentication:**
```bash
# Start development server
python manage.py runserver

# Test registration endpoint
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "SecurePass123!",
    "password_confirm": "SecurePass123!",
    "first_name": "Test",
    "last_name": "User"
  }'

# Test login (get JWT tokens)
curl -X POST http://localhost:8000/api/v1/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123!"
  }'
```

**✅ Milestone 2 Checklist:**
- [ ] Custom User model created
- [ ] Document models implemented
- [ ] Q&A models implemented
- [ ] JWT authentication configured
- [ ] User registration endpoint working
- [ ] Login/token endpoints working
- [ ] Database migrations applied
- [ ] Admin panel accessible
- [ ] API tested with curl/Postman
- [ ] Code committed and pushed to GitHub

**Git Commit:**
```bash
git add .
git commit -m "Milestone 2: Database models and JWT authentication"
git push origin main
```

**🎓 What You Learned:**
- Django model design best practices
- Custom User model implementation
- JWT authentication with DRF
- PostgreSQL pgvector for embeddings
- RESTful API design patterns

---

### 🎯 MILESTONE 3: Document Upload & Processing

**Goal:** Implement document upload, parsing, text extraction, and chunk processing

**Tasks:**
1. Create document upload endpoint
2. Implement file parsing (PDF, DOCX, TXT)
3. Set up Celery for background processing
4. Create text chunking logic
5. Implement document management endpoints (list, retrieve, delete)

**New Dependencies:**
```bash
# Add to requirements/base.txt
celery==5.3.4
redis==5.0.1
PyPDF2==3.0.1
python-docx==1.1.0
python-magic==0.4.27
```

**Celery Configuration (config/celery.py):**
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

**Add to config/__init__.py:**
```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

**Settings update (config/settings.py):**
```python
# Celery Configuration
CELERY_BROKER_URL = config('REDIS_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = config('REDIS_URL', default='redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# File Upload Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Max file size: 50MB
MAX_UPLOAD_SIZE = 50 * 1024 * 1024

ALLOWED_DOCUMENT_TYPES = ['pdf', 'docx', 'txt', 'md']
```

**Document Processing Utility (apps/documents/utils.py):**
```python
import magic
import PyPDF2
from docx import Document as DocxDocument
from typing import Tuple, List
import re


class DocumentProcessor:
    """Utility class for document text extraction and processing"""

    @staticmethod
    def detect_file_type(file_path: str) -> str:
        """Detect file MIME type"""
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> Tuple[str, int]:
        """Extract text from PDF file"""
        text = ""
        page_count = 0

        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                page_count = len(pdf_reader.pages)

                for page_num in range(page_count):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n\n"
        except Exception as e:
            raise Exception(f"Error extracting PDF text: {str(e)}")

        return text.strip(), page_count

    @staticmethod
    def extract_text_from_docx(file_path: str) -> Tuple[str, int]:
        """Extract text from DOCX file"""
        try:
            doc = DocxDocument(file_path)
            text = "\n\n".join([para.text for para in doc.paragraphs if para.text])
            page_count = len(doc.paragraphs) // 20  # Rough estimate
            return text, max(1, page_count)
        except Exception as e:
            raise Exception(f"Error extracting DOCX text: {str(e)}")

    @staticmethod
    def extract_text_from_txt(file_path: str) -> Tuple[str, int]:
        """Extract text from TXT file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            page_count = 1
            return text, page_count
        except Exception as e:
            raise Exception(f"Error reading TXT file: {str(e)}")

    @staticmethod
    def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """
        Split text into overlapping chunks

        Args:
            text: Input text
            chunk_size: Maximum characters per chunk
            overlap: Characters to overlap between chunks

        Returns:
            List of text chunks
        """
        # Clean text
        text = re.sub(r'\s+', ' ', text).strip()

        if len(text) <= chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size

            # Try to break at sentence boundary
            if end < len(text):
                # Look for sentence end in the last 100 chars
                last_period = text.rfind('.', start, end)
                last_newline = text.rfind('\n', start, end)
                break_point = max(last_period, last_newline)

                if break_point > start:
                    end = break_point + 1

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

**Document Tasks (apps/documents/tasks.py):**
```python
from celery import shared_task
from django.utils import timezone
import os

from .models import Document, DocumentChunk
from .utils import DocumentProcessor


@shared_task
def process_document(document_id: str):
    """
    Celery task to process uploaded document:
    1. Extract text
    2. Create chunks
    3. Generate embeddings (Milestone 4)
    """
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
        chunks = processor.chunk_text(text, chunk_size=1000, overlap=200)

        # Save chunks to database
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
        return f"Error processing document {document_id}: {str(e)}"
```

**Document Serializers (apps/documents/serializers.py):**
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
            'status', 'processing_error', 'extracted_text',
            'page_count', 'word_count', 'chunks_count',
            'created_at', 'updated_at', 'processed_at'
        )
        read_only_fields = (
            'id', 'file_size', 'status', 'processing_error',
            'extracted_text', 'page_count', 'word_count',
            'created_at', 'updated_at', 'processed_at'
        )

    def get_chunks_count(self, obj):
        return obj.chunks.count()


class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'file', 'file_type', 'collection')

    def validate_file(self, value):
        # Validate file size
        if value.size > 50 * 1024 * 1024:  # 50MB
            raise serializers.ValidationError("File size must be under 50MB")
        return value

    def create(self, validated_data):
        # Set file size
        validated_data['file_size'] = validated_data['file'].size
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class DocumentCollectionSerializer(serializers.ModelSerializer):
    documents_count = serializers.SerializerMethodField()

    class Meta:
        model = DocumentCollection
        fields = ('id', 'name', 'description', 'documents_count', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_documents_count(self, obj):
        return obj.documents.count()
```

**Document Views (apps/documents/views.py):**
```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Document, DocumentCollection, DocumentChunk
from .serializers import (
    DocumentSerializer, DocumentUploadSerializer,
    DocumentCollectionSerializer, DocumentChunkSerializer
)
from .tasks import process_document


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'file_type', 'collection']
    search_fields = ['title', 'extracted_text']
    ordering_fields = ['created_at', 'updated_at', 'title']
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

    @action(detail=True, methods=['post'])
    def reprocess(self, request, pk=None):
        """Reprocess a document"""
        document = self.get_object()
        # Delete existing chunks
        document.chunks.all().delete()
        # Trigger reprocessing
        process_document.delay(str(document.id))
        return Response({'status': 'Document reprocessing started'})


class DocumentCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentCollectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DocumentCollection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def documents(self, request, pk=None):
        """Get all documents in a collection"""
        collection = self.get_object()
        documents = collection.documents.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
```

**Document URLs (apps/documents/urls.py):**
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

**Running Celery:**
```bash
# Terminal 1: Start Redis
redis-server

# Terminal 2: Start Celery worker
cd backend
celery -A config worker -l info

# Terminal 3: Start Django dev server
python manage.py runserver
```

**Testing Document Upload:**
```bash
# Get JWT token first
TOKEN="your-jwt-token-here"

# Upload document
curl -X POST http://localhost:8000/api/v1/documents/documents/ \
  -H "Authorization: Bearer $TOKEN" \
  -F "title=Test Document" \
  -F "file=@/path/to/document.pdf" \
  -F "file_type=pdf"

# List documents
curl http://localhost:8000/api/v1/documents/documents/ \
  -H "Authorization: Bearer $TOKEN"

# Get document chunks
curl http://localhost:8000/api/v1/documents/documents/{document_id}/chunks/ \
  -H "Authorization: Bearer $TOKEN"
```

**✅ Milestone 3 Checklist:**
- [ ] Celery configured with Redis
- [ ] Document upload endpoint working
- [ ] PDF text extraction working
- [ ] DOCX text extraction working
- [ ] TXT file handling working
- [ ] Text chunking implemented
- [ ] Background processing with Celery
- [ ] Document listing/filtering working
- [ ] Collection management working
- [ ] Error handling for failed uploads
- [ ] Code committed and pushed

**Git Commit:**
```bash
git add .
git commit -m "Milestone 3: Document upload and processing system"
git push origin main
```

**🎓 What You Learned:**
- Celery task queue implementation
- File upload handling in Django
- Text extraction from multiple formats
- Chunking strategies for RAG
- Background job processing

---

### 🎯 MILESTONE 4: RAG Implementation (Vector Embeddings & LLM)

**Goal:** Implement the core RAG functionality with vector embeddings and OpenAI integration

**Tasks:**
1. Set up OpenAI API integration
2. Generate vector embeddings for document chunks
3. Implement vector similarity search
4. Create Q&A endpoint with RAG
5. Implement context retrieval and prompt engineering

**New Dependencies:**
```bash
# Add to requirements/base.txt
openai==1.6.0
langchain==0.1.0
langchain-openai==0.0.2
tiktoken==0.5.2
numpy==1.26.2
faiss-cpu==1.7.4  # or faiss-gpu for GPU support
```

**RAG Service (apps/qa/services/rag_service.py):**
```python
import openai
from typing import List, Dict, Tuple
import numpy as np
from django.conf import settings
import faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage

from apps.documents.models import DocumentChunk, Document

openai.api_key = settings.OPENAI_API_KEY


class RAGService:
    """Service for Retrieval-Augmented Generation"""

    def __init__(self):
        self.embeddings_model = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            openai_api_key=settings.OPENAI_API_KEY
        )
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
        self.embedding_dimension = 1536

    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding vector for text"""
        try:
            embedding = self.embeddings_model.embed_query(text)
            return embedding
        except Exception as e:
            raise Exception(f"Error generating embedding: {str(e)}")

    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        try:
            embeddings = self.embeddings_model.embed_documents(texts)
            return embeddings
        except Exception as e:
            raise Exception(f"Error generating embeddings: {str(e)}")

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
        system_prompt = """You are an intelligent document assistant. Your role is to answer questions based ONLY on the provided context from the user's documents.

Rules:
1. Only use information from the provided context
2. If the answer is not in the context, say "I don't have enough information to answer that"
3. Cite sources by referring to [Source X] numbers
4. Be concise but complete
5. If you're uncertain, express that clearly"""

        user_prompt = f"""Context from documents:
{context_text}

{"Previous conversation:" + history_text if history_text else ""}

Question: {question}

Please provide a detailed answer based on the context above."""

        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ]

            response = self.llm.invoke(messages)
            answer = response.content

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
                'model': 'gpt-4'
            }

        except Exception as e:
            raise Exception(f"Error generating answer: {str(e)}")
```

**Update Document Processing Task (apps/documents/tasks.py):**
```python
from apps.qa.services.rag_service import RAGService

@shared_task
def process_document(document_id: str):
    """Process document and generate embeddings"""
    try:
        # ... (previous code for text extraction and chunking)

        # Generate embeddings
        rag_service = RAGService()
        embedded_count = rag_service.embed_document_chunks(document_id)

        print(f"Generated embeddings for {embedded_count} chunks")

        document.status = 'completed'
        document.processed_at = timezone.now()
        document.save()

        return f"Document {document_id} processed with {embedded_count} embeddings"

    except Exception as e:
        document.status = 'failed'
        document.processing_error = str(e)
        document.save()
        return f"Error processing document: {str(e)}"
```

**Q&A Serializers (apps/qa/serializers.py):**
```python
from rest_framework import serializers
from .models import Conversation, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id', 'question_text', 'answer_text', 'sources',
            'confidence_score', 'processing_time_ms', 'created_at',
            'is_helpful', 'feedback_text'
        )
        read_only_fields = (
            'id', 'answer_text', 'sources', 'confidence_score',
            'processing_time_ms', 'created_at'
        )


class AskQuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=1000)
    document_ids = serializers.ListField(
        child=serializers.UUIDField(),
        required=False,
        allow_empty=True
    )
    conversation_id = serializers.UUIDField(required=False, allow_null=True)


class ConversationSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    latest_question = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = (
            'id', 'title', 'questions_count', 'latest_question',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_questions_count(self, obj):
        return obj.questions.count()

    def get_latest_question(self, obj):
        latest = obj.questions.last()
        if latest:
            return QuestionSerializer(latest).data
        return None
```

**Q&A Views (apps/qa/views.py):**
```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
import time

from .models import Conversation, Question
from .serializers import (
    ConversationSerializer, QuestionSerializer, AskQuestionSerializer
)
from .services.rag_service import RAGService


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        """Get all questions in a conversation"""
        conversation = self.get_object()
        questions = conversation.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def ask(self, request):
        """Ask a question and get RAG-powered answer"""
        serializer = AskQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question_text = serializer.validated_data['question']
        document_ids = serializer.validated_data.get('document_ids', None)
        conversation_id = serializer.validated_data.get('conversation_id', None)

        start_time = time.time()

        try:
            # Get or create conversation
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

            # Initialize RAG service
            rag_service = RAGService()

            # Search for relevant chunks
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

            # Get conversation history
            previous_questions = conversation.questions.all().order_by('created_at')
            history = [
                {'question': q.question_text, 'answer': q.answer_text}
                for q in previous_questions[-3:]
            ]

            # Generate answer
            result = rag_service.generate_answer(
                question=question_text,
                context_chunks=similar_chunks,
                conversation_history=history
            )

            processing_time = int((time.time() - start_time) * 1000)

            # Calculate average confidence score
            avg_confidence = sum(s['similarity_score'] for s in result['sources']) / len(result['sources'])

            # Create question record
            question = Question.objects.create(
                conversation=conversation,
                user=request.user,
                question_text=question_text,
                answer_text=result['answer'],
                sources=result['sources'],
                confidence_score=avg_confidence,
                processing_time_ms=processing_time
            )

            # Update user stats
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
            }, status=status.HTTP_200_OK)

        except Conversation.DoesNotExist:
            return Response({
                'error': 'Conversation not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def feedback(self, request, pk=None):
        """Submit feedback on answer quality"""
        question = self.get_object()
        is_helpful = request.data.get('is_helpful')
        feedback_text = request.data.get('feedback_text', '')

        if is_helpful is not None:
            question.is_helpful = is_helpful
            question.feedback_text = feedback_text
            question.save()

            return Response({'status': 'Feedback recorded'})

        return Response(
            {'error': 'is_helpful field is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
```

**Q&A URLs (apps/qa/urls.py):**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
]
```

**Testing RAG:**
```bash
# Upload a document first, then:

# Ask a question
curl -X POST http://localhost:8000/api/v1/qa/conversations/ask/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the main topic of the document?",
    "document_ids": ["document-uuid-here"]
  }'

# Continue conversation
curl -X POST http://localhost:8000/api/v1/qa/conversations/ask/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Can you tell me more about that?",
    "conversation_id": "conversation-uuid-here"
  }'

# Get conversation history
curl http://localhost:8000/api/v1/qa/conversations/{conversation_id}/questions/ \
  -H "Authorization: Bearer $TOKEN"
```

**✅ Milestone 4 Checklist:**
- [ ] OpenAI API integrated
- [ ] Vector embeddings generated for chunks
- [ ] FAISS vector search working
- [ ] RAG service implemented
- [ ] Q&A endpoint functional
- [ ] Context retrieval working
- [ ] Prompt engineering implemented
- [ ] Conversation history maintained
- [ ] Source citations included
- [ ] Feedback mechanism working
- [ ] Code committed and pushed

**Git Commit:**
```bash
git add .
git commit -m "Milestone 4: RAG implementation with OpenAI and vector search"
git push origin main
```

**🎓 What You Learned:**
- RAG architecture and implementation
- Vector embeddings and similarity search
- LangChain framework usage
- OpenAI API integration
- FAISS for efficient vector search
- Prompt engineering techniques

---

### 🎯 MILESTONE 5: React Frontend Foundation

**Goal:** Set up React frontend with TypeScript, Redux, and Material-UI

I'll continue in the next message with Milestones 5-10...

---

### 🎯 MILESTONE 5: React Frontend Foundation

**Goal:** Set up React application with TypeScript, Redux Toolkit, and Material-UI

**Tasks:**
1. Initialize React app with Vite + TypeScript
2. Set up project structure
3. Configure Redux Toolkit
4. Set up routing with React Router
5. Configure Axios for API calls
6. Create authentication context
7. Implement login/register pages

**Setup Commands:**
```bash
# Navigate to project root
cd intelligent-doc-assistant

# Create React app with Vite
npm create vite@latest frontend -- --template react-ts

cd frontend
npm install

# Install dependencies
npm install @reduxjs/toolkit react-redux
npm install react-router-dom
npm install @mui/material @mui/icons-material @emotion/react @emotion/styled
npm install axios
npm install react-hook-form yup @hookform/resolvers
npm install @tanstack/react-query
```

**Frontend Directory Structure:**
```
frontend/
├── public/
├── src/
│   ├── app/
│   │   ├── store.ts              # Redux store
│   │   └── hooks.ts              # Custom hooks
│   ├── features/
│   │   ├── auth/
│   │   │   ├── authSlice.ts
│   │   │   ├── authAPI.ts
│   │   │   ├── Login.tsx
│   │   │   └── Register.tsx
│   │   ├── documents/
│   │   │   ├── documentsSlice.ts
│   │   │   ├── documentsAPI.ts
│   │   │   ├── DocumentList.tsx
│   │   │   ├── DocumentUpload.tsx
│   │   │   └── DocumentViewer.tsx
│   │   └── qa/
│   │       ├── qaSlice.ts
│   │       ├── qaAPI.ts
│   │       ├── ChatInterface.tsx
│   │       └── ConversationList.tsx
│   ├── components/
│   │   ├── common/
│   │   │   ├── Layout.tsx
│   │   │   ├── Navbar.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   └── Loading.tsx
│   │   └── ProtectedRoute.tsx
│   ├── services/
│   │   ├── api.ts               # Axios instance
│   │   └── authService.ts
│   ├── types/
│   │   ├── auth.types.ts
│   │   ├── document.types.ts
│   │   └── qa.types.ts
│   ├── utils/
│   │   ├── constants.ts
│   │   └── helpers.ts
│   ├── App.tsx
│   ├── main.tsx
│   └── vite-env.d.ts
├── .env.example
├── .eslintrc.cjs
├── package.json
├── tsconfig.json
└── vite.config.ts
```

**Environment Variables (frontend/.env.example):**
```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

**Types (src/types/auth.types.ts):**
```typescript
export interface User {
  id: string;
  email: string;
  username: string;
  first_name: string;
  last_name: string;
  avatar?: string;
  total_documents: number;
  total_questions: number;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterData {
  email: string;
  username: string;
  password: string;
  password_confirm: string;
  first_name: string;
  last_name: string;
}

export interface AuthResponse {
  access: string;
  refresh: string;
  user: User;
}

export interface AuthState {
  user: User | null;
  accessToken: string | null;
  refreshToken: string | null;
  isAuthenticated: boolean;
  loading: boolean;
  error: string | null;
}
```

**Types (src/types/document.types.ts):**
```typescript
export interface Document {
  id: string;
  title: string;
  file: string;
  file_type: 'pdf' | 'docx' | 'txt' | 'md';
  file_size: number;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  processing_error?: string;
  page_count: number;
  word_count: number;
  chunks_count: number;
  created_at: string;
  updated_at: string;
  processed_at?: string;
}

export interface DocumentUploadData {
  title: string;
  file: File;
  file_type: string;
  collection?: string;
}
```

**Types (src/types/qa.types.ts):**
```typescript
export interface Source {
  document_id: string;
  document_title: string;
  chunk_id: string;
  page_number: number;
  text_preview: string;
  similarity_score: number;
}

export interface Question {
  id: string;
  question_text: string;
  answer_text: string;
  sources: Source[];
  confidence_score: number;
  processing_time_ms: number;
  created_at: string;
  is_helpful?: boolean;
}

export interface Conversation {
  id: string;
  title: string;
  questions_count: number;
  latest_question?: Question;
  created_at: string;
  updated_at: string;
}

export interface AskQuestionData {
  question: string;
  document_ids?: string[];
  conversation_id?: string;
}
```

**Axios Instance (src/services/api.ts):**
```typescript
import axios, { AxiosError, AxiosResponse } from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for token refresh
api.interceptors.response.use(
  (response: AxiosResponse) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config as any;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post(`${API_BASE_URL}/auth/token/refresh/`, {
          refresh: refreshToken,
        });

        const { access } = response.data;
        localStorage.setItem('accessToken', access);

        originalRequest.headers.Authorization = `Bearer ${access}`;
        return api(originalRequest);
      } catch (refreshError) {
        // Refresh failed, logout user
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

export default api;
```

**Redux Store (src/app/store.ts):**
```typescript
import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../features/auth/authSlice';
import documentsReducer from '../features/documents/documentsSlice';
import qaReducer from '../features/qa/qaSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    documents: documentsReducer,
    qa: qaReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

**Redux Hooks (src/app/hooks.ts):**
```typescript
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';
import type { RootState, AppDispatch } from './store';

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
```

**Auth Slice (src/features/auth/authSlice.ts):**
```typescript
import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import api from '../../services/api';
import { AuthState, LoginCredentials, RegisterData, AuthResponse, User } from '../../types/auth.types';

const initialState: AuthState = {
  user: null,
  accessToken: localStorage.getItem('accessToken'),
  refreshToken: localStorage.getItem('refreshToken'),
  isAuthenticated: !!localStorage.getItem('accessToken'),
  loading: false,
  error: null,
};

// Async thunks
export const login = createAsyncThunk(
  'auth/login',
  async (credentials: LoginCredentials, { rejectWithValue }) => {
    try {
      const response = await api.post<AuthResponse>('/auth/token/', credentials);
      const { access, refresh } = response.data;

      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);

      // Fetch user profile
      const userResponse = await api.get<User>('/auth/profile/');
      return { ...response.data, user: userResponse.data };
    } catch (error: any) {
      return rejectWithValue(error.response?.data || 'Login failed');
    }
  }
);

export const register = createAsyncThunk(
  'auth/register',
  async (data: RegisterData, { rejectWithValue }) => {
    try {
      const response = await api.post('/auth/register/', data);
      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data || 'Registration failed');
    }
  }
);

export const fetchUserProfile = createAsyncThunk(
  'auth/fetchProfile',
  async (_, { rejectWithValue }) => {
    try {
      const response = await api.get<User>('/auth/profile/');
      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data || 'Failed to fetch profile');
    }
  }
);

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    logout: (state) => {
      state.user = null;
      state.accessToken = null;
      state.refreshToken = null;
      state.isAuthenticated = false;
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    builder
      // Login
      .addCase(login.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.loading = false;
        state.isAuthenticated = true;
        state.user = action.payload.user;
        state.accessToken = action.payload.access;
        state.refreshToken = action.payload.refresh;
      })
      .addCase(login.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      // Register
      .addCase(register.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(register.fulfilled, (state) => {
        state.loading = false;
      })
      .addCase(register.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      // Fetch Profile
      .addCase(fetchUserProfile.fulfilled, (state, action) => {
        state.user = action.payload;
      });
  },
});

export const { logout, clearError } = authSlice.actions;
export default authSlice.reducer;
```

**Login Component (src/features/auth/Login.tsx):**
```typescript
import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import {
  Box,
  Button,
  Container,
  TextField,
  Typography,
  Alert,
  Paper,
  Link as MuiLink,
} from '@mui/material';
import { useAppDispatch, useAppSelector } from '../../app/hooks';
import { login } from './authSlice';
import { LoginCredentials } from '../../types/auth.types';

const schema = yup.object({
  email: yup.string().email('Invalid email').required('Email is required'),
  password: yup.string().required('Password is required'),
});

const Login: React.FC = () => {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const { loading, error } = useAppSelector((state) => state.auth);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginCredentials>({
    resolver: yupResolver(schema),
  });

  const onSubmit = async (data: LoginCredentials) => {
    const result = await dispatch(login(data));
    if (login.fulfilled.match(result)) {
      navigate('/dashboard');
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Paper elevation={3} sx={{ p: 4, width: '100%' }}>
          <Typography component="h1" variant="h4" align="center" gutterBottom>
            Intelligent Doc Assistant
          </Typography>
          <Typography component="h2" variant="h6" align="center" gutterBottom>
            Sign In
          </Typography>

          {error && (
            <Alert severity="error" sx={{ mb: 2 }}>
              {JSON.stringify(error)}
            </Alert>
          )}

          <Box component="form" onSubmit={handleSubmit(onSubmit)} sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              autoComplete="email"
              autoFocus
              {...register('email')}
              error={!!errors.email}
              helperText={errors.email?.message}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              {...register('password')}
              error={!!errors.password}
              helperText={errors.password?.message}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              disabled={loading}
            >
              {loading ? 'Signing In...' : 'Sign In'}
            </Button>
            <Box sx={{ textAlign: 'center' }}>
              <MuiLink component={Link} to="/register" variant="body2">
                Don't have an account? Sign Up
              </MuiLink>
            </Box>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
};

export default Login;
```

**App.tsx with Routing:**
```typescript
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { Provider } from 'react-redux';
import { store } from './app/store';

import Login from './features/auth/Login';
import Register from './features/auth/Register';
import Dashboard from './pages/Dashboard';
import ProtectedRoute from './components/ProtectedRoute';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Router>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route
              path="/dashboard"
              element={
                <ProtectedRoute>
                  <Dashboard />
                </ProtectedRoute>
              }
            />
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </Router>
      </ThemeProvider>
    </Provider>
  );
}

export default App;
```

**Protected Route Component:**
```typescript
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAppSelector } from '../app/hooks';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { isAuthenticated } = useAppSelector((state) => state.auth);

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
};

export default ProtectedRoute;
```

**Run Frontend:**
```bash
cd frontend
npm run dev
```

**✅ Milestone 5 Checklist:**
- [ ] React app created with Vite + TypeScript
- [ ] Redux Toolkit configured
- [ ] React Router set up
- [ ] Axios instance configured
- [ ] Auth slice implemented
- [ ] Login page working
- [ ] Register page working
- [ ] Protected routes working
- [ ] Material-UI theme configured
- [ ] Code committed and pushed

**Git Commit:**
```bash
git add .
git commit -m "Milestone 5: React frontend foundation with auth"
git push origin main
```

**🎓 What You Learned:**
- React + TypeScript setup with Vite
- Redux Toolkit state management
- React Router for navigation
- Form handling with react-hook-form
- Material-UI component library
- JWT token management in frontend

---

### 🎯 MILESTONE 6: Frontend-Backend Integration

**Goal:** Build document management and Q&A chat interfaces

**Tasks:**
1. Create document upload UI
2. Build document list with filtering
3. Implement chat interface
4. Add real-time status updates
5. Build conversation history

**Documents Slice (src/features/documents/documentsSlice.ts):**
```typescript
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import api from '../../services/api';
import { Document, DocumentUploadData } from '../../types/document.types';

interface DocumentsState {
  documents: Document[];
  loading: boolean;
  error: string | null;
  uploadProgress: number;
}

const initialState: DocumentsState = {
  documents: [],
  loading: false,
  error: null,
  uploadProgress: 0,
};

export const fetchDocuments = createAsyncThunk(
  'documents/fetchAll',
  async () => {
    const response = await api.get<Document[]>('/documents/documents/');
    return response.data;
  }
);

export const uploadDocument = createAsyncThunk(
  'documents/upload',
  async (data: DocumentUploadData, { rejectWithValue }) => {
    try {
      const formData = new FormData();
      formData.append('title', data.title);
      formData.append('file', data.file);
      formData.append('file_type', data.file_type);

      const response = await api.post<Document>('/documents/documents/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data);
    }
  }
);

export const deleteDocument = createAsyncThunk(
  'documents/delete',
  async (id: string) => {
    await api.delete(`/documents/documents/${id}/`);
    return id;
  }
);

const documentsSlice = createSlice({
  name: 'documents',
  initialState,
  reducers: {
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchDocuments.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchDocuments.fulfilled, (state, action) => {
        state.loading = false;
        state.documents = action.payload;
      })
      .addCase(fetchDocuments.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Failed to fetch documents';
      })
      .addCase(uploadDocument.fulfilled, (state, action) => {
        state.documents.unshift(action.payload);
      })
      .addCase(deleteDocument.fulfilled, (state, action) => {
        state.documents = state.documents.filter(doc => doc.id !== action.payload);
      });
  },
});

export const { clearError } = documentsSlice.actions;
export default documentsSlice.reducer;
```

**Chat Interface (src/features/qa/ChatInterface.tsx):**
```typescript
import React, { useState, useRef, useEffect } from 'react';
import {
  Box,
  TextField,
  Button,
  Paper,
  Typography,
  CircularProgress,
  Chip,
  Card,
  CardContent,
  IconButton,
  Collapse,
} from '@mui/material';
import SendIcon from '@mui/icons-material/Send';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import ThumbDownIcon from '@mui/icons-material/ThumbDown';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { styled } from '@mui/material/styles';
import api from '../../services/api';
import { Question, AskQuestionData } from '../../types/qa.types';

const MessageBox = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(2),
  marginBottom: theme.spacing(2),
  maxWidth: '80%',
}));

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Question[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [expandedSources, setExpandedSources] = useState<{ [key: string]: boolean }>({});
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const questionText = input;
    setInput('');
    setLoading(true);

    try {
      const data: AskQuestionData = {
        question: questionText,
        conversation_id: conversationId || undefined,
      };

      const response = await api.post('/qa/conversations/ask/', data);
      const newQuestion: Question = {
        id: response.data.question_id,
        question_text: questionText,
        answer_text: response.data.answer,
        sources: response.data.sources,
        confidence_score: response.data.confidence_score,
        processing_time_ms: response.data.processing_time_ms,
        created_at: new Date().toISOString(),
      };

      setMessages([...messages, newQuestion]);
      setConversationId(response.data.conversation_id);
    } catch (error) {
      console.error('Error asking question:', error);
    } finally {
      setLoading(false);
    }
  };

  const toggleSources = (questionId: string) => {
    setExpandedSources({
      ...expandedSources,
      [questionId]: !expandedSources[questionId],
    });
  };

  return (
    <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <Box sx={{ flexGrow: 1, overflow: 'auto', p: 2 }}>
        {messages.length === 0 && (
          <Box sx={{ textAlign: 'center', mt: 4 }}>
            <Typography variant="h6" color="text.secondary">
              Ask me anything about your documents
            </Typography>
          </Box>
        )}

        {messages.map((question) => (
          <Box key={question.id}>
            <MessageBox sx={{ ml: 'auto', bgcolor: 'primary.light' }}>
              <Typography variant="body1">{question.question_text}</Typography>
            </MessageBox>

            <MessageBox sx={{ mr: 'auto', bgcolor: 'grey.100' }}>
              <Typography variant="body1" paragraph>
                {question.answer_text}
              </Typography>

              <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap', mb: 1 }}>
                <Chip
                  label={`Confidence: ${(question.confidence_score * 100).toFixed(1)}%`}
                  size="small"
                  color="primary"
                  variant="outlined"
                />
                <Chip
                  label={`${question.processing_time_ms}ms`}
                  size="small"
                  variant="outlined"
                />
                <Chip
                  label={`${question.sources.length} sources`}
                  size="small"
                  variant="outlined"
                  onClick={() => toggleSources(question.id)}
                />
              </Box>

              <Collapse in={expandedSources[question.id]}>
                <Box sx={{ mt: 2 }}>
                  <Typography variant="subtitle2" gutterBottom>
                    Sources:
                  </Typography>
                  {question.sources.map((source, idx) => (
                    <Card key={idx} sx={{ mb: 1 }}>
                      <CardContent>
                        <Typography variant="caption" color="text.secondary">
                          {source.document_title} - Page {source.page_number}
                        </Typography>
                        <Typography variant="body2" sx={{ mt: 1 }}>
                          {source.text_preview}
                        </Typography>
                      </CardContent>
                    </Card>
                  ))}
                </Box>
              </Collapse>
            </MessageBox>
          </Box>
        ))}

        {loading && (
          <Box sx={{ display: 'flex', justifyContent: 'center', my: 2 }}>
            <CircularProgress />
          </Box>
        )}

        <div ref={messagesEndRef} />
      </Box>

      <Box sx={{ p: 2, bgcolor: 'background.paper', borderTop: 1, borderColor: 'divider' }}>
        <Box sx={{ display: 'flex', gap: 1 }}>
          <TextField
            fullWidth
            placeholder="Ask a question about your documents..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleSend();
              }
            }}
            disabled={loading}
            multiline
            maxRows={4}
          />
          <Button
            variant="contained"
            onClick={handleSend}
            disabled={loading || !input.trim()}
            endIcon={<SendIcon />}
          >
            Send
          </Button>
        </Box>
      </Box>
    </Box>
  );
};

export default ChatInterface;
```

**✅ Milestone 6 Checklist:**
- [ ] Document upload interface complete
- [ ] Document list with filtering
- [ ] Chat interface functional
- [ ] Source citations displayed
- [ ] Conversation history maintained
- [ ] Real-time updates working
- [ ] Responsive design
- [ ] Error handling
- [ ] Code committed and pushed

---

### 🎯 MILESTONE 7: Docker Containerization

**Goal:** Containerize the entire application with Docker and Docker Compose

**Dockerfile for Backend (backend/Dockerfile):**
```dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/production.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]
```

**Dockerfile for Frontend (frontend/Dockerfile):**
```dockerfile
# Build stage
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**Docker Compose (docker-compose.yml):**
```yaml
version: '3.8'

services:
  db:
    image: pgvector/pgvector:pg15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=intelligent_doc_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./backend:/app
      - media_volume:/app/media
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy

  celery:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: celery -A config worker -l info
    volumes:
      - ./backend:/app
      - media_volume:/app/media
    env_file:
      - ./backend/.env
    depends_on:
      - db
      - redis
      - backend

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    depends_on:
      - backend

volumes:
  postgres_data:
  media_volume:
```

**✅ Milestone 7 Checklist:**
- [ ] Backend Dockerfile created
- [ ] Frontend Dockerfile created
- [ ] Docker Compose configuration complete
- [ ] All services start successfully
- [ ] Database migrations run in container
- [ ] Volumes configured correctly
- [ ] Environment variables working
- [ ] Application accessible via containers
- [ ] Code committed and pushed

**Git Commit:**
```bash
git add .
git commit -m "Milestone 7: Docker containerization complete"
git push origin main
```

---

### 🎯 MILESTONE 8: CI/CD Pipeline with GitHub Actions

**Goal:** Set up automated testing, linting, and deployment pipeline

**GitHub Actions Workflow (.github/workflows/ci.yml):**
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  # Backend Tests
  backend-test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: pgvector/pgvector:pg15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

      redis:
        image: redis:7-alpine
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Cache pip packages
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('backend/requirements/*.txt') }}

    - name: Install dependencies
      run: |
        cd backend
        pip install -r requirements/development.txt

    - name: Run linting
      run: |
        cd backend
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        black --check .

    - name: Run tests with coverage
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        REDIS_URL: redis://localhost:6379/0
      run: |
        cd backend
        pytest --cov=. --cov-report=xml

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./backend/coverage.xml
        flags: backend

  # Frontend Tests
  frontend-test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
        cache-dependency-path: frontend/package-lock.json

    - name: Install dependencies
      run: |
        cd frontend
        npm ci

    - name: Run linting
      run: |
        cd frontend
        npm run lint

    - name: Run tests
      run: |
        cd frontend
        npm run test:ci

    - name: Build
      run: |
        cd frontend
        npm run build

  # Docker Build
  docker-build:
    runs-on: ubuntu-latest
    needs: [backend-test, frontend-test]
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}

    - name: Build and push backend
      uses: docker/build-push-action@v4
      with:
        context: ./backend
        push: true
        tags: your-username/intelligent-doc-backend:latest

    - name: Build and push frontend
      uses: docker/build-push-action@v4
      with:
        context: ./frontend
        push: true
        tags: your-username/intelligent-doc-frontend:latest
```

**Pre-commit Configuration (.pre-commit-config.yaml):**
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black
        language_version: python3.11
        files: ^backend/

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        files: ^backend/
        args: ['--max-line-length=100', '--extend-ignore=E203,W503']

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.56.0
    hooks:
      - id: eslint
        files: ^frontend/src/.*\.[jt]sx?$
        types: [file]
```

**✅ Milestone 8 Checklist:**
- [ ] GitHub Actions workflow created
- [ ] Backend tests running in CI
- [ ] Frontend tests running in CI
- [ ] Code linting automated
- [ ] Docker images building in CI
- [ ] Pre-commit hooks configured
- [ ] Coverage reports generated
- [ ] All checks passing
- [ ] Code committed and pushed

---

### 🎯 MILESTONE 9: Testing & Quality Assurance

**Goal:** Implement comprehensive testing suite

**Backend Tests (backend/apps/qa/tests/test_rag_service.py):**
```python
import pytest
from django.contrib.auth import get_user_model
from apps.documents.models import Document, DocumentChunk
from apps.qa.services.rag_service import RAGService

User = get_user_model()


@pytest.mark.django_db
class TestRAGService:
    @pytest.fixture
    def user(self):
        return User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    @pytest.fixture
    def document(self, user):
        return Document.objects.create(
            user=user,
            title='Test Document',
            file_type='txt',
            file_size=1000,
            status='completed',
            extracted_text='This is a test document about AI and machine learning.'
        )

    @pytest.fixture
    def chunks(self, document):
        chunks = []
        for i in range(3):
            chunk = DocumentChunk.objects.create(
                document=document,
                text=f'Chunk {i}: AI and machine learning content.',
                chunk_index=i
            )
            chunks.append(chunk)
        return chunks

    def test_generate_embedding(self):
        service = RAGService()
        embedding = service.generate_embedding('Test text')
        assert len(embedding) == 1536
        assert all(isinstance(x, float) for x in embedding)

    def test_search_similar_chunks(self, user, document, chunks):
        service = RAGService()

        # Generate embeddings for chunks
        service.embed_document_chunks(str(document.id))

        # Search
        results = service.search_similar_chunks(
            query='AI machine learning',
            user_id=str(user.id),
            top_k=2
        )

        assert len(results) <= 2
        assert all(isinstance(r[0], DocumentChunk) for r in results)
        assert all(isinstance(r[1], float) for r in results)
```

**Frontend Tests (frontend/src/features/auth/Login.test.tsx):**
```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import { configureStore } from '@reduxjs/toolkit';
import Login from './Login';
import authReducer from './authSlice';

const mockStore = configureStore({
  reducer: {
    auth: authReducer,
  },
});

describe('Login Component', () => {
  it('renders login form', () => {
    render(
      <Provider store={mockStore}>
        <BrowserRouter>
          <Login />
        </BrowserRouter>
      </Provider>
    );

    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /sign in/i })).toBeInTheDocument();
  });

  it('shows validation errors for empty fields', async () => {
    render(
      <Provider store={mockStore}>
        <BrowserRouter>
          <Login />
        </BrowserRouter>
      </Provider>
    );

    const submitButton = screen.getByRole('button', { name: /sign in/i });
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/email is required/i)).toBeInTheDocument();
    });
  });
});
```

**✅ Milestone 9 Checklist:**
- [ ] Backend unit tests written
- [ ] Frontend unit tests written
- [ ] Integration tests added
- [ ] Test coverage above 80%
- [ ] All tests passing
- [ ] Code committed and pushed

---

### 🎯 MILESTONE 10: Production Deployment & Optimization

**Goal:** Deploy to production and optimize performance

**Production Considerations:**

1. **Environment Variables:**
   - Use secrets management (AWS Secrets Manager, etc.)
   - Never commit `.env` files

2. **Database:**
   - Set up managed PostgreSQL (AWS RDS, DigitalOcean)
   - Enable automated backups
   - Set up read replicas for scaling

3. **File Storage:**
   - Use S3 or DigitalOcean Spaces
   - Enable CDN for static files

4. **Caching:**
   - Implement Redis caching for API responses
   - Use HTTP caching headers

5. **Monitoring:**
   - Set up Sentry for error tracking
   - Use DataDog/New Relic for APM
   - Configure logging (ELK stack)

6. **Security:**
   - Enable HTTPS (Let's Encrypt)
   - Set up WAF (Cloudflare, AWS WAF)
   - Implement rate limiting
   - Regular security audits

**✅ Milestone 10 Checklist:**
- [ ] Production environment configured
- [ ] Application deployed
- [ ] HTTPS enabled
- [ ] Monitoring set up
- [ ] Error tracking configured
- [ ] Backups automated
- [ ] Performance optimized
- [ ] Security hardened
- [ ] Documentation updated
- [ ] Final commit and push

---

## Best Practices Followed

### Code Quality
✅ **Type Safety:** TypeScript in frontend, type hints in backend
✅ **Linting:** ESLint, Flake8, Black formatter
✅ **Code Review:** Pull request workflow
✅ **Documentation:** Inline comments, API docs (Swagger)

### Architecture
✅ **Separation of Concerns:** Clean architecture layers
✅ **DRY Principle:** Reusable components and utilities
✅ **SOLID Principles:** Single responsibility, dependency injection
✅ **RESTful API Design:** Standard HTTP methods and status codes

### Security
✅ **Authentication:** JWT with refresh tokens
✅ **Authorization:** Role-based access control
✅ **Input Validation:** Server-side validation
✅ **SQL Injection Prevention:** ORM usage
✅ **XSS Protection:** React's built-in escaping
✅ **CSRF Protection:** Django CSRF middleware

### Performance
✅ **Database Indexing:** Optimized queries
✅ **Caching:** Redis for frequently accessed data
✅ **Lazy Loading:** Code splitting in React
✅ **Background Jobs:** Celery for heavy tasks
✅ **CDN Usage:** Static file delivery

### DevOps
✅ **Version Control:** Git with feature branches
✅ **CI/CD:** Automated testing and deployment
✅ **Containerization:** Docker for consistency
✅ **Monitoring:** Error tracking and logging
✅ **Backups:** Automated database backups

---

## Common Pitfalls to Avoid

### Backend
❌ **Don't:** Store sensitive data in code
✅ **Do:** Use environment variables and secrets management

❌ **Don't:** Run heavy operations synchronously
✅ **Do:** Use Celery for background processing

❌ **Don't:** Return raw database errors to frontend
✅ **Do:** Implement proper error handling and logging

❌ **Don't:** Allow unlimited file uploads
✅ **Do:** Implement size limits and validation

### Frontend
❌ **Don't:** Store JWT in localStorage without consideration
✅ **Do:** Understand XSS risks and implement proper security

❌ **Don't:** Make API calls in components directly
✅ **Do:** Use Redux Toolkit Query or React Query

❌ **Don't:** Forget to handle loading and error states
✅ **Do:** Provide feedback for every user action

### DevOps
❌ **Don't:** Use the same secrets in dev and production
✅ **Do:** Maintain separate environments with different credentials

❌ **Don't:** Deploy without testing
✅ **Do:** Have staging environment and automated tests

---

## Additional Resources

### Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Redux Toolkit](https://redux-toolkit.js.org/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)

### Learning
- [Full Stack Open](https://fullstackopen.com/)
- [Django for APIs](https://djangoforapis.com/)
- [RAG Tutorial](https://www.pinecone.io/learn/retrieval-augmented-generation/)

---

## Project Showcase

When applying to Full Scale, showcase this project by:

1. **GitHub README:**
   - Project overview with screenshots
   - Technology stack
   - Setup instructions
   - Live demo link

2. **Live Demo:**
   - Deploy on Heroku/Render/Railway
   - Seed with sample documents
   - Create demo video (Loom)

3. **Portfolio Highlights:**
   - RAG implementation (core requirement)
   - Full-stack capabilities
   - Production-ready code
   - CI/CD pipeline
   - Clean architecture

4. **During Interview:**
   - Explain architectural decisions
   - Discuss scaling strategies
   - Share challenges overcome
   - Demonstrate live Q&A functionality

---

## Congratulations! 🎉

You've built a production-grade RAG-powered application that demonstrates:
- ✅ Python (Django/DRF) expertise
- ✅ React proficiency
- ✅ AI/ML integration (LLMs, RAG)
- ✅ Database management (PostgreSQL, vector search)
- ✅ DevOps skills (Docker, CI/CD)
- ✅ Professional development practices

This project showcases exactly what Full Scale is looking for. You're ready to apply!

---

**Your Senior Software Engineer Mentor,
Claude**

*"The only way to learn a new programming language is by writing programs in it."* - Dennis Ritchie

Ready to start? Let's begin with **MILESTONE 1**! 🚀
