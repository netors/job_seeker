from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import json
import os
from .tools.job_search_tools import job_search_tool, job_evaluation_tool, database_tool, report_generation_tool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class JobSeeker():
    """JobSeeker crew - AI-powered job search and application system"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        super().__init__()
        # Tools are now imported as functions

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def job_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['job_search_agent'], # type: ignore[index]
            tools=[job_search_tool],
            verbose=True
        )

    @agent
    def job_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['job_evaluator'], # type: ignore[index]
            tools=[job_evaluation_tool],
            verbose=True
        )

    @agent
    def database_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['database_manager'], # type: ignore[index]
            tools=[database_tool],
            verbose=True
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'], # type: ignore[index]
            tools=[report_generation_tool],
            verbose=True
        )

    @agent
    def application_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['application_coordinator'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def job_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_search_task'], # type: ignore[index]
            context=[],  # Will be populated with user profile
        )

    @task
    def job_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_evaluation_task'], # type: ignore[index]
            context=[self.job_search_task()],
        )

    @task
    def database_storage_task(self) -> Task:
        return Task(
            config=self.tasks_config['database_storage_task'], # type: ignore[index]
            context=[self.job_evaluation_task()],
        )

    @task
    def report_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_generation_task'], # type: ignore[index]
            context=[self.job_evaluation_task()],
            output_file='job_search_report.md'
        )

    @task
    def application_coordination_task(self) -> Task:
        return Task(
            config=self.tasks_config['application_coordination_task'], # type: ignore[index]
            context=[self.report_generation_task()],
            output_file='application_strategy.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the JobSeeker crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

    def load_user_profile(self, profile_path: str = None) -> dict:
        """Load user profile from JSON file"""
        if profile_path is None:
            profile_path = os.path.join(os.path.dirname(__file__), '..', '..', 'knowledge', 'resume_template.json')
        
        try:
            with open(profile_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Profile file not found at {profile_path}")
            print("Please update the resume_template.json file with your information")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error parsing profile file: {e}")
            return {}

    def run_job_search(self, user_profile: dict = None, job_sites: list = None):
        """Run the complete job search process"""
        if user_profile is None:
            user_profile = self.load_user_profile()
        
        if not user_profile:
            print("No user profile available. Please check your resume_template.json file.")
            return
        
        # Prepare inputs for the crew
        inputs = {
            'user_profile': json.dumps(user_profile),
            'job_sites': job_sites or [
                "indeed.com",
                "linkedin.com/jobs", 
                "glassdoor.com",
                "dice.com",           # Great for tech jobs
                "remote.co",          # Remote work focused
                "angel.co",           # Startup jobs
                "stackoverflow.com/jobs",  # Developer focused
                "github.com/careers", # Tech company jobs
                "weworkremotely.com", # Remote work
                "flexjobs.com"        # Flexible work
            ],
            'search_query': f"{user_profile.get('current_role', 'Software Engineer')} {user_profile.get('skills', [])[0] if user_profile.get('skills') else ''}"
        }
        
        print(f"Starting job search for {user_profile.get('name', 'Job Seeker')}")
        print(f"Searching for: {inputs['search_query']}")
        print(f"Target sites: {', '.join(inputs['job_sites'])}")
        
        try:
            result = self.crew().kickoff(inputs=inputs)
            print("\n" + "="*50)
            print("JOB SEARCH COMPLETED SUCCESSFULLY!")
            print("="*50)
            print("Check the following files for results:")
            print("- job_search_report.md (Comprehensive report)")
            print("- application_strategy.md (Application guidance)")
            print("- job_opportunities.db (Database of opportunities)")
            return result
        except Exception as e:
            print(f"Error during job search: {e}")
            raise
