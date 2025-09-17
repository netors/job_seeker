# 🤖 AI-Powered Job Search System

An intelligent job search system built with CrewAI that uses multiple AI agents to find, evaluate, and recommend job opportunities tailored to your profile.

## ✨ Features

- **🔍 Multi-Platform Search**: Searches across Indeed, LinkedIn, Glassdoor, and more
- **🎯 Smart Matching**: AI-powered evaluation with 0-100 match scores
- **📊 Comprehensive Analysis**: Detailed reports with application strategies
- **💾 Persistent Storage**: SQLite database for tracking and history
- **🎨 Customizable**: Flexible search parameters and job site selection

## 🚀 Quick Start

### 1. Install

```bash
git clone https://github.com/netors/job_seeker.git
cd job_seeker
pip install -e .
```

### 2. Configure

```bash
# Set up environment
cp env_template.txt .env
# Edit .env with your API keys

# Configure profile
# Edit knowledge/resume_template.json with your information
```

### 3. Run

```bash
python src/job_seeker/main.py run
```

## 🏗️ How It Works

The system uses **5 specialized AI agents** working together:

1. **🔍 Job Search Agent** - Discovers opportunities across platforms
2. **⚖️ Job Evaluator Agent** - Scores jobs against your profile
3. **🗄️ Database Manager Agent** - Stores and organizes data
4. **📄 Report Generator Agent** - Creates comprehensive analysis
5. **🎯 Application Coordinator Agent** - Provides strategic guidance

## 📊 What You Get

After each search, the system generates:

- **📋 Comprehensive Report** (`job_search_report.md`) - Top opportunities with detailed analysis
- **📝 Application Strategy** (`application_strategy.md`) - Personalized guidance and templates
- **💾 Job Database** (`job_opportunities.db`) - All opportunities with scores and history

## 🔑 API Keys Required

- **SerperDev API** (Required): [Get free key](https://serper.dev/) - 100 searches/month
- **OpenAI API** (Recommended): [Get key](https://platform.openai.com/) - Best AI performance

## 📖 Documentation

**Complete documentation available in the [`docs/`](docs/) folder:**

| Guide | Description |
|-------|-------------|
| **[Installation Guide](docs/installation.md)** | Complete setup with troubleshooting |
| **[Profile Configuration](docs/profile-configuration.md)** | Optimize your profile for better matches |
| **[Usage Guide](docs/usage.md)** | All commands and advanced features |
| **[Output Files Guide](docs/output-files.md)** | Understanding reports and database |
| **[Architecture](docs/architecture.md)** | Technical implementation details |
| **[Troubleshooting](docs/troubleshooting.md)** | Common issues and solutions |

**Visual Documentation:**
- [System Architecture Diagrams](docs/crew_architecture_diagram.md)
- [Agent Workflow Diagrams](docs/crew_sequence_diagram.md)
- [Process Flow Diagrams](docs/crew_workflow_diagram.md)

## 🌐 Live Demo

Check out our [GitHub Pages site](https://netors.github.io/job_seeker/) for:
- Interactive architecture diagrams
- Complete feature overview
- Setup walkthrough
- API documentation

## ⚡ Example Usage

```bash
# Basic job search
python src/job_seeker/main.py run

# Custom search with specific sites
python src/job_seeker/main.py search_custom '{
  "job_sites": ["indeed.com", "linkedin.com"],
  "search_query": "Senior Python Developer",
  "location": "Remote"
}'

# View previous results
python src/job_seeker/main.py view_results
```

## 🛠️ Requirements

- **Python 3.10+** (supports up to 3.13)
- **API Keys**: SerperDev (required), OpenAI (recommended)
- **Dependencies**: Automatically installed with `pip install -e .`

## 📁 Project Structure

```
job_seeker/
├── src/job_seeker/              # Main application code
│   ├── config/                  # Agent and task configurations
│   ├── tools/                   # Custom CrewAI tools
│   ├── crew.py                  # Main crew orchestrator
│   └── main.py                  # CLI interface
├── knowledge/                   # User profile and data
├── docs/                        # Comprehensive documentation
├── pages/                       # GitHub Pages website
└── README.md                    # This file
```

## 🎯 Match Scoring Algorithm

Jobs are evaluated based on weighted criteria:
- **Skills Match (40%)** - Technical alignment with requirements
- **Experience Level (25%)** - Years of experience compatibility
- **Location Preference (15%)** - Geographic and remote work fit
- **Salary Expectations (10%)** - Compensation alignment
- **Company Culture (10%)** - Company type and culture fit

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with detailed description

See our [Development Guide](docs/development.md) for technical details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) - Multi-agent framework
- [SerperDev](https://serper.dev/) - Web search API
- [OpenAI](https://openai.com/) - AI language models

## 📞 Support

**Need help?**

1. **📖 Check the docs**: Start with our [comprehensive documentation](docs/)
2. **🔍 Search issues**: Look for similar problems in [GitHub Issues](https://github.com/netors/job_seeker/issues)
3. **🆘 Get help**: Create a [new issue](https://github.com/netors/job_seeker/issues/new) with details
4. **💬 Community**: Join discussions and share experiences

**Quick Links:**
- [Installation Problems?](docs/troubleshooting.md#installation-issues)
- [Configuration Help](docs/profile-configuration.md)
- [Usage Examples](docs/usage.md#workflow-examples)
- [API Issues](docs/troubleshooting.md#api-issues)

---

**🎯 Ready to transform your job search?** Start with our [Installation Guide](docs/installation.md) and find your next opportunity with AI!

**👨‍💻 Follow the Creator:** [@eruysanchez](http://x.com/eruysanchez)