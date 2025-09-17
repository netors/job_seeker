# Troubleshooting Guide

Comprehensive troubleshooting guide for common issues with the AI-Powered Job Search System.

## Quick Diagnostic Commands

Before diving into specific issues, run these commands to quickly identify problems:

```bash
# Test overall system health
python src/job_seeker/main.py test

# Check configuration
python src/job_seeker/main.py update_profile

# View system information
python --version
pip list | grep crewai
ls -la knowledge/resume_template.json
ls -la .env
```

## Installation Issues

### Python Version Problems

**Error:**
```
ERROR: This package requires Python 3.10 or higher
```

**Solution:**
```bash
# Check current Python version
python --version
python3 --version

# Install Python 3.10+ (macOS with Homebrew)
brew install python@3.10

# Install Python 3.10+ (Ubuntu/Debian)
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-pip

# Windows: Download from python.org
```

**Verification:**
```bash
# Ensure correct Python is in PATH
which python3.10
python3.10 --version
```

### Virtual Environment Issues

**Error:**
```
ERROR: No module named 'venv'
```

**Solution:**
```bash
# Install venv module (Ubuntu/Debian)
sudo apt install python3-venv

# Alternative: Use virtualenv
pip install virtualenv
virtualenv .venv

# Alternative: Use conda
conda create -n job_seeker python=3.10
conda activate job_seeker
```

**Common venv problems:**
```bash
# Can't activate virtual environment
# Windows PowerShell execution policy issue
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Permission denied on activation script
chmod +x .venv/bin/activate

# Wrong Python version in venv
rm -rf .venv
python3.10 -m venv .venv
```

### Dependency Installation Failures

**Error:**
```
ERROR: Could not build wheels for some-package
```

**Solutions:**
```bash
# Update build tools
pip install --upgrade pip setuptools wheel

# Install system dependencies (Ubuntu/Debian)
sudo apt install build-essential python3-dev

# Install system dependencies (macOS)
xcode-select --install

# Use pre-compiled wheels
pip install --only-binary=all -e .

# Clear pip cache and retry
pip cache purge
pip install -e .
```

**Specific package issues:**
```bash
# lxml installation issues
# Ubuntu/Debian:
sudo apt install libxml2-dev libxslt1-dev

# macOS:
brew install libxml2 libxslt

# Error with crewai installation
pip install --no-cache-dir crewai[tools]>=0.186.1
```

## Configuration Issues

### Environment Variables

**Error:**
```
❌ No user profile found
```

**Diagnosis:**
```bash
# Check if .env file exists
ls -la .env

# Check environment variables
echo $SERPER_API_KEY
echo $OPENAI_API_KEY

# Verify .env file format
cat .env
```

**Solutions:**
```bash
# Create .env file from template
cp env_template.txt .env

# Edit with correct format (no spaces around =)
SERPER_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Reload environment
source .env  # bash/zsh
# or restart terminal
```

**Common .env mistakes:**
```bash
# Wrong format (spaces around =)
SERPER_API_KEY = your_key_here  # ❌

# Correct format
SERPER_API_KEY=your_key_here    # ✅

# Missing quotes for special characters
API_KEY=key_with_special!chars  # ❌
API_KEY="key_with_special!chars" # ✅
```

### Profile Configuration Issues

**Error:**
```
❌ Invalid JSON in profile
```

**Diagnosis:**
```bash
# Check if profile file exists
ls -la knowledge/resume_template.json

# Validate JSON syntax
python -m json.tool knowledge/resume_template.json

# Check file permissions
ls -la knowledge/
```

**Solutions:**
```bash
# Fix JSON syntax errors
# Use online JSON validator: jsonlint.com

# Common JSON errors:
# Missing comma
{
  "name": "John Doe"  # ❌ Missing comma
  "email": "john@example.com"
}

# Correct format
{
  "name": "John Doe",  # ✅
  "email": "john@example.com"
}

# Trailing comma (not allowed in JSON)
{
  "name": "John Doe",
  "email": "john@example.com",  # ❌ Trailing comma
}

# Fix file permissions
chmod 644 knowledge/resume_template.json
```

**Validation script:**
```python
#!/usr/bin/env python3
import json
import sys

def validate_profile(filename):
    try:
        with open(filename, 'r') as f:
            profile = json.load(f)

        required_fields = ['name', 'email', 'current_role', 'years_experience',
                          'location', 'preferred_locations', 'expected_salary', 'skills']

        missing_fields = [field for field in required_fields if field not in profile]

        if missing_fields:
            print(f"❌ Missing required fields: {missing_fields}")
            return False

        print("✅ Profile validation successful")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ JSON syntax error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return False

if __name__ == "__main__":
    validate_profile("knowledge/resume_template.json")
```

