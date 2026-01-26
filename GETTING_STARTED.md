# Getting Started - Quick Reference

> Your quick reference guide to start building the Intelligent Document Q&A Platform

## 📋 Prerequisites Checklist

Before you begin, make sure you have:

- [ ] Python 3.11 or higher installed
- [ ] Node.js 18 or higher installed
- [ ] PostgreSQL 15 or higher installed
- [ ] Redis installed
- [ ] Git installed
- [ ] A code editor (VS Code recommended)
- [ ] Google account for Gemini API key (FREE!)
- [ ] GitHub account

## 🚀 Quick Start (30 minutes)

### Step 1: Verify Installations (5 min)

```bash
# Check Python version
python --version  # Should be 3.11+

# Check Node.js version
node --version  # Should be 18+

# Check PostgreSQL
psql --version  # Should be 15+

# Check Redis
redis-cli --version

# Check Git
git --version
```

**📚 Need help installing PostgreSQL or Redis?**
👉 **See detailed step-by-step instructions**: [INSTALLATION_GUIDE.md](./INSTALLATION_GUIDE.md)

### Step 2: Get Google Gemini API Key - FREE! (5 min)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key" or "Create API Key"
4. Copy your API key
5. **IMPORTANT**: Save this key securely - you'll need it in `.env` file
6. **NOTE**: No credit card required! Totally FREE with generous limits (1,500 requests/day)

### Step 3: Initial Setup (5 min)

```bash
# Create project directory
mkdir intelligent-doc-assistant
cd intelligent-doc-assistant

# Initialize git repository
git init

# Create basic structure
mkdir backend frontend docs scripts

# Copy the Claude.md tutorial (already provided)
# Read through MILESTONE 1 in Claude.md
```

### Step 4: Setup PostgreSQL Database (5 min)

```bash
# Option 1: Using psql command line
createdb intelligent_doc_db

# Connect to database
psql intelligent_doc_db

# Enable pgvector extension
CREATE EXTENSION vector;

# Exit psql
\q

# Option 2: Using PostgreSQL GUI (pgAdmin, DBeaver, etc.)
# - Create database: intelligent_doc_db
# - Run SQL: CREATE EXTENSION vector;
```

### Step 5: Backend Setup (5 min)

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Create initial requirements file
cat > requirements.txt << EOL
Django==5.0.0
djangorestframework==3.14.0
django-cors-headers==4.3.0
psycopg2-binary==2.9.9
python-decouple==3.8
EOL

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your database credentials and Gemini API key
```

### Step 6: Frontend Setup (5 min)

```bash
cd ../frontend

# Initialize React project with Vite
npm create vite@latest . -- --template react-ts

# Install dependencies
npm install

# Create .env file
echo "VITE_API_BASE_URL=http://localhost:8000/api/v1" > .env
```

## 📚 Following the Tutorial

Open [Claude.md](./Claude.md) and follow along milestone by milestone:

### Recommended Learning Path

**Week 1: Backend Foundation**
- ✅ Milestone 1: Project Setup & Django Foundation
- ✅ Milestone 2: Database Models & Authentication
- ✅ Milestone 3: Document Upload & Processing

**Week 2: AI Integration**
- ✅ Milestone 4: RAG Implementation

**Week 3: Frontend Development**
- ✅ Milestone 5: React Frontend Foundation
- ✅ Milestone 6: Frontend-Backend Integration

**Week 4: Production Ready**
- ✅ Milestone 7: Docker Containerization
- ✅ Milestone 8: CI/CD Pipeline
- ✅ Milestone 9: Testing & Quality Assurance
- ✅ Milestone 10: Production Deployment

## 🎯 After Each Milestone

After completing each milestone:

1. **Test your code**
   ```bash
   # Backend
   python manage.py runserver

   # Frontend
   npm run dev
   ```

2. **Commit to Git**
   ```bash
   git add .
   git commit -m "Milestone X: Brief description"
   ```

3. **Push to GitHub**
   ```bash
   git push origin main
   ```

4. **Update your learning log**
   - What did you learn?
   - What challenges did you face?
   - What would you do differently?

## 🆘 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution**: Make sure your virtual environment is activated
```bash
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### Issue: "psycopg2 installation error"
**Solution**: Use psycopg2-binary instead
```bash
pip install psycopg2-binary
```

