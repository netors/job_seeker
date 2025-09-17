#!/usr/bin/env python
import sys
import warnings
import json
import os
from datetime import datetime

from job_seeker.crew import JobSeeker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the job search crew.
    """
    print("🚀 Starting AI-Powered Job Search System")
    print("=" * 50)
    
    # Initialize the job seeker crew
    job_seeker = JobSeeker()
    
    # Load user profile
    user_profile = job_seeker.load_user_profile()
    
    if not user_profile:
        print("❌ No user profile found. Please update knowledge/resume_template.json")
        print("📝 The template includes fields for:")
        print("   - Personal information (name, email, phone)")
        print("   - Professional details (current role, experience)")
        print("   - Skills and technologies")
        print("   - Location preferences")
        print("   - Salary expectations")
        print("   - Education and certifications")
        return
    
    # Display user profile summary
    print(f"👤 Job Search for: {user_profile.get('name', 'Unknown')}")
    print(f"💼 Current Role: {user_profile.get('current_role', 'Unknown')}")
    print(f"🎯 Experience: {user_profile.get('years_experience', 'Unknown')} years")
    print(f"📍 Location: {user_profile.get('location', 'Unknown')}")
    print(f"💰 Expected Salary: ${user_profile.get('expected_salary', 'Unknown'):,}")
    print(f"🛠️  Key Skills: {', '.join(user_profile.get('skills', [])[:5])}")
    print("=" * 50)
    
    # Get job sites to search (optional)
    job_sites = None
    if len(sys.argv) > 1:
        try:
            job_sites = json.loads(sys.argv[1])
            print(f"🎯 Custom job sites: {', '.join(job_sites)}")
        except json.JSONDecodeError:
            print("⚠️  Invalid job sites format. Using default sites.")
    
    try:
        # Run the job search
        result = job_seeker.run_job_search(user_profile, job_sites)
        
        print("\n🎉 Job search completed successfully!")
        print("📊 Check the generated files for detailed results:")
        print("   📄 job_search_report.md - Comprehensive analysis")
        print("   📋 application_strategy.md - Application guidance")
        print("   🗄️  job_opportunities.db - Database of opportunities")
        
        return result
        
    except Exception as e:
        print(f"❌ An error occurred during job search: {e}")
        raise Exception(f"Job search failed: {e}")


def search_custom():
    """
    Run job search with custom parameters.
    Usage: python main.py search_custom '{"job_sites": ["indeed.com", "linkedin.com"], "search_query": "AI Engineer"}'
    """
    if len(sys.argv) < 2:
        print("❌ Please provide custom search parameters as JSON")
        print("Example: python main.py search_custom '{\"job_sites\": [\"indeed.com\"], \"search_query\": \"AI Engineer\"}'")
        return
    
    try:
        custom_params = json.loads(sys.argv[1])
        job_seeker = JobSeeker()
        user_profile = job_seeker.load_user_profile()
        
        if not user_profile:
            print("❌ No user profile found. Please update knowledge/resume_template.json")
            return
        
        # Override search query if provided
        if 'search_query' in custom_params:
            user_profile['custom_search'] = custom_params['search_query']
        
        job_sites = custom_params.get('job_sites')
        
        print(f"🔍 Custom search: {custom_params.get('search_query', 'Default')}")
        print(f"🌐 Target sites: {', '.join(job_sites) if job_sites else 'Default'}")
        
        result = job_seeker.run_job_search(user_profile, job_sites)
        return result
        
    except json.JSONDecodeError:
        print("❌ Invalid JSON format for custom parameters")
    except Exception as e:
        print(f"❌ Error in custom search: {e}")


def update_profile():
    """
    Interactive profile update.
    """
    print("📝 Profile Update Tool")
    print("=" * 30)
    
    profile_path = os.path.join(os.path.dirname(__file__), '..', 'knowledge', 'resume_template.json')
    
    if not os.path.exists(profile_path):
        print(f"❌ Profile file not found at {profile_path}")
        return
    
    print(f"📄 Current profile location: {profile_path}")
    print("✏️  Please edit the file directly and run the job search again.")
    print("💡 Key fields to update:")
    print("   - name: Your full name")
    print("   - current_role: Your current job title")
    print("   - years_experience: Years of professional experience")
    print("   - skills: List of your technical skills")
    print("   - preferred_locations: Where you want to work")
    print("   - expected_salary: Your salary expectation")


def view_results():
    """
    View previous job search results.
    """
    print("📊 Viewing Job Search Results")
    print("=" * 30)
    
    # Check for generated files
    files_to_check = [
        'job_search_report.md',
        'application_strategy.md',
        'job_opportunities.db'
    ]
    
    for file in files_to_check:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - Not found")
    
    # If report exists, show summary
    if os.path.exists('job_search_report.md'):
        print("\n📄 Job Search Report Summary:")
        print("-" * 30)
        try:
            with open('job_search_report.md', 'r') as f:
                lines = f.readlines()
                # Show first 20 lines as preview
                for i, line in enumerate(lines[:20]):
                    print(line.rstrip())
                if len(lines) > 20:
                    print(f"... ({len(lines) - 20} more lines)")
        except Exception as e:
            print(f"Error reading report: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    print("🏋️ Training Job Search Crew")
    print("=" * 30)
    
    # Load user profile for training
    job_seeker = JobSeeker()
    user_profile = job_seeker.load_user_profile()
    
    if not user_profile:
        print("❌ No user profile found for training")
        return
    
    inputs = {
        'user_profile': json.dumps(user_profile),
        'job_sites': ["indeed.com", "linkedin.com/jobs", "glassdoor.com"],
        'search_query': f"{user_profile.get('current_role', 'Software Engineer')}"
    }
    
    try:
        n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 3
        filename = sys.argv[2] if len(sys.argv) > 2 else 'job_search_training.json'
        
        print(f"🔄 Training for {n_iterations} iterations")
        print(f"💾 Results will be saved to {filename}")
        
        job_seeker.crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
        print("✅ Training completed successfully!")
        
    except Exception as e:
        print(f"❌ Training failed: {e}")
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    if len(sys.argv) < 2:
        print("❌ Please provide a task ID to replay")
        print("Usage: python main.py replay <task_id>")
        return
    
    try:
        task_id = sys.argv[1]
        print(f"🔄 Replaying task: {task_id}")
        JobSeeker().crew().replay(task_id=task_id)
        print("✅ Replay completed successfully!")
        
    except Exception as e:
        print(f"❌ Replay failed: {e}")
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    print("🧪 Testing Job Search Crew")
    print("=" * 30)
    
    # Load user profile for testing
    job_seeker = JobSeeker()
    user_profile = job_seeker.load_user_profile()
    
    if not user_profile:
        print("❌ No user profile found for testing")
        return
    
    inputs = {
        'user_profile': json.dumps(user_profile),
        'job_sites': ["indeed.com", "linkedin.com/jobs"],
        'search_query': f"{user_profile.get('current_role', 'Software Engineer')}"
    }
    
    try:
        n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 2
        eval_llm = sys.argv[2] if len(sys.argv) > 2 else "gpt-4"
        
        print(f"🔬 Testing with {n_iterations} iterations")
        print(f"🤖 Using LLM: {eval_llm}")
        
        JobSeeker().crew().test(n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs)
        print("✅ Testing completed successfully!")
        
    except Exception as e:
        print(f"❌ Testing failed: {e}")
        raise Exception(f"An error occurred while testing the crew: {e}")


def help():
    """
    Show help information.
    """
    print("🤖 AI-Powered Job Search System")
    print("=" * 40)
    print("Available commands:")
    print()
    print("🚀 run                    - Start job search with your profile")
    print("🔍 search_custom          - Search with custom parameters")
    print("📝 update_profile         - Update your profile information")
    print("📊 view_results           - View previous search results")
    print("🏋️  train                 - Train the crew")
    print("🔄 replay <task_id>       - Replay a specific task")
    print("🧪 test                   - Test the crew")
    print("❓ help                   - Show this help message")
    print()
    print("Examples:")
    print("  python main.py run")
    print("  python main.py search_custom '{\"job_sites\": [\"indeed.com\"]}'")
    print("  python main.py train 5 training_results.json")
    print("  python main.py replay task_123")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        run()
    else:
        command = sys.argv[1]
        if command == "search_custom":
            search_custom()
        elif command == "update_profile":
            update_profile()
        elif command == "view_results":
            view_results()
        elif command == "train":
            train()
        elif command == "replay":
            replay()
        elif command == "test":
            test()
        elif command == "help":
            help()
        else:
            print(f"❌ Unknown command: {command}")
            print("Run 'python main.py help' for available commands")