## API Issues

### SerperDev API Problems

**Error:**
```
❌ SerperDev API timeout
```

**Diagnosis:**
```bash
# Test API connectivity
curl -X POST https://google.serper.dev/search \
  -H "X-API-KEY: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"q": "test query"}'

# Check API key format
echo $SERPER_API_KEY | wc -c  # Should be ~40 characters
```

**Solutions:**
```bash
# Verify API key is correct
# Visit https://serper.dev/dashboard to check

# Check account status and usage
# Ensure you haven't exceeded free tier limits (100 searches/month)

# Test with simple query
python -c "
import os, requests
response = requests.post(
    'https://google.serper.dev/search',
    headers={'X-API-KEY': os.getenv('SERPER_API_KEY')},
    json={'q': 'test'}
)
print(f'Status: {response.status_code}')
print(f'Response: {response.text[:200]}')
"
```

**Rate limiting issues:**
```bash
# If hitting rate limits, spread out searches
python src/job_seeker/main.py search_custom '{
  "max_results": 10
}'

# Use mock data for testing
export SERPER_API_KEY=""  # This will trigger fallback to mock data
python src/job_seeker/main.py run
```

### OpenAI API Issues

**Error:**
```
❌ OpenAI API authentication failed
```

**Diagnosis:**
```bash
# Test OpenAI API
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
  https://api.openai.com/v1/models

# Check API key format
echo $OPENAI_API_KEY | cut -c1-7  # Should start with "sk-"
```

**Solutions:**
```bash
# Verify API key at https://platform.openai.com/

# Check billing status
# Ensure you have credits available

# Test with different model
export MODEL=gpt-3.5-turbo
python src/job_seeker/main.py run

# Use system without OpenAI (will use default model)
unset OPENAI_API_KEY
python src/job_seeker/main.py run
```

## Runtime Issues

### Database Problems

**Error:**
```
❌ Database connection failed
```

**Diagnosis:**
```bash
# Check if database file exists
ls -la job_opportunities.db

# Check file permissions
ls -la job_opportunities.db

# Check disk space
df -h .

# Test database integrity
sqlite3 job_opportunities.db "PRAGMA integrity_check;"
```

**Solutions:**
```bash
# Fix permissions
chmod 664 job_opportunities.db

# Delete corrupted database (will be recreated)
rm job_opportunities.db
python src/job_seeker/main.py run

# Check available disk space
# Ensure at least 100MB free space

# Manual database repair
sqlite3 job_opportunities.db << EOF
PRAGMA integrity_check;
VACUUM;
REINDEX;
EOF
```

**Database recovery script:**
```python
#!/usr/bin/env python3
import sqlite3
import shutil
from datetime import datetime

def recover_database():
    db_file = "job_opportunities.db"
    backup_file = f"job_opportunities_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"

    try:
        # Create backup
        shutil.copy2(db_file, backup_file)
        print(f"✅ Backup created: {backup_file}")

        # Test connection
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Check integrity
        cursor.execute("PRAGMA integrity_check")
        result = cursor.fetchone()[0]

        if result == "ok":
            print("✅ Database integrity OK")
        else:
            print(f"❌ Database integrity issues: {result}")

        # Repair operations
        cursor.execute("VACUUM")
        cursor.execute("REINDEX")

        conn.close()
        print("✅ Database repair completed")

    except Exception as e:
        print(f"❌ Database recovery failed: {e}")
        print(f"Restore from backup: mv {backup_file} {db_file}")

if __name__ == "__main__":
    recover_database()
```

### Memory Issues

**Error:**
```
MemoryError: Unable to allocate memory
```

**Diagnosis:**
```bash
# Check available memory
free -h  # Linux
vm_stat  # macOS
# Windows: Task Manager > Performance > Memory

# Check Python memory usage
python -c "
import psutil
import os
process = psutil.Process(os.getpid())
print(f'Memory usage: {process.memory_info().rss / 1024 / 1024:.1f} MB')
"
```

**Solutions:**
```bash
# Reduce search scope
python src/job_seeker/main.py search_custom '{
  "max_results": 10,
  "job_sites": ["indeed.com"]
}'

# Close other applications
# Increase swap space (Linux)
sudo swapon --show
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Network Issues

**Error:**
```
❌ Connection timeout
```

**Diagnosis:**
```bash
# Test internet connectivity
ping google.com

