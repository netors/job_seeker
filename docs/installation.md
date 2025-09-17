# Installation Guide

Complete installation and setup guide for the AI-Powered Job Search System.

## Prerequisites

### System Requirements

- **Python 3.10 or higher** (supports up to 3.13)
- **Git** for version control
- **Virtual environment** support (venv or conda)
- **pip** package manager (latest version recommended)

### Check Your Python Version

```bash
python --version  # Should show 3.10+
pip --version     # Should be available
```

If you need to install Python, visit [python.org](https://python.org) or use your system's package manager.

## Installation Steps

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/netors/job_seeker.git
cd job_seeker
```

### 2. Set Up Virtual Environment (Recommended)

Using a virtual environment isolates the project dependencies:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install in development mode (recommended)
pip install -e .

# This installs all required dependencies:
# - crewai[tools]>=0.186.1
# - requests>=2.31.0
# - pydantic>=2.0.0
# - beautifulsoup4>=4.12.0
# - python-dotenv>=1.0.0
```

### 4. Environment Configuration

Set up your environment variables:

```bash
# Copy the environment template
cp env_template.txt .env

# Edit the .env file with your API keys
nano .env  # or use your preferred editor
```

## API Keys Setup

### Required: SerperDev API Key

The SerperDev API is required for job search functionality:

1. Visit [serper.dev](https://serper.dev/)
2. Sign up for a free account
3. Get your API key (100 free searches per month)
4. Add to your `.env` file:

```bash
SERPER_API_KEY=your_serper_api_key_here
```

### Recommended: OpenAI API Key

For best AI performance, configure OpenAI:

1. Visit [platform.openai.com](https://platform.openai.com/)
2. Create an account or sign in
3. Generate an API key
4. Add to your `.env` file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### Complete .env File Example

```bash
# Required: SerperDev API for job search
SERPER_API_KEY=your_serper_api_key_here

# Recommended: OpenAI API for best AI performance
OPENAI_API_KEY=your_openai_api_key_here

# Model selection (optional)
MODEL=gpt-4o

# Disable telemetry (optional)
CREWAI_DISABLE_TELEMETRY=true
CREWAI_DISABLE_TRACKING=true
OTEL_SDK_DISABLED=true
```

## Verification

### Test Installation

```bash
# Test system functionality
python src/job_seeker/main.py test

# Should show:
# ✅ Dependencies installed correctly
# ✅ Environment variables configured
# ✅ API connections working
# ✅ Database permissions OK
```

### Available Commands

After installation, these commands become available:

```bash
# Direct script execution
python src/job_seeker/main.py run

# Installed command shortcuts (after pip install -e .)
job_seeker      # equivalent to run command
run_crew       # equivalent to run command
```

## Troubleshooting

### Common Installation Issues

#### Python Version Error
```
ERROR: This package requires Python 3.10 or higher
```
**Solution:** Install Python 3.10+ from [python.org](https://python.org)

#### pip Install Fails
```
ERROR: Could not build wheels for some-package
```
**Solution:** Update pip and setuptools:
```bash
pip install --upgrade pip setuptools wheel
```

#### Virtual Environment Issues
```
ERROR: No module named 'venv'
```
**Solution:** Install python3-venv:
```bash
# Ubuntu/Debian
sudo apt install python3-venv

# macOS with Homebrew
brew install python
```

#### Permission Denied
```
ERROR: Could not install packages due to PermissionError
```
**Solution:** Use virtual environment or user installation:
```bash
pip install --user -e .
```

### Dependency Conflicts

If you encounter dependency conflicts:

```bash
# Create fresh environment
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
```

### API Key Issues

#### SerperDev API Not Working
1. Check API key format (should be a long string)
2. Verify account status at [serper.dev](https://serper.dev/)
3. Check monthly usage limits
4. Ensure no extra spaces in .env file

#### OpenAI API Issues
1. Verify API key is valid and active
2. Check account billing status
3. Ensure sufficient credits available
4. Test with simpler model (gpt-3.5-turbo)

## Next Steps

After successful installation:

1. **Configure Profile**: Set up your `knowledge/resume_template.json` - see [Profile Configuration](profile-configuration.md)
2. **Run First Search**: Execute your first job search - see [Usage Guide](usage.md)
3. **Understand Output**: Learn about generated reports - see [Output Files](output-files.md)

## Advanced Installation

### Development Installation

For contributors or advanced users:

```bash
# Clone with full history
git clone --recursive https://github.com/netors/job_seeker.git

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Docker Installation (Future)

Docker support is planned for future releases:

```bash
# Future feature
docker run -d job-seeker:latest
```

### Multiple Environment Setup

For managing multiple configurations:

```bash
# Production environment
cp env_template.txt .env.prod

# Development environment
cp env_template.txt .env.dev

# Load specific environment
source .env.prod  # or .env.dev
```

## Support

If you encounter issues during installation:

1. Check the [Troubleshooting Guide](troubleshooting.md)
2. Review [Common Issues](https://github.com/netors/job_seeker/issues)
3. Create a new issue with:
   - Your operating system
   - Python version
   - Complete error message
   - Steps you've already tried