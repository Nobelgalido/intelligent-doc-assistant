# Intelligent Document Q&A Platform

> A production-grade RAG (Retrieval-Augmented Generation) powered document intelligence system built with Django, React, and Google Gemini AI (FREE!).

[![CI/CD](https://github.com/yourusername/intelligent-doc-assistant/workflows/CI/badge.svg)](https://github.com/yourusername/intelligent-doc-assistant/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18-blue.svg)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

An intelligent document assistant that allows users to upload documents (PDF, DOCX, TXT) and ask questions about their content using advanced RAG (Retrieval-Augmented Generation) technology powered by Google Gemini AI (100% FREE with no credit card required!).

### ✨ Key Features

- **📄 Multi-format Document Support**: Upload and process PDF, DOCX, TXT, and Markdown files
- **🤖 AI-Powered Q&A**: Ask natural language questions and get accurate answers with source citations
- **🔍 Vector Search**: Efficient semantic search using pgvector and FAISS
- **💬 Conversation History**: Maintain context across multiple questions
- **📊 Source Attribution**: Every answer includes references to source documents
- **🔐 Secure Authentication**: JWT-based authentication with refresh tokens
- **⚡ Real-time Processing**: Background document processing with Celery
- **📱 Responsive UI**: Modern, intuitive interface built with Material-UI

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.0 + Django REST Framework
- **Language**: Python 3.11+
- **Database**: PostgreSQL 15 + pgvector extension
- **AI/ML**:
  - **Google Gemini 1.5 Flash** (Language Model) - **FREE!** 🎉
  - Alternative: OpenAI GPT-4 (requires paid API)
  - FAISS (Vector similarity search)
  - Gemini text-embedding-004 (768-dim embeddings)
- **Task Queue**: Celery + Redis
- **Storage**: MinIO / AWS S3

### Frontend
- **Framework**: React 18 + TypeScript
- **State Management**: Redux Toolkit
- **UI Library**: Material-UI (MUI) v5
- **Build Tool**: Vite
- **HTTP Client**: Axios
- **Testing**: Jest + React Testing Library

### DevOps
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Code Quality**: Black, Flake8, ESLint, Prettier
- **Documentation**: Swagger/OpenAPI

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Redis
- Docker & Docker Compose (optional)

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/yourusername/intelligent-doc-assistant.git
cd intelligent-doc-assistant

# Create environment file
cp .env.example .env
# Edit .env with your configuration (especially GOOGLE_API_KEY - it's FREE!)

# Start all services
docker-compose up -d

# Run migrations
docker-compose exec backend python manage.py migrate

# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Application will be available at:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# Admin Panel: http://localhost:8000/admin
```

### Option 2: Local Development

#### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements/development.txt

# Create .env file
cp .env.example .env
# Edit .env with your configuration

# Setup database
createdb intelligent_doc_db
psql intelligent_doc_db -c "CREATE EXTENSION vector;"

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

#### Celery Worker (separate terminal)

```bash
cd backend
source venv/bin/activate
celery -A config worker -l info
```

#### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Start development server
npm run dev
```

## 📋 Usage

### 1. Upload Documents

- Log in to the application
- Navigate to "Documents" section
- Upload PDF, DOCX, or TXT files
- Wait for processing to complete (background task)

### 2. Ask Questions

- Go to "Chat" section
- Type your question about the uploaded documents
- Receive AI-generated answers with source citations
- Continue the conversation for follow-up questions

### 3. View Sources

- Click on source chips to expand and view relevant document excerpts
- See confidence scores and processing times
- Provide feedback on answer quality

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Client (React)                         │
└───────────────────────────┬─────────────────────────────────┘
                            │ REST API
┌───────────────────────────▼─────────────────────────────────┐
│                   Django REST Framework                     │
└───────────────────────────┬─────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼──────┐  ┌────────▼────────┐  ┌──────▼──────┐
│  PostgreSQL  │  │   RAG Engine    │  │    Redis    │
│  + pgvector  │  │  (LangChain +   │  │ (Cache/Queue)│
│              │  │    OpenAI)      │  │             │
└──────────────┘  └────────┬────────┘  └─────────────┘
                           │
                  ┌────────▼────────┐
                  │  Vector Store   │
                  │     (FAISS)     │
                  └─────────────────┘
```

### RAG Pipeline

```
User Question
    ↓
Document Retrieval (Vector Search)
    ↓
Context Extraction (Top-K Chunks)
    ↓
Prompt Engineering (System + Context + Question)
    ↓
Gemini AI Generation (FREE!)
    ↓
Response with Sources
```

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest --cov=. --cov-report=html
```

### Frontend Tests

```bash
cd frontend
npm run test
npm run test:coverage
```

### Run All Tests

```bash
# With Docker
docker-compose run backend pytest
docker-compose run frontend npm test

# Local
./scripts/run_all_tests.sh
```

## 📊 API Documentation

API documentation is available via Swagger UI:

```
http://localhost:8000/api/docs/
```

### Key Endpoints

#### Authentication
- `POST /api/v1/auth/register/` - User registration
- `POST /api/v1/auth/token/` - Login (get JWT tokens)
- `POST /api/v1/auth/token/refresh/` - Refresh access token

#### Documents
- `GET /api/v1/documents/documents/` - List documents
- `POST /api/v1/documents/documents/` - Upload document
- `GET /api/v1/documents/documents/{id}/` - Get document details
- `DELETE /api/v1/documents/documents/{id}/` - Delete document

#### Q&A
- `POST /api/v1/qa/conversations/ask/` - Ask a question
- `GET /api/v1/qa/conversations/` - List conversations
- `GET /api/v1/qa/conversations/{id}/questions/` - Get conversation history

## 🔧 Configuration

### Environment Variables

#### Backend (.env)

```env
# Django
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,yourdomain.com

# Database
DATABASE_NAME=intelligent_doc_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/0

# AI Provider (FREE!)
AI_PROVIDER=gemini
GOOGLE_API_KEY=your-google-gemini-api-key

# Optional: OpenAI (paid)
# OPENAI_API_KEY=sk-your-api-key

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```

#### Frontend (.env)

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in Django settings
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Use strong `SECRET_KEY`
- [ ] Set up HTTPS (SSL certificate)
- [ ] Configure production database (managed PostgreSQL)
- [ ] Set up S3/DigitalOcean Spaces for file storage
- [ ] Configure CDN for static files
- [ ] Set up monitoring (Sentry, DataDog)
- [ ] Enable automated backups
- [ ] Configure rate limiting
- [ ] Set up log aggregation
- [ ] Implement caching strategy

### Deployment Platforms

- **Backend**: Heroku, Railway, Render, AWS ECS, DigitalOcean App Platform
- **Frontend**: Vercel, Netlify, AWS S3 + CloudFront
- **Database**: AWS RDS, DigitalOcean Managed Databases, Supabase

## 📈 Performance Optimization

- **Database**: Indexed queries, connection pooling, read replicas
- **Caching**: Redis for API responses and session data
- **Background Jobs**: Celery for document processing
- **Frontend**: Code splitting, lazy loading, CDN
- **API**: Pagination, field filtering, compression

## 🔒 Security

- JWT authentication with refresh tokens
- CORS configuration
- CSRF protection
- SQL injection prevention (Django ORM)
- XSS protection (React escaping)
- Rate limiting
- Input validation
- File upload restrictions
- Environment variable management

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure:
- Code passes all tests
- Linting passes (Black, Flake8, ESLint)
- Add tests for new features
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**

- GitHub: [@Nobelgalido](https://github.com/yourusername)
- LinkedIn: [Alfred Nobel Galido](https://linkedin.com/in/yourprofile)
- Portfolio: [yourportfolio.com](https://yourportfolio.com)

## 🙏 Acknowledgments

- Google for Gemini AI and generous free tier
- Alternative: OpenAI GPT-4 API
- Django and React communities
- Full Scale for the opportunity

## 📞 Support

For questions or support:
- Create an issue on GitHub
- Email: your.email@example.com

---

**Built with ❤️ as a portfolio project for Full Scale**

*Demonstrating full-stack development with Django, React, AI/ML integration, and production-grade DevOps practices.*
