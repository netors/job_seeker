# 🤖 AI-Powered Job Search System

An intelligent job search system built with [CrewAI](https://www.crewai.com/) that uses multiple AI agents to find, evaluate, and recommend job opportunities tailored to your profile.

## ✨ Features

- **🔍 Multi-Platform Search**: Searches across Indeed, LinkedIn, Glassdoor, and more
- **🎯 Smart Matching**: AI-powered evaluation with 0-100 match scores
- **📊 Comprehensive Analysis**: Detailed reports with application strategies
- **💾 Persistent Storage**: SQLite database for tracking and history
- **🎨 Customizable**: Flexible search parameters and job site selection
- **🤖 CrewAI Framework**: Built with CrewAI's multi-agent orchestration

## 🚀 Quick Start

### 1. Install

```bash
git clone https://github.com/netors/job_seeker.git
cd job_seeker
crewai install
```

> **Note**: This is a CrewAI project. The `crewai install` command will install all dependencies and set up the project structure according to CrewAI standards.

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
crewai run
```

## 🏗️ How It Works

Built with [CrewAI's multi-agent framework](https://docs.crewai.com/), the system uses **5 specialized AI agents** working together in a sequential process:

1. **🔍 Job Search Agent** - Discovers opportunities across platforms
2. **⚖️ Job Evaluator Agent** - Scores jobs against your profile
3. **🗄️ Database Manager Agent** - Stores and organizes data
4. **📄 Report Generator Agent** - Creates comprehensive analysis
5. **🎯 Application Coordinator Agent** - Provides strategic guidance

### CrewAI Integration

This project follows [CrewAI best practices](https://docs.crewai.com/en/quickstart):
- **YAML Configuration**: Agents and tasks defined in `config/` directory
- **@CrewBase Decorator**: Main crew class with agent and task decorators
- **Sequential Process**: Tasks execute in order with proper context passing
- **Custom Tools**: Specialized job search and evaluation tools
- **CrewAI CLI**: Use `crewai run`, `crewai train`, `crewai test` commands

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

**CrewAI Framework Documentation:**
- [CrewAI Quickstart](https://docs.crewai.com/en/quickstart) - Get started with CrewAI
- [CrewAI Agents](https://docs.crewai.com/concepts/agents) - Learn about agent configuration
- [CrewAI Tasks](https://docs.crewai.com/concepts/tasks) - Understand task workflows
- [CrewAI Tools](https://docs.crewai.com/concepts/tools) - Create custom tools

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
crewai run

# Train the crew
crewai train

# Test the crew
crewai test

# Replay a specific task
crewai replay <task_id>
```

## 🛠️ Requirements

- **Python 3.10+** (supports up to 3.13)
- **CrewAI**: Multi-agent framework for AI orchestration
- **API Keys**: SerperDev (required), OpenAI (recommended)
- **Dependencies**: Automatically installed with `crewai install`

## 📁 Project Structure

```
job_seeker/
├── src/job_seeker/              # Main CrewAI application
│   ├── config/                  # Agent and task YAML configurations
│   │   ├── agents.yaml          # Agent definitions and roles
│   │   └── tasks.yaml           # Task definitions and workflows
│   ├── tools/                   # Custom CrewAI tools
│   ├── crew.py                  # CrewAI crew orchestrator (@CrewBase)
│   └── main.py                  # Entry point and CLI interface
├── knowledge/                   # User profile and data
├── docs/                        # Comprehensive documentation
├── pages/                       # GitHub Pages website
├── pyproject.toml               # CrewAI project configuration
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

- [CrewAI](https://www.crewai.com/) - Multi-agent orchestration framework
- [SerperDev](https://serper.dev/) - Web search API for job discovery
- [OpenAI](https://openai.com/) - AI language models for agent reasoning

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

## 🚀 CrewAI Features

This project showcases advanced CrewAI capabilities:
- **Multi-Agent Collaboration**: 5 specialized agents working in harmony
- **YAML Configuration**: Easy agent and task customization
- **Custom Tools**: Specialized job search and evaluation tools
- **Sequential Processing**: Tasks execute with proper context flow
- **Training & Testing**: Built-in crew training and testing capabilities
- **Replay Functionality**: Debug and replay specific tasks

**👨‍💻 Follow the Creator:** [@eruysanchez](http://x.com/eruysanchez)