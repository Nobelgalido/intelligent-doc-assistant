# Installation Guide - Redis & PostgreSQL

> Complete guide to installing Redis and PostgreSQL on Windows, Mac, and Linux

---

## 🪟 Windows Installation

### PostgreSQL Installation (with psql)

#### Option 1: Official Installer (Recommended)

1. **Download PostgreSQL Installer**
   - Go to [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)
   - Click "Download the installer" link
   - Download PostgreSQL 15 or 16 (latest stable)

2. **Run the Installer**
   - Double-click the downloaded `.exe` file
   - Click "Next" through the setup wizard
   - **Important**: Remember the password you set for the `postgres` user!
   - Default port: `5432` (keep this)
   - Install Stack Builder components: Select `pgvector` if available

3. **Verify Installation**
   ```bash
   # Open Command Prompt or PowerShell
   psql --version
   # Should output: psql (PostgreSQL) 15.x or 16.x
   ```

4. **Add to PATH (if not automatic)**
   - Right-click "This PC" → Properties → Advanced System Settings
   - Click "Environment Variables"
   - Under "System Variables", find `Path` and click "Edit"
   - Click "New" and add: `C:\Program Files\PostgreSQL\15\bin`
   - Click OK on all dialogs
   - **Restart your terminal**

5. **Test Connection**
   ```bash
   # Connect to PostgreSQL
   psql -U postgres
   # Enter the password you set during installation

   # You should see:
   # postgres=#

   # Type \q to quit
   ```

#### Option 2: Using Chocolatey

```bash
# Install Chocolatey first (if not installed)
# Run PowerShell as Administrator and run:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install PostgreSQL
choco install postgresql15 -y

# Verify
psql --version
```

### Redis Installation

#### Option 1: Using Memurai (Windows-native Redis)

1. **Download Memurai**
   - Go to [https://www.memurai.com/get-memurai](https://www.memurai.com/get-memurai)
   - Download Memurai Developer Edition (Free)
   - Run the installer

2. **Verify Installation**
   ```bash
   # Check if Memurai is running
   memurai-cli ping
   # Should output: PONG
   ```

#### Option 2: Windows Subsystem for Linux (WSL) - Recommended for Full Redis

1. **Install WSL**
   ```bash
   # Run PowerShell as Administrator
   wsl --install
   # Restart your computer
   ```

2. **Install Redis in WSL**
   ```bash
   # Open WSL (Ubuntu)
   wsl

   # Update packages
   sudo apt update

   # Install Redis
   sudo apt install redis-server -y

   # Start Redis
   sudo service redis-server start

   # Test
   redis-cli ping
   # Should output: PONG
   ```

3. **Make Redis start automatically**
   ```bash
   # In WSL
   echo "sudo service redis-server start" >> ~/.bashrc
   ```

#### Option 3: Using Chocolatey

```bash
# Run PowerShell as Administrator
choco install redis-64 -y

# Start Redis
redis-server

# Test in new terminal
redis-cli ping
```

#### Option 4: Docker (Easiest for Development)

```bash
# Install Docker Desktop for Windows first
# Then run:
docker run -d -p 6379:6379 --name redis redis:alpine

# Test
docker exec -it redis redis-cli ping
# Should output: PONG
```

---

## 🍎 macOS Installation

### PostgreSQL Installation

#### Option 1: Using Homebrew (Recommended)

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install PostgreSQL
brew install postgresql@15

# Start PostgreSQL service
brew services start postgresql@15

# Create default database
createdb $(whoami)

# Verify
psql --version
psql -d postgres
```

#### Option 2: Using Postgres.app

1. Download from [https://postgresapp.com/](https://postgresapp.com/)
2. Drag to Applications folder
3. Open Postgres.app
4. Click "Initialize" to create a new server
5. Add to PATH:
   ```bash
   echo 'export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Redis Installation

```bash
# Using Homebrew
brew install redis

# Start Redis service
brew services start redis

# Verify
redis-cli ping
# Should output: PONG
```

---

## 🐧 Linux Installation

### Ubuntu/Debian

#### PostgreSQL

```bash
# Update package list
sudo apt update

# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Switch to postgres user and create your user
sudo -u postgres createuser --interactive --pwprompt
# Enter your username and password

# Create database
sudo -u postgres createdb your_username

# Verify
psql --version
```

#### Install pgvector Extension

```bash
# Install development tools
sudo apt install postgresql-server-dev-15 git build-essential -y

# Clone and install pgvector
cd /tmp
git clone --branch v0.5.1 https://github.com/pgvector/pgvector.git
cd pgvector
make
sudo make install

# Test in psql
psql -U postgres
CREATE EXTENSION vector;
\dx  # Should show vector extension
```

#### Redis

```bash
# Install Redis
sudo apt update
sudo apt install redis-server -y

# Start Redis service
sudo systemctl start redis-server
sudo systemctl enable redis-server

# Verify
redis-cli ping
# Should output: PONG
```

### CentOS/RHEL/Fedora

#### PostgreSQL

```bash
# Install PostgreSQL
sudo dnf install postgresql-server postgresql-contrib -y

# Initialize database
sudo postgresql-setup --initdb

# Start service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Verify
psql --version
```

#### Redis

```bash
# Install Redis
sudo dnf install redis -y

# Start service
sudo systemctl start redis
sudo systemctl enable redis

# Verify
redis-cli ping
```

---

## 🔧 Post-Installation Configuration

### PostgreSQL Setup

1. **Create Project Database**
   ```bash
   # Connect as postgres user
   psql -U postgres

   # Create database
   CREATE DATABASE intelligent_doc_db;

   # Create user
   CREATE USER doc_user WITH PASSWORD 'your_password';

   # Grant privileges
   GRANT ALL PRIVILEGES ON DATABASE intelligent_doc_db TO doc_user;

   # Enable vector extension
   \c intelligent_doc_db
   CREATE EXTENSION vector;

   # Verify
   \dx

   # Exit
   \q
   ```

2. **Update your `.env` file**
   ```env
   DATABASE_NAME=intelligent_doc_db
   DATABASE_USER=doc_user
   DATABASE_PASSWORD=your_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

### Redis Configuration

Redis works out-of-the-box for development. Just verify it's running:

```bash
# Test Redis
redis-cli ping
# Should output: PONG

# Check if it's accepting connections
redis-cli
127.0.0.1:6379> SET test "Hello"
127.0.0.1:6379> GET test
# Should output: "Hello"
127.0.0.1:6379> exit
```

---

## ✅ Verification Checklist

Run these commands to verify everything is installed:

```bash
# Python
python --version  # Should be 3.11+

# Node.js
node --version    # Should be 18+
npm --version

# PostgreSQL
psql --version    # Should be 15+

# Redis
redis-cli --version

# Git
git --version

# Test PostgreSQL connection
psql -U postgres -c "SELECT version();"

# Test Redis connection
redis-cli ping    # Should output: PONG
```

---

## 🐛 Common Issues & Solutions

### PostgreSQL Issues

#### Issue: "psql: command not found"
**Solution**: Add PostgreSQL to your PATH

**Windows**:
```bash
# Add to PATH:
C:\Program Files\PostgreSQL\15\bin
```

**Mac** (if using Postgres.app):
```bash
echo 'export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Linux**:
```bash
# Usually automatic, but if needed:
echo 'export PATH=/usr/lib/postgresql/15/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

#### Issue: "peer authentication failed"
**Solution**: Edit `pg_hba.conf`

```bash
# Find the file
# Windows: C:\Program Files\PostgreSQL\15\data\pg_hba.conf
# Mac: /usr/local/var/postgresql@15/pg_hba.conf
# Linux: /etc/postgresql/15/main/pg_hba.conf

# Change this line:
# local   all   postgres   peer
# To:
# local   all   postgres   md5

# Restart PostgreSQL
# Windows: Services → PostgreSQL → Restart
# Mac: brew services restart postgresql@15
# Linux: sudo systemctl restart postgresql
```

#### Issue: "could not connect to server"
**Solution**: Start PostgreSQL service

**Windows**:
```bash
# Open Services (Win + R, type: services.msc)
# Find "postgresql-x64-15" and click "Start"
```

**Mac**:
```bash
brew services start postgresql@15
```

**Linux**:
```bash
sudo systemctl start postgresql
```

### Redis Issues

#### Issue: "Could not connect to Redis"
**Solution**: Start Redis service

**Windows (Memurai)**:
```bash
# Check Windows Services for Memurai
# Or start manually:
memurai-server
```

**Mac**:
```bash
brew services start redis
```

**Linux**:
```bash
sudo systemctl start redis-server
```

#### Issue: Redis not starting on Windows
**Solution**: Use Docker or WSL

```bash
# Docker option
docker run -d -p 6379:6379 --name redis redis:alpine

# WSL option
wsl
sudo service redis-server start
```

---

## 🐳 Docker Alternative (Easiest for Development)

If you have Docker installed, you can skip all the above and use Docker Compose:

**Create `docker-compose.dev.yml`**:
```yaml
version: '3.8'

services:
  db:
    image: pgvector/pgvector:pg15
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: intelligent_doc_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

**Start both services**:
```bash
docker-compose -f docker-compose.dev.yml up -d

# Verify
docker ps
# Should show both postgres and redis running

# Connect to PostgreSQL
docker exec -it intelligent-doc-assistant-db-1 psql -U postgres

# Connect to Redis
docker exec -it intelligent-doc-assistant-redis-1 redis-cli ping
```

---

## 📚 Next Steps

After installing PostgreSQL and Redis:

1. ✅ Verify installations with the checklist above
2. ✅ Create the project database
3. ✅ Update your `.env` file with database credentials
4. ✅ Test connections
5. ✅ Continue with [GETTING_STARTED.md](./GETTING_STARTED.md)

---

## 🆘 Still Having Issues?

1. **Check if services are running**:
   ```bash
   # PostgreSQL
   # Windows: Check Services (services.msc)
   # Mac: brew services list
   # Linux: sudo systemctl status postgresql

   # Redis
   # Windows: Check Services or Task Manager
   # Mac: brew services list
   # Linux: sudo systemctl status redis-server
   ```

2. **Check firewall**: Make sure ports 5432 (PostgreSQL) and 6379 (Redis) are not blocked

3. **Restart your computer**: Sometimes services need a restart to work properly

4. **Use Docker**: If all else fails, Docker is the easiest option

---

**Need more help?** Check:
- PostgreSQL docs: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- Redis docs: [https://redis.io/docs/](https://redis.io/docs/)
- Stack Overflow: Search for your specific error message

---

*Last updated: January 2026*