### Issue: "Port 8000 already in use"
**Solution**: Kill the process or use a different port
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

### Issue: "pgvector extension not found"
**Solution**: Install pgvector extension for PostgreSQL
```bash
# Mac (Homebrew)
brew install pgvector

# Ubuntu/Debian
sudo apt install postgresql-15-pgvector

# Then connect to your database and run:
CREATE EXTENSION vector;
```

### Issue: "Google Gemini API key not working"
**Solution**:
1. Verify your API key is correct
2. Make sure you're using Google AI Studio (not Google Cloud Console)
3. Check that the API key is enabled
4. Ensure `.env` file is properly formatted: `GOOGLE_API_KEY=your-key-here` (no spaces around `=`)
5. Verify you haven't exceeded the free tier rate limits (15 requests/minute)

## 📝 Daily Development Workflow

### Starting Your Dev Environment

```bash
# Terminal 1: Start PostgreSQL (if not running as service)
# Usually runs automatically on Windows/Mac

# Terminal 2: Start Redis
redis-server

# Terminal 3: Backend
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python manage.py runserver

# Terminal 4: Celery Worker
cd backend
source venv/bin/activate
celery -A config worker -l info

# Terminal 5: Frontend
cd frontend
npm run dev
```

### Stopping Your Dev Environment

```bash
# Press Ctrl+C in each terminal
# Or close all terminals
```

## 🧪 Testing Your Setup

### Backend Health Check
```bash
# Visit in browser or curl
curl http://localhost:8000/admin/

# Should show Django admin login page
```

### Frontend Health Check
```bash
# Visit in browser
http://localhost:3000

# Should show React app
```

### Database Health Check
```bash
psql intelligent_doc_db

# Run query
SELECT * FROM pg_extension WHERE extname = 'vector';

# Should show vector extension installed
```

### Redis Health Check
```bash
redis-cli ping

# Should respond with "PONG"
```

## 📖 Learning Resources

### Documentation
- [Django Docs](https://docs.djangoproject.com/en/5.0/)
- [DRF Docs](https://www.django-rest-framework.org/)
- [React Docs](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [LangChain Docs](https://python.langchain.com/)

### Tutorials (if you get stuck)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [React Tutorial](https://react.dev/learn)
- [Full Stack Open](https://fullstackopen.com/)

### Community Help
- [Django Discord](https://discord.gg/xcRH6mN4fa)
- [React Discord](https://discord.gg/react)
- [Stack Overflow](https://stackoverflow.com/)

## 💡 Tips for Success

1. **Read Claude.md thoroughly** before starting each milestone
2. **Don't skip steps** - each builds on the previous
3. **Test frequently** - after every significant change
4. **Commit often** - small, meaningful commits
5. **Ask for help** - use the community resources above
6. **Take breaks** - this is a marathon, not a sprint
7. **Document your learning** - keep notes of what you learn
8. **Experiment** - try variations once you understand the basics

## 🎓 Next Steps

Once you've completed the quick start:

1. Open [Claude.md](./Claude.md)
2. Read through Milestone 1 completely
3. Start implementing step by step
4. Commit and push after completing Milestone 1
5. Move to Milestone 2

## 📞 Getting Help

If you're stuck:

1. **Check the Common Issues section above**
2. **Review the relevant Milestone in Claude.md**
3. **Check the official documentation**
4. **Search Stack Overflow**
5. **Ask in community forums/Discord**
6. **Review your error messages carefully** - they usually tell you what's wrong

## ✅ Pre-Flight Checklist

Before starting Milestone 1, verify:

- [ ] Python 3.11+ installed and working
- [ ] Node.js 18+ installed and working
- [ ] PostgreSQL 15+ installed and running
- [ ] Redis installed and can start
- [ ] Git initialized in project directory
- [ ] GitHub repository created
- [ ] Google Gemini API key obtained (FREE!)
- [ ] Code editor ready
- [ ] Terminal windows ready (4-5 recommended)
- [ ] Claude.md open and ready to follow
- [ ] Excitement level: Maximum! 🚀

---

**You're ready to start! Head to Claude.md and begin with MILESTONE 1.**

Good luck on your journey to building a production-grade AI application! 💪

---

**Pro Tip**: Keep this file open in a browser tab for quick reference while following the tutorial in Claude.md.
