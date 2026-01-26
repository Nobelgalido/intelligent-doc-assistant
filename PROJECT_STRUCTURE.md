# Project Structure

Complete directory structure for the Intelligent Document Q&A Platform.

```
intelligent-doc-assistant/
│
├── 📁 backend/                          # Django backend application
│   ├── 📁 config/                       # Django project configuration
│   │   ├── __init__.py
│   │   ├── settings.py                  # Main settings file
│   │   ├── urls.py                      # Root URL configuration
│   │   ├── wsgi.py                      # WSGI configuration
│   │   ├── asgi.py                      # ASGI configuration
│   │   └── celery.py                    # Celery configuration
│   │
│   ├── 📁 apps/                         # Django applications
│   │   │
│   │   ├── 📁 users/                    # User management app
│   │   │   ├── __init__.py
│   │   │   ├── models.py                # Custom User model
│   │   │   ├── serializers.py           # User serializers
│   │   │   ├── views.py                 # Auth views
│   │   │   ├── urls.py                  # User URLs
│   │   │   ├── admin.py                 # Admin configuration
│   │   │   ├── tests/                   # User tests
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_views.py
│   │   │   │   └── test_serializers.py
│   │   │   └── migrations/              # Database migrations
│   │   │
│   │   ├── 📁 documents/                # Document management app
│   │   │   ├── __init__.py
│   │   │   ├── models.py                # Document, DocumentChunk, Collection models
│   │   │   ├── serializers.py           # Document serializers
│   │   │   ├── views.py                 # Document CRUD views
│   │   │   ├── urls.py                  # Document URLs
│   │   │   ├── admin.py                 # Admin configuration
│   │   │   ├── tasks.py                 # Celery tasks for processing
│   │   │   ├── utils.py                 # Document processing utilities
│   │   │   ├── tests/                   # Document tests
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_views.py
│   │   │   │   ├── test_tasks.py
│   │   │   │   └── test_utils.py
│   │   │   └── migrations/              # Database migrations
│   │   │
│   │   ├── 📁 qa/                       # Q&A functionality app
│   │   │   ├── __init__.py
│   │   │   ├── models.py                # Conversation, Question models
│   │   │   ├── serializers.py           # Q&A serializers
│   │   │   ├── views.py                 # Q&A views
│   │   │   ├── urls.py                  # Q&A URLs
│   │   │   ├── admin.py                 # Admin configuration
│   │   │   ├── 📁 services/             # Business logic
│   │   │   │   ├── __init__.py
│   │   │   │   ├── rag_service.py       # RAG implementation
│   │   │   │   └── embedding_service.py # Embedding generation
│   │   │   ├── tests/                   # Q&A tests
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_views.py
│   │   │   │   └── test_rag_service.py
│   │   │   └── migrations/              # Database migrations
│   │   │
│   │   └── 📁 core/                     # Shared utilities
│   │       ├── __init__.py
│   │       ├── permissions.py           # Custom permissions
│   │       ├── pagination.py            # Custom pagination
│   │       ├── exceptions.py            # Custom exceptions
│   │       └── utils.py                 # Shared utilities
│   │
│   ├── 📁 requirements/                 # Python dependencies
│   │   ├── base.txt                     # Common dependencies
│   │   ├── development.txt              # Dev dependencies (extends base)
│   │   └── production.txt               # Production dependencies (extends base)
│   │
│   ├── 📁 media/                        # Uploaded files (not in git)
│   │   └── documents/
│   │
│   ├── 📁 staticfiles/                  # Collected static files (not in git)
│   │
│   ├── 📁 tests/                        # Integration tests
│   │   ├── __init__.py
│   │   ├── conftest.py                  # Pytest configuration
│   │   └── test_integration.py
│   │
│   ├── manage.py                        # Django management script
│   ├── .env.example                     # Environment variables template
│   ├── .env                             # Actual environment (not in git)
│   ├── pytest.ini                       # Pytest configuration
│   ├── .coveragerc                      # Coverage configuration
│   └── Dockerfile                       # Docker image for backend
│
├── 📁 frontend/                         # React frontend application
│   ├── 📁 public/                       # Static assets
│   │   ├── favicon.ico
│   │   └── index.html
│   │
│   ├── 📁 src/                          # Source code
│   │   │
│   │   ├── 📁 app/                      # Redux store
│   │   │   ├── store.ts                 # Store configuration
│   │   │   └── hooks.ts                 # Typed Redux hooks
│   │   │
│   │   ├── 📁 features/                 # Feature modules
│   │   │   │
│   │   │   ├── 📁 auth/                 # Authentication
│   │   │   │   ├── authSlice.ts         # Auth state management
│   │   │   │   ├── authAPI.ts           # Auth API calls
│   │   │   │   ├── Login.tsx            # Login page
│   │   │   │   ├── Register.tsx         # Registration page
│   │   │   │   ├── Login.test.tsx       # Login tests
│   │   │   │   └── Register.test.tsx    # Register tests
│   │   │   │
│   │   │   ├── 📁 documents/            # Document management
│   │   │   │   ├── documentsSlice.ts    # Documents state
│   │   │   │   ├── documentsAPI.ts      # Documents API calls
│   │   │   │   ├── DocumentList.tsx     # Document list view
│   │   │   │   ├── DocumentUpload.tsx   # Upload component
│   │   │   │   ├── DocumentViewer.tsx   # Document viewer
│   │   │   │   └── DocumentCard.tsx     # Document card component
│   │   │   │
│   │   │   └── 📁 qa/                   # Q&A functionality
│   │   │       ├── qaSlice.ts           # Q&A state management
│   │   │       ├── qaAPI.ts             # Q&A API calls
│   │   │       ├── ChatInterface.tsx    # Main chat UI
│   │   │       ├── ConversationList.tsx # Conversation list
│   │   │       ├── MessageBubble.tsx    # Message component
│   │   │       └── SourceCard.tsx       # Source citation component
│   │   │
│   │   ├── 📁 components/               # Reusable components
│   │   │   ├── 📁 common/               # Common components
│   │   │   │   ├── Layout.tsx           # App layout
│   │   │   │   ├── Navbar.tsx           # Navigation bar
│   │   │   │   ├── Sidebar.tsx          # Sidebar navigation
│   │   │   │   ├── Loading.tsx          # Loading spinner
│   │   │   │   ├── ErrorBoundary.tsx    # Error boundary
│   │   │   │   └── ConfirmDialog.tsx    # Confirmation dialog
│   │   │   ├── ProtectedRoute.tsx       # Auth route guard
│   │   │   └── FileUploadZone.tsx       # Drag-drop upload
│   │   │
│   │   ├── 📁 pages/                    # Page components
│   │   │   ├── Dashboard.tsx            # Main dashboard
│   │   │   ├── Documents.tsx            # Documents page
│   │   │   ├── Chat.tsx                 # Chat page
│   │   │   ├── Profile.tsx              # User profile
│   │   │   └── NotFound.tsx             # 404 page
│   │   │
│   │   ├── 📁 services/                 # API services
│   │   │   ├── api.ts                   # Axios instance
│   │   │   ├── authService.ts           # Auth service
│   │   │   ├── documentService.ts       # Document service
│   │   │   └── qaService.ts             # Q&A service
│   │   │
│   │   ├── 📁 types/                    # TypeScript types
│   │   │   ├── auth.types.ts            # Auth types
│   │   │   ├── document.types.ts        # Document types
│   │   │   ├── qa.types.ts              # Q&A types
│   │   │   └── common.types.ts          # Common types
│   │   │
│   │   ├── 📁 utils/                    # Utility functions
│   │   │   ├── constants.ts             # App constants
│   │   │   ├── helpers.ts               # Helper functions
│   │   │   ├── validators.ts            # Validation functions
│   │   │   └── formatters.ts            # Data formatters
│   │   │
│   │   ├── 📁 hooks/                    # Custom React hooks
│   │   │   ├── useAuth.ts               # Auth hook
│   │   │   ├── useDocuments.ts          # Documents hook
│   │   │   └── useDebounce.ts           # Debounce hook
│   │   │
│   │   ├── 📁 styles/                   # Global styles
│   │   │   ├── theme.ts                 # MUI theme
│   │   │   └── global.css               # Global CSS
│   │   │
│   │   ├── App.tsx                      # Root component
│   │   ├── main.tsx                     # Entry point
│   │   ├── vite-env.d.ts                # Vite types
│   │   └── setupTests.ts                # Test setup
│   │
│   ├── .env.example                     # Environment template
│   ├── .env                             # Actual environment (not in git)
│   ├── package.json                     # Node dependencies
│   ├── package-lock.json                # Locked dependencies
│   ├── tsconfig.json                    # TypeScript config
│   ├── vite.config.ts                   # Vite configuration
│   ├── .eslintrc.cjs                    # ESLint config
│   ├── .prettierrc                      # Prettier config
│   ├── jest.config.js                   # Jest config
│   ├── nginx.conf                       # Nginx config for Docker
│   └── Dockerfile                       # Docker image for frontend
│
├── 📁 .github/                          # GitHub configuration
│   └── 📁 workflows/                    # GitHub Actions
│       ├── ci.yml                       # CI/CD pipeline
│       ├── backend-tests.yml            # Backend tests
│       └── frontend-tests.yml           # Frontend tests
│
├── 📁 docker/                           # Docker configurations
│   ├── backend/
│   │   ├── Dockerfile                   # Production Dockerfile
│   │   └── entrypoint.sh                # Entrypoint script
│   ├── frontend/
│   │   ├── Dockerfile                   # Production Dockerfile
│   │   └── nginx.conf                   # Nginx config
│   └── postgres/
│       └── init.sql                     # Database initialization
│
├── 📁 docs/                             # Documentation
│   ├── API.md                           # API documentation
│   ├── ARCHITECTURE.md                  # Architecture overview
│   ├── DEPLOYMENT.md                    # Deployment guide
│   └── CONTRIBUTING.md                  # Contributing guidelines
│
├── 📁 scripts/                          # Utility scripts
│   ├── setup.sh                         # Initial setup script
│   ├── run_tests.sh                     # Run all tests
│   ├── deploy.sh                        # Deployment script
│   └── backup_db.sh                     # Database backup
│
├── .gitignore                           # Git ignore rules
├── .env.example                         # Root environment template
├── docker-compose.yml                   # Docker Compose config
├── docker-compose.dev.yml               # Development override
├── docker-compose.prod.yml              # Production override
├── .pre-commit-config.yaml              # Pre-commit hooks
├── README.md                            # Project README
├── Claude.md                            # This tutorial guide
├── PROJECT_STRUCTURE.md                 # This file
├── LICENSE                              # MIT License
└── CHANGELOG.md                         # Version history
```

## File Count Summary

- **Total Files**: ~150+ files
- **Python Files**: ~50 files
- **TypeScript/React Files**: ~60 files
- **Configuration Files**: ~20 files
- **Documentation**: ~10 files

## Key Directories Explained

### Backend (`/backend`)
- **config/**: Django project settings and configuration
- **apps/**: Modular Django applications (users, documents, qa, core)
- **requirements/**: Separated dependencies for different environments
- **media/**: User-uploaded files (excluded from git)
- **tests/**: Integration and end-to-end tests

### Frontend (`/frontend`)
- **src/features/**: Feature-based architecture (auth, documents, qa)
- **src/components/**: Reusable UI components
- **src/services/**: API communication layer
- **src/types/**: TypeScript type definitions
- **src/utils/**: Helper functions and utilities

### DevOps
- **.github/workflows/**: CI/CD automation
- **docker/**: Docker configurations per service
- **scripts/**: Development and deployment automation

## Important Files

### Configuration
- `backend/config/settings.py` - Django settings
- `frontend/vite.config.ts` - Vite build configuration
- `docker-compose.yml` - Multi-container orchestration
- `.env.example` - Environment variable template

### Entry Points
- `backend/manage.py` - Django CLI
- `backend/config/wsgi.py` - Production server entry
- `frontend/src/main.tsx` - React app entry
- `backend/config/celery.py` - Celery worker entry

### Key Business Logic
- `backend/apps/qa/services/rag_service.py` - RAG implementation
- `backend/apps/documents/tasks.py` - Document processing
- `frontend/src/features/qa/ChatInterface.tsx` - Chat UI
- `frontend/src/app/store.ts` - Redux store

## File Naming Conventions

### Backend (Python)
- `models.py` - Django models
- `views.py` - API views/endpoints
- `serializers.py` - DRF serializers
- `tasks.py` - Celery tasks
- `tests/test_*.py` - Test files

### Frontend (TypeScript)
- `*.tsx` - React components
- `*.ts` - TypeScript modules
- `*.types.ts` - Type definitions
- `*Slice.ts` - Redux slices
- `*API.ts` - API service files
- `*.test.tsx` - Component tests

## Git Ignore Patterns

The following are excluded from version control:
- `*.pyc`, `__pycache__/` - Python bytecode
- `.env`, `.env.local` - Environment files
- `node_modules/` - Node dependencies
- `media/`, `staticfiles/` - Generated files
- `dist/`, `build/` - Build outputs
- `.coverage`, `htmlcov/` - Test coverage
- `*.log` - Log files

## Development Workflow

1. **Backend Development**: Edit files in `backend/apps/`
2. **Frontend Development**: Edit files in `frontend/src/`
3. **Testing**: Run tests from respective directories
4. **Documentation**: Update files in `docs/`
5. **Deployment**: Use scripts in `scripts/` or GitHub Actions

---

This structure follows industry best practices for:
- Separation of concerns
- Modularity and scalability
- Testability
- Documentation
- DevOps integration