# Test specific APIs
curl -I https://google.serper.dev
curl -I https://api.openai.com

# Check DNS resolution
nslookup google.serper.dev
```

**Solutions:**
```bash
# Use different DNS servers
# Google DNS: 8.8.8.8, 8.8.4.4
# Cloudflare DNS: 1.1.1.1, 1.0.0.1

# Configure proxy if needed
export https_proxy=http://your-proxy:port
export http_proxy=http://your-proxy:port

# Increase timeout in code (temporary fix)
export REQUESTS_TIMEOUT=60
python src/job_seeker/main.py run

# Use offline mode (mock data)
export OFFLINE_MODE=true
python src/job_seeker/main.py run
```

## Agent and Task Issues

### Agent Initialization Failures

**Error:**
```
❌ Agent initialization failed
```

**Diagnosis:**
```bash
# Check YAML configuration files
python -c "
import yaml
with open('src/job_seeker/config/agents.yaml') as f:
    agents = yaml.safe_load(f)
print('Agents config loaded successfully')

with open('src/job_seeker/config/tasks.yaml') as f:
    tasks = yaml.safe_load(f)
print('Tasks config loaded successfully')
"

# Check for syntax errors
python -m yaml src/job_seeker/config/agents.yaml
python -m yaml src/job_seeker/config/tasks.yaml
```

**Solutions:**
```bash
# Fix YAML syntax errors
# Common issues: incorrect indentation, missing quotes

# Validate YAML online: yamllint.com

# Reset to default configuration
git checkout src/job_seeker/config/agents.yaml
git checkout src/job_seeker/config/tasks.yaml

# Check file permissions
chmod 644 src/job_seeker/config/*.yaml
```

### Task Execution Failures

**Error:**
```
❌ Task execution failed: job_search_task
```

**Diagnosis:**
```bash
# Check detailed logs
tail -f ~/.crewai/logs/job_seeker.log

# Run with verbose output
export CREWAI_LOG_LEVEL=DEBUG
python src/job_seeker/main.py run

# Test individual components
python -c "
from src.job_seeker.tools.job_search_tools import JobSearchTool
tool = JobSearchTool()
result = tool._run('software engineer', ['indeed.com'])
print(result[:200])
"
```

**Solutions:**
```bash
# Restart with fresh environment
deactivate
source .venv/bin/activate
python src/job_seeker/main.py run

# Clear any cached data
rm -rf ~/.crewai/cache/
rm -rf __pycache__/

# Run minimal test
python src/job_seeker/main.py search_custom '{
  "job_sites": ["indeed.com"],
  "max_results": 1
}'
```

## Performance Issues

### Slow Execution

**Symptoms:**
- Job search takes longer than 10 minutes
- High CPU or memory usage
- System becomes unresponsive

**Diagnosis:**
```bash
# Monitor resource usage
top -p $(pgrep -f job_seeker)  # Linux
Activity Monitor  # macOS

# Profile Python execution
python -m cProfile -s cumulative src/job_seeker/main.py run

# Check I/O wait
iostat 1 10  # Linux
```

**Solutions:**
```bash
# Reduce search scope
python src/job_seeker/main.py search_custom '{
  "max_results": 20,
  "job_sites": ["indeed.com", "linkedin.com"]
}'

# Close unnecessary applications
# Use SSD instead of HDD if possible

# Optimize database
sqlite3 job_opportunities.db << EOF
ANALYZE;
VACUUM;
REINDEX;
EOF
```

### API Rate Limiting

**Error:**
```
❌ Rate limit exceeded
```

**Solutions:**
```bash
# Spread out API calls
# Wait before retrying
sleep 60
python src/job_seeker/main.py run

# Use smaller batch sizes
python src/job_seeker/main.py search_custom '{
  "max_results": 10
}'

# Upgrade API plan if needed
# Check SerperDev dashboard for usage
```

## Common Error Messages

### Error Reference Table

| Error Message | Cause | Solution |
|--------------|-------|----------|
| `No module named 'crewai'` | Dependencies not installed | `pip install -e .` |
| `SERPER_API_KEY not found` | Missing environment variable | Add to `.env` file |
| `Invalid JSON in profile` | Syntax error in profile | Validate JSON syntax |
| `Permission denied` | File permissions issue | `chmod 644 filename` |
| `Database is locked` | SQLite lock conflict | Close other database connections |
| `Connection timeout` | Network issues | Check internet connection |
| `Out of memory` | Insufficient RAM | Reduce search scope |
| `Agent initialization failed` | YAML configuration error | Check agents.yaml syntax |
| `Task execution timeout` | Long-running operation | Increase timeout or reduce scope |
| `Import error` | Missing dependency | `pip install missing_package` |

## Recovery Procedures

### Complete System Reset

When multiple issues persist:

```bash
# 1. Backup important data
cp job_opportunities.db job_opportunities_backup.db
cp knowledge/resume_template.json knowledge/resume_backup.json

# 2. Clean environment
deactivate
rm -rf .venv
rm -rf __pycache__
rm -rf ~/.crewai/cache/

# 3. Fresh installation
python3.10 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .

# 4. Reconfigure
cp env_template.txt .env
# Edit .env with your API keys

# 5. Test
python src/job_seeker/main.py test
```

### Data Recovery

If data is lost or corrupted:

```bash
# Check for automatic backups
ls -la *.db.backup
ls -la backups/

# Restore from Git (if versioned)
git log --oneline
git checkout HEAD~1 -- job_opportunities.db

# Export data before corruption
sqlite3 job_opportunities_backup.db << EOF
.mode csv
.output recovered_jobs.csv
SELECT * FROM job_opportunities;
EOF
```

## Getting Additional Help

### Log Analysis

Enable detailed logging for better diagnostics:

```bash
# Set environment variables
export CREWAI_LOG_LEVEL=DEBUG
export PYTHONPATH=$(pwd)/src

# Run with logging
python src/job_seeker/main.py run 2>&1 | tee debug.log

# Analyze logs
grep "ERROR" debug.log
grep "WARNING" debug.log
tail -50 debug.log
```

### Creating Bug Reports

When reporting issues, include:

1. **System Information:**
```bash
python --version
pip list | grep crewai
uname -a  # Linux/macOS
systeminfo  # Windows
```

2. **Error Details:**
```bash
# Full error traceback
# Steps to reproduce
# Expected vs actual behavior
# Configuration files (remove sensitive data)
```

3. **Log Files:**
```bash
# Recent log entries
tail -100 ~/.crewai/logs/job_seeker.log

# System logs
journalctl -u python  # Linux systemd
Console.app  # macOS
Event Viewer  # Windows
```

### Community Resources

- **[GitHub Issues](https://github.com/netors/job_seeker/issues)**: Report bugs and feature requests
- **Documentation**: Review latest docs for updates
- **CrewAI Community**: Framework-specific issues
- **Stack Overflow**: General Python and AI questions

### Professional Support

For mission-critical deployments:
- Consider commercial CrewAI support
- Hire Python/AI development consultants
- Set up monitoring and alerting systems
- Implement backup and disaster recovery plans

## Prevention Best Practices

### Regular Maintenance

```bash
# Weekly maintenance script
#!/bin/bash

# Update dependencies
pip list --outdated
pip install --upgrade crewai

# Clean cache
rm -rf __pycache__/
rm -rf ~/.crewai/cache/

# Database maintenance
sqlite3 job_opportunities.db "VACUUM; REINDEX;"

# Backup data
cp job_opportunities.db "backups/job_opportunities_$(date +%Y%m%d).db"

# Test system
python src/job_seeker/main.py test
```

### Monitoring Setup

```python
# Basic monitoring script
import psutil
import sqlite3
import os
from datetime import datetime

def health_check():
    """Basic system health monitoring"""
    issues = []

    # Check disk space
    disk_usage = psutil.disk_usage('.')
    if disk_usage.percent > 90:
        issues.append(f"Low disk space: {disk_usage.percent}%")

    # Check memory
    memory = psutil.virtual_memory()
    if memory.percent > 80:
        issues.append(f"High memory usage: {memory.percent}%")

    # Check database
    try:
        conn = sqlite3.connect('job_opportunities.db')
        conn.execute("SELECT 1")
        conn.close()
    except Exception as e:
        issues.append(f"Database issue: {e}")

    # Check API keys
    if not os.getenv('SERPER_API_KEY'):
        issues.append("Missing SERPER_API_KEY")

    if issues:
        print(f"⚠️  Health check issues found:")
        for issue in issues:
            print(f"   - {issue}")
    else:
        print("✅ System health check passed")

    return len(issues) == 0

if __name__ == "__main__":
    health_check()
```

By following this troubleshooting guide, you should be able to resolve most common issues with the AI-Powered Job Search System. Remember to check the basics first (Python version, dependencies, configuration) before diving into complex solutions.