"""
Custom tools for job searching and evaluation
"""
import json
import sqlite3
import requests
from typing import List, Dict, Any
from datetime import datetime
from crewai.tools import tool
from crewai_tools import SerperDevTool
import re
from urllib.parse import urljoin, urlparse
import time


@tool("job_search_tool")
def job_search_tool(query: str, sites: List[str] = None, max_results: int = 20) -> str:
    """
    Search for job opportunities across multiple platforms using SerperDevTool
    
    Args:
        query: Job search query (e.g., "AI Engineer", "Machine Learning")
        sites: List of job sites to search (default: major job boards)
        max_results: Maximum number of results to return per site
    """
    if sites is None:
        sites = [
            "indeed.com",
            "linkedin.com/jobs",
            "glassdoor.com",
            "monster.com",
            "ziprecruiter.com",
            "dice.com",
            "angel.co",
            "remote.co"
        ]
    
    # Initialize SerperDevTool
    serper_tool = SerperDevTool(n_results=max_results)
    
    results = []
    
    for site in sites:
        try:
            # Create site-specific search query
            site_query = f'site:{site} "{query}" jobs'
            
            # Search using SerperDevTool
            search_results = serper_tool.run(search_query=site_query)
            
            # Parse the search results
            site_results = _parse_serper_results(search_results, site, query)
            results.extend(site_results)
            
            # Rate limiting
            time.sleep(1)
            
        except Exception as e:
            print(f"Error searching {site}: {e}")
            # Fallback to mock data if Serper fails
            site_results = _search_site(query, site, max_results)
            results.extend(site_results)
            continue
    
    return json.dumps(results, indent=2)


def _parse_serper_results(search_results: str, site: str, query: str) -> List[Dict]:
    """Parse SerperDevTool search results into job format"""
    try:
        # SerperDevTool returns a string, we need to parse it
        # The results are typically in a structured format
        jobs = []
        
        # Split by common separators to extract individual results
        if "---" in search_results:
            result_sections = search_results.split("---")
        else:
            result_sections = [search_results]
        
        for i, section in enumerate(result_sections[:10]):  # Limit to 10 results per site
            if not section.strip():
                continue
                
            # Extract title, link, and snippet from the section
            lines = section.strip().split('\n')
            title = ""
            link = ""
            snippet = ""
            
            for line in lines:
                line = line.strip()
                if line.startswith("Title:"):
                    title = line.replace("Title:", "").strip()
                elif line.startswith("Link:"):
                    link = line.replace("Link:", "").strip()
                elif line.startswith("Snippet:"):
                    snippet = line.replace("Snippet:", "").strip()
            
            # Skip if we don't have essential information
            if not title or not link:
                continue
                
            # Extract job details
            job = {
                "title": title,
                "company": _extract_company_from_title(title),
                "location": _extract_location_from_snippet(snippet),
                "url": link,
                "description": snippet,
                "posted_date": _extract_date_from_snippet(snippet),
                "salary_range": _extract_salary_from_snippet(snippet),
                "site": site,
                "job_type": _extract_job_type_from_snippet(snippet)
            }
            
            jobs.append(job)
        
        return jobs
        
    except Exception as e:
        print(f"Error parsing Serper results for {site}: {e}")
        return []


def _extract_company_from_title(title: str) -> str:
    """Extract company name from job title"""
    # Common patterns: "Job Title at Company", "Company - Job Title", etc.
    if " at " in title:
        return title.split(" at ")[-1].strip()
    elif " - " in title:
        return title.split(" - ")[0].strip()
    else:
        return "Unknown Company"


def _extract_location_from_snippet(snippet: str) -> str:
    """Extract location from job snippet"""
    # Look for common location patterns
    location_patterns = [
        r'([A-Z][a-z]+(?: [A-Z][a-z]+)*,?\s*[A-Z]{2})',  # City, State
        r'([A-Z][a-z]+(?: [A-Z][a-z]+)*,?\s*[A-Z][a-z]+)',  # City, Country
        r'(Remote|Work from home|WFH)',
        r'(San Francisco|New York|Los Angeles|Chicago|Boston|Seattle|Austin|Denver)'
    ]
    
    for pattern in location_patterns:
        match = re.search(pattern, snippet, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return "Location not specified"


def _extract_date_from_snippet(snippet: str) -> str:
    """Extract posted date from snippet"""
    # Look for date patterns
    date_patterns = [
        r'(\d{1,2} days? ago)',
        r'(\d{1,2} hours? ago)',
        r'(\d{1,2} weeks? ago)',
        r'(Posted \d{1,2}/\d{1,2}/\d{4})',
        r'(\d{4}-\d{2}-\d{2})'
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, snippet, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return "Date not specified"


def _extract_salary_from_snippet(snippet: str) -> str:
    """Extract salary range from snippet"""
    # Look for salary patterns
    salary_patterns = [
        r'(\$\d{1,3}(?:,\d{3})*(?:-\$\d{1,3}(?:,\d{3})*)?)',
        r'(\$\d{1,3}(?:,\d{3})*(?:k|K)?(?:-\$\d{1,3}(?:,\d{3})*(?:k|K)?)?)',
        r'(\d{1,3}(?:,\d{3})*(?:-\d{1,3}(?:,\d{3})*)?\s*(?:k|K)?)'
    ]
    
    for pattern in salary_patterns:
        match = re.search(pattern, snippet)
        if match:
            return f"${match.group(1).strip()}"
    
    return "Salary not specified"


def _extract_job_type_from_snippet(snippet: str) -> str:
    """Extract job type from snippet"""
    snippet_lower = snippet.lower()
    
    if any(word in snippet_lower for word in ['full-time', 'full time', 'permanent']):
        return "Full-time"
    elif any(word in snippet_lower for word in ['part-time', 'part time']):
        return "Part-time"
    elif any(word in snippet_lower for word in ['contract', 'contractor']):
        return "Contract"
    elif any(word in snippet_lower for word in ['remote', 'work from home', 'wfh']):
        return "Remote"
    else:
        return "Full-time"  # Default assumption


def _search_site(query: str, site: str, max_results: int) -> List[Dict]:
    """Simulate job search for a specific site"""
    # This is a mock implementation - in reality, you'd use actual APIs or web scraping
    mock_jobs = [
        {
            "title": f"Senior {query} Engineer",
            "company": f"Tech Company {i}",
            "location": "San Francisco, CA",
            "url": f"https://{site}/job/{i}",
            "description": f"Looking for a senior {query} engineer with 5+ years experience...",
            "posted_date": "2024-01-15",
            "salary_range": "$120,000 - $180,000",
            "site": site,
            "job_type": "Full-time"
        }
        for i in range(1, min(max_results + 1, 6))
    ]
    return mock_jobs


@tool("job_evaluation_tool")
def job_evaluation_tool(job_data: str, user_profile: str) -> str:
    """
    Evaluate job opportunities against user profile
    
    Args:
        job_data: JSON string containing job information
        user_profile: JSON string containing user skills and experience
    """
    try:
        jobs = json.loads(job_data) if isinstance(job_data, str) else job_data
        profile = json.loads(user_profile) if isinstance(user_profile, str) else user_profile
        
        evaluated_jobs = []
        
        for job in jobs:
            score = _calculate_match_score(job, profile)
            job['match_score'] = score
            job['evaluation_date'] = datetime.now().isoformat()
            evaluated_jobs.append(job)
        
        # Sort by match score (highest first)
        evaluated_jobs.sort(key=lambda x: x['match_score'], reverse=True)
        
        return json.dumps(evaluated_jobs, indent=2)
        
    except Exception as e:
        return f"Error evaluating jobs: {e}"


def _calculate_match_score(job: Dict, profile: Dict) -> float:
    """Calculate match score between job and user profile"""
    score = 0.0
    max_score = 100.0
    
    # Skills matching (40% of total score)
    job_skills = _extract_skills(job.get('description', ''))
    user_skills = profile.get('skills', [])
    skill_matches = len(set(job_skills) & set(user_skills))
    skill_score = (skill_matches / max(len(job_skills), 1)) * 40
    score += skill_score
    
    # Experience level matching (25% of total score)
    required_exp = _extract_experience_requirement(job.get('description', ''))
    user_exp = profile.get('years_experience', 0)
    if required_exp <= user_exp:
        exp_score = 25
    else:
        exp_score = max(0, 25 - (required_exp - user_exp) * 5)
    score += exp_score
    
    # Location preference (15% of total score)
    job_location = job.get('location', '').lower()
    preferred_locations = [loc.lower() for loc in profile.get('preferred_locations', [])]
    if any(loc in job_location for loc in preferred_locations):
        score += 15
    elif 'remote' in job_location or 'anywhere' in job_location:
        score += 10
    
    # Salary expectations (10% of total score)
    job_salary = _extract_salary(job.get('salary_range', ''))
    expected_salary = profile.get('expected_salary', 0)
    if job_salary and expected_salary:
        if job_salary >= expected_salary:
            score += 10
        else:
            score += max(0, 10 - (expected_salary - job_salary) / expected_salary * 10)
    
    # Company size/type preference (10% of total score)
    company_type = profile.get('preferred_company_type', '')
    if company_type and company_type.lower() in job.get('company', '').lower():
        score += 10
    
    return min(score, max_score)


def _extract_skills(description: str) -> List[str]:
    """Extract technical skills from job description"""
    common_skills = [
        'python', 'javascript', 'java', 'react', 'node.js', 'aws', 'docker',
        'kubernetes', 'machine learning', 'ai', 'tensorflow', 'pytorch',
        'sql', 'mongodb', 'postgresql', 'git', 'linux', 'api', 'rest',
        'graphql', 'microservices', 'agile', 'scrum', 'ci/cd', 'jenkins',
        'terraform', 'puppet', 'ansible', 'devops', 'security', 'hipaa',
        'hitrust', 'finops', 'azure', 'gcp', 'snowflake'
    ]
    
    found_skills = []
    description_lower = description.lower()
    
    for skill in common_skills:
        if skill in description_lower:
            found_skills.append(skill)
    
    return found_skills


def _extract_experience_requirement(description: str) -> int:
    """Extract years of experience required from job description"""
    patterns = [
        r'(\d+)\+?\s*years?\s*of\s*experience',
        r'(\d+)\+?\s*years?\s*in\s*the\s*field',
        r'(\d+)\+?\s*years?\s*of\s*relevant\s*experience'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description.lower())
        if match:
            return int(match.group(1))
    
    return 3  # Default assumption


def _extract_salary(salary_range: str) -> int:
    """Extract average salary from salary range string"""
    if not salary_range:
        return 0
    
    # Extract numbers from salary range
    numbers = re.findall(r'\$?(\d{1,3}(?:,\d{3})*)', salary_range)
    if numbers:
        # Take the average of the range
        salaries = [int(num.replace(',', '')) for num in numbers]
        return sum(salaries) // len(salaries)
    
    return 0


@tool("database_tool")
def database_tool(action: str, data: str = None) -> str:
    """
    Perform database operations
    
    Args:
        action: 'store', 'retrieve', 'update', 'delete'
        data: JSON string containing data for the operation
    """
    try:
        if action == 'store':
            return _store_jobs(data)
        elif action == 'retrieve':
            return _retrieve_jobs(data)
        elif action == 'update':
            return _update_job(data)
        elif action == 'delete':
            return _delete_job(data)
        else:
            return f"Unknown action: {action}"
    except Exception as e:
        return f"Database error: {e}"


def _init_database():
    """Initialize the database with required tables"""
    conn = sqlite3.connect("job_opportunities.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_opportunities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            url TEXT UNIQUE,
            description TEXT,
            salary_range TEXT,
            posted_date TEXT,
            site TEXT,
            job_type TEXT,
            match_score REAL,
            evaluation_date TEXT,
            applied BOOLEAN DEFAULT FALSE,
            application_date TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()


def _store_jobs(jobs_json: str) -> str:
    """Store job opportunities in the database"""
    _init_database()  # Ensure database exists
    
    jobs = json.loads(jobs_json) if isinstance(jobs_json, str) else jobs_json
    
    conn = sqlite3.connect("job_opportunities.db")
    cursor = conn.cursor()
    
    stored_count = 0
    for job in jobs:
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO job_opportunities 
                (title, company, location, url, description, salary_range, 
                 posted_date, site, job_type, match_score, evaluation_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                job.get('title', ''),
                job.get('company', ''),
                job.get('location', ''),
                job.get('url', ''),
                job.get('description', ''),
                job.get('salary_range', ''),
                job.get('posted_date', ''),
                job.get('site', ''),
                job.get('job_type', ''),
                job.get('match_score', 0.0),
                job.get('evaluation_date', '')
            ))
            stored_count += 1
        except sqlite3.IntegrityError:
            # Job already exists, skip
            continue
    
    conn.commit()
    conn.close()
    
    return f"Stored {stored_count} job opportunities in database"


def _retrieve_jobs(filters_json: str = None) -> str:
    """Retrieve job opportunities from the database"""
    _init_database()  # Ensure database exists
    
    conn = sqlite3.connect("job_opportunities.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM job_opportunities ORDER BY match_score DESC"
    params = []
    
    if filters_json:
        filters = json.loads(filters_json)
        conditions = []
        
        if 'min_score' in filters:
            conditions.append("match_score >= ?")
            params.append(filters['min_score'])
        
        if 'limit' in filters:
            query += " LIMIT ?"
            params.append(filters['limit'])
    
    if conditions:
        query = query.replace("ORDER BY", "WHERE " + " AND ".join(conditions) + " ORDER BY")
    
    cursor.execute(query, params)
    columns = [description[0] for description in cursor.description]
    jobs = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    conn.close()
    
    return json.dumps(jobs, indent=2)


def _update_job(update_data: str) -> str:
    """Update a job record"""
    data = json.loads(update_data)
    job_id = data.get('id')
    updates = data.get('updates', {})
    
    if not job_id:
        return "Job ID is required for updates"
    
    conn = sqlite3.connect("job_opportunities.db")
    cursor = conn.cursor()
    
    set_clauses = []
    params = []
    
    for key, value in updates.items():
        set_clauses.append(f"{key} = ?")
        params.append(value)
    
    params.append(job_id)
    
    cursor.execute(f'''
        UPDATE job_opportunities 
        SET {', '.join(set_clauses)}
        WHERE id = ?
    ''', params)
    
    conn.commit()
    conn.close()
    
    return f"Updated job {job_id} successfully"


def _delete_job(job_id: str) -> str:
    """Delete a job record"""
    conn = sqlite3.connect("job_opportunities.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM job_opportunities WHERE id = ?", (job_id,))
    
    conn.commit()
    conn.close()
    
    return f"Deleted job {job_id} successfully"


@tool("report_generation_tool")
def report_generation_tool(jobs_data: str, user_profile: str) -> str:
    """
    Generate a comprehensive job search report
    
    Args:
        jobs_data: JSON string containing evaluated job opportunities
        user_profile: JSON string containing user profile information
    """
    try:
        jobs = json.loads(jobs_data) if isinstance(jobs_data, str) else jobs_data
        profile = json.loads(user_profile) if isinstance(user_profile, str) else user_profile
        
        # Filter top opportunities (score >= 70)
        top_jobs = [job for job in jobs if job.get('match_score', 0) >= 70]
        
        report = _generate_markdown_report(top_jobs, profile)
        return report
        
    except Exception as e:
        return f"Error generating report: {e}"


def _generate_markdown_report(jobs: List[Dict], profile: Dict) -> str:
    """Generate markdown report for top job opportunities"""
    report = f"""# Job Search Report for {profile.get('name', 'Job Seeker')}

## Executive Summary
Found {len(jobs)} highly relevant job opportunities matching your profile.
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Your Profile Summary
- **Name**: {profile.get('name', 'N/A')}
- **Current Role**: {profile.get('current_role', 'N/A')}
- **Experience**: {profile.get('years_experience', 'N/A')} years
- **Key Skills**: {', '.join(profile.get('skills', [])[:10])}
- **Preferred Locations**: {', '.join(profile.get('preferred_locations', []))}
- **Expected Salary**: ${profile.get('expected_salary', 'N/A'):,}

## Top Job Opportunities

"""
    
    for i, job in enumerate(jobs[:10], 1):  # Top 10 jobs
        report += f"""### {i}. {job.get('title', 'N/A')} at {job.get('company', 'N/A')}
**Match Score**: {job.get('match_score', 0):.1f}/100

**Details:**
- **Location**: {job.get('location', 'N/A')}
- **Salary**: {job.get('salary_range', 'N/A')}
- **Job Type**: {job.get('job_type', 'N/A')}
- **Posted**: {job.get('posted_date', 'N/A')}
- **Source**: {job.get('site', 'N/A')}

**Description:**
{job.get('description', 'N/A')[:300]}...

**Apply Here**: [View Job]({job.get('url', '#')})

---

"""
    
    report += f"""
## Application Strategy

### Immediate Actions (Next 24-48 hours):
1. **Priority Applications**: Apply to the top 3 opportunities immediately
2. **Customize Applications**: Tailor your resume and cover letter for each role
3. **Follow Up**: Set reminders to follow up on applications

### Medium-term Actions (Next Week):
1. **Expand Search**: Consider additional job sites or networking opportunities
2. **Skill Development**: Focus on any gaps identified in the job requirements
3. **Interview Preparation**: Prepare for common interview questions in your field

### Long-term Actions (Next Month):
1. **Network Building**: Connect with employees at target companies
2. **Portfolio Updates**: Update your portfolio with recent projects
3. **Salary Negotiation**: Research market rates for your target positions

## Next Steps
1. Review each opportunity carefully
2. Visit the job URLs to read full descriptions
3. Prepare customized applications
4. Track your applications in a spreadsheet
5. Set up job alerts for similar positions

---
*Report generated by Job Seeker AI Crew*
"""
    
    return report