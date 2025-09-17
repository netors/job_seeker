# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI-powered job search system built with CrewAI that uses multiple specialized agents to find, evaluate, and recommend job opportunities. The system searches across multiple job boards using the SerperDev API, evaluates matches based on user profiles, stores results in a SQLite database, and generates comprehensive markdown reports. The project includes a GitHub Pages site showcasing the system's capabilities.

## Common Development Commands

### Running the Application

```bash
# Main job search with default profile
python src/job_seeker/main.py run

# Custom job search with specific sites
python src/job_seeker/main.py search_custom '{"job_sites": ["indeed.com", "linkedin.com"]}'

# View previous results
python src/job_seeker/main.py view_results

# Update user profile interactively
python src/job_seeker/main.py update_profile

# Other commands
python src/job_seeker/main.py train <iterations> <output_file>
python src/job_seeker/main.py replay <task_id>
python src/job_seeker/main.py test

# Using project scripts (after pip install -e .)
job_seeker  # equivalent to run command
run_crew   # equivalent to run command
```

### Installing Dependencies

```bash
# Install in development mode (recommended)
pip install -e .

# Install specific dependencies
pip install crewai[tools]>=0.186.1

# Set up environment variables
cp env_template.txt .env
# Edit .env with your API keys
```

## Architecture Overview

### Multi-Agent System

The system uses 5 specialized CrewAI agents:

1. **Job Search Agent** (`job_search_agent`): Searches multiple job platforms using the `job_search_tool`
2. **Job Evaluator** (`job_evaluator`): Scores opportunities 0-100 based on profile match using `job_evaluation_tool`
3. **Database Manager** (`database_manager`): Stores opportunities in SQLite database using `database_tool`
4. **Report Generator** (`report_generator`): Creates markdown reports using `report_generation_tool`
5. **Application Coordinator** (`application_coordinator`): Provides application strategy

Agents execute tasks sequentially with context passing between tasks.

### Key Components

- **Crew Definition**: `src/job_seeker/crew.py` - Main JobSeeker class that orchestrates agents
- **Agent/Task Configs**: `src/job_seeker/config/agents.yaml` and `tasks.yaml` - Define agent roles and task descriptions
- **Custom Tools**: `src/job_seeker/tools/job_search_tools.py` - Implements job search, evaluation, database, and report tools
- **CLI Interface**: `src/job_seeker/main.py` - Entry point with commands for run, search_custom, update_profile, view_results, train, test, replay
- **User Profile**: `knowledge/resume_template.json` - JSON template for user information (use as template)
- **Environment Config**: `env_template.txt` - Template for environment variables and API keys
- **Documentation**: `docs/` - Architecture diagrams in Mermaid format
- **GitHub Pages**: `index.html` - Project showcase website

### Data Flow

1. User profile loaded from `knowledge/resume_template.json`
2. Job search performed across configured sites (Indeed, LinkedIn, Glassdoor, etc.)
3. Jobs evaluated and scored based on skills match, experience, location, salary
4. Results stored in `job_opportunities.db` SQLite database
5. Reports generated as `job_search_report.md` and `application_strategy.md`

## User Profile Configuration

The system requires a properly configured user profile in `knowledge/resume_template.json` with:
- Personal info (name, email, phone)
- Professional details (current_role, years_experience)
- Skills array (technical and soft skills)
- Location preferences (location, preferred_locations)
- Salary expectations (expected_salary)
- Company type preferences (preferred_company_type)
- Education history with degrees and institutions
- Experience history with achievements
- Certifications and projects
- Languages and interests

**Note**: The template file contains placeholder values - replace with your actual information.

## Testing

Currently no automated tests are implemented. Use `python src/job_seeker/main.py test` for manual crew testing.

## Environment Variables

Required environment variables (copy `env_template.txt` to `.env`):
- `SERPER_API_KEY`: For web search functionality (get free key at serper.dev)
- `OPENAI_API_KEY`: For OpenAI models (optional, but recommended)
- `MODEL`: Specify model to use (default: gpt-4o)
- `CREWAI_DISABLE_TELEMETRY`: Set to true to disable telemetry

## Project Structure

```
job_seeker/
├── src/job_seeker/           # Main package
│   ├── config/               # Agent and task configurations
│   ├── tools/                # Custom CrewAI tools
│   ├── crew.py              # Main crew orchestrator
│   └── main.py              # CLI interface
├── knowledge/               # User profile and data
├── docs/                    # Architecture diagrams
├── index.html              # GitHub Pages site
├── env_template.txt        # Environment template
├── pyproject.toml          # Project configuration
└── .gitignore             # Git ignore rules
```

## Generated Files

After running job search:
- `job_search_report.md` - Comprehensive job analysis
- `application_strategy.md` - Application guidance
- `job_opportunities.db` - SQLite database with results

## Python Environment

- Python 3.10+ required (supports up to 3.13)
- Virtual environment recommended at `.venv/`
- Main dependencies:
  - crewai[tools]>=0.186.1
  - requests>=2.31.0
  - pydantic>=2.0.0
  - beautifulsoup4>=4.12.0
  - python-dotenv>=1.0.0

## API Keys Setup

1. **SerperDev API** (Required for job search):
   - Visit https://serper.dev/ and sign up
   - Get free API key (100 searches/month)
   - Add to .env as SERPER_API_KEY

2. **OpenAI API** (Recommended for best results):
   - Visit https://platform.openai.com/
   - Generate API key
   - Add to .env as OPENAI_API_KEY