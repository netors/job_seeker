# Usage Guide

Complete guide to using the AI-Powered Job Search System for finding and evaluating job opportunities.

## Overview

The system provides several commands for different types of job searches and system management. All commands are executed through the main Python script or installed command shortcuts.

## Basic Commands

### Standard Job Search

Execute a complete job search using your configured profile:

```bash
# Full command
python src/job_seeker/main.py run

# Shortcut (after pip install -e .)
job_seeker
# or
run_crew
```

**What it does:**
- Loads your profile from `knowledge/resume_template.json`
- Searches across multiple job platforms
- Evaluates each opportunity against your profile
- Stores results in SQLite database
- Generates comprehensive reports

**Example output:**
```
🚀 Starting AI-Powered Job Search System
==================================================
👤 Job Search for: John Doe
💼 Current Role: Software Engineer
🎯 Experience: 5 years
📍 Location: San Francisco, CA
💰 Expected Salary: $150,000
🛠️ Key Skills: Python, JavaScript, React, AWS, Docker
==================================================

🔍 Job Search Agent: Discovering opportunities...
⚖️ Job Evaluator Agent: Scoring matches...
🗄️ Database Manager Agent: Storing results...
📄 Report Generator Agent: Creating analysis...
🎯 Application Coordinator Agent: Preparing strategy...

🎉 Job search completed successfully!
📊 Generated files:
   📄 job_search_report.md - Comprehensive analysis
   📋 application_strategy.md - Application guidance
   🗄️ job_opportunities.db - Database of opportunities
```

### Custom Job Search

Perform targeted searches with specific parameters:

```bash
python src/job_seeker/main.py search_custom 'JSON_PARAMETERS'
```

**Basic custom search:**
```bash
python src/job_seeker/main.py search_custom '{
  "job_sites": ["indeed.com", "linkedin.com"],
  "search_query": "Senior Python Developer",
  "location": "Remote"
}'
```

**Advanced custom search:**
```bash
python src/job_seeker/main.py search_custom '{
  "job_sites": ["indeed.com", "linkedin.com", "glassdoor.com"],
  "search_query": "Machine Learning Engineer",
  "location": "San Francisco Bay Area",
  "max_results": 50,
  "salary_min": 120000,
  "experience_level": "senior"
}'
```

### View Previous Results

Check your previous search results and generated files:

```bash
python src/job_seeker/main.py view_results
```

**Output includes:**
- Last search execution time
- Number of opportunities found
- Generated file locations and sizes
- Database statistics
- Quick summary of top matches

## Advanced Usage

### Profile Management

Update your profile configuration interactively:

```bash
python src/job_seeker/main.py update_profile
```

This command provides:
- Profile validation and syntax checking
- Field-by-field guidance
- Best practices recommendations
- Completeness assessment

### System Testing

Verify all components are working correctly:

```bash
python src/job_seeker/main.py test
```

**Tests include:**
- API connectivity (SerperDev, OpenAI)
- Database operations and schema
- File system permissions
- Agent initialization
- Configuration validation

### Training the System

Improve agent performance through training iterations:

```bash
python src/job_seeker/main.py train <iterations> <output_file>

# Example:
python src/job_seeker/main.py train 5 training_results.json
```

**Training benefits:**
- Improved job matching accuracy
- Better evaluation scoring
- Enhanced report quality
- Optimized agent coordination

### Task Replay

Replay specific tasks for debugging or analysis:

```bash
python src/job_seeker/main.py replay <task_id>

# Example:
python src/job_seeker/main.py replay task_job_search_20241201_143022
```

## Search Customization Options

### Job Site Selection

Available job sites for targeted searches:

- `indeed.com` - Indeed job board
- `linkedin.com` - LinkedIn job postings
- `glassdoor.com` - Glassdoor opportunities
- `dice.com` - Dice tech jobs

**Example:**
```json
{
  "job_sites": ["indeed.com", "dice.com"]
}
```

### Search Query Customization

Override profile-based search terms:

```json
{
  "search_query": "Senior Full Stack Developer"
}
```

**Tips:**
- Use specific role titles for targeted results
- Include key technologies: "Python Django Developer"
- Add seniority level: "Senior", "Lead", "Principal"

### Location Targeting

Specify locations different from your profile:

```json
{
  "location": "New York City",
  "preferred_locations": ["New York, NY", "Brooklyn, NY", "Remote"]
}
```

**Location formats:**
- City, State: "San Francisco, CA"
- Metro areas: "San Francisco Bay Area"
- Remote work: "Remote"
- International: "London, UK"

### Result Limits

Control the number of results returned:

```json
{
  "max_results": 30
}
```

**Recommendations:**
- Default: 20 results (good balance)
- Quick search: 10 results
- Comprehensive: 50-100 results
- Training data: 100+ results

### Salary Filtering

Filter opportunities by salary range:

```json
{
  "salary_min": 100000,
  "salary_max": 200000
}
```

### Experience Level Targeting

Target specific experience levels:

```json
{
  "experience_level": "senior"
}
```

**Available levels:**
- `entry` - Entry level positions
- `mid` - Mid-level roles
- `senior` - Senior positions
- `lead` - Lead/Staff roles
- `executive` - Executive positions

## Workflow Examples

### Daily Job Search Routine

```bash
# 1. Quick search for new opportunities
python src/job_seeker/main.py search_custom '{
  "max_results": 10,
  "search_query": "Recent Senior Developer Postings"
}'

# 2. View and compare with previous results
python src/job_seeker/main.py view_results

# 3. Update application tracking (manual process)
```

### Weekly Comprehensive Search

```bash
# 1. Update profile if needed
python src/job_seeker/main.py update_profile

# 2. Run full search across all platforms
python src/job_seeker/main.py run

# 3. Analyze results and plan applications
# Review job_search_report.md and application_strategy.md
```

### Targeted Company Research

```bash
# 1. Search specific companies
python src/job_seeker/main.py search_custom '{
  "job_sites": ["linkedin.com", "glassdoor.com"],
  "search_query": "Google Software Engineer",
  "location": "Mountain View, CA"
}'

# 2. Compare with general market
python src/job_seeker/main.py search_custom '{
  "search_query": "Software Engineer",
  "location": "Silicon Valley"
}'
```

### Market Research

```bash
# 1. Search different experience levels
python src/job_seeker/main.py search_custom '{
  "experience_level": "mid",
  "max_results": 50
}'

python src/job_seeker/main.py search_custom '{
  "experience_level": "senior",
  "max_results": 50
}'

# 2. Compare salary ranges and requirements
# Analyze reports for market trends
```

## Performance Optimization

### Faster Searches

For quicker results:
- Limit job sites: `["indeed.com"]`
- Reduce max_results: `10-20`
- Use specific search terms
- Target single locations

### Comprehensive Coverage

For thorough searches:
- Include all job sites
- Increase max_results: `50-100`
- Use broader search terms
- Include multiple locations

### API Rate Limit Management

**SerperDev Free Tier:**
- 100 searches per month
- Plan searches strategically
- Use custom searches for specific needs

**Optimization strategies:**
- Combine multiple criteria in single searches
- Use training mode sparingly
- Monitor usage with view_results

## Error Handling and Recovery

### Common Issues

#### API Timeout
```
⚠️ SerperDev API timeout - falling back to mock data
```
**Action:** System continues with mock data, retry later

#### Profile Not Found
```
❌ No user profile found
```
**Action:** Configure `knowledge/resume_template.json`

#### Invalid Search Parameters
```
❌ Invalid JSON format for custom parameters
```
**Action:** Validate JSON syntax and parameter names

### Automatic Recovery

The system includes fallback mechanisms:
- **API failures:** Switches to mock data
- **Network issues:** Retries with exponential backoff
- **Database errors:** Creates new database if corrupted
- **Agent failures:** Attempts recovery or skips problematic tasks

### Manual Recovery

If searches consistently fail:

```bash
# 1. Test system components
python src/job_seeker/main.py test

# 2. Check configuration
python src/job_seeker/main.py update_profile

# 3. Try minimal search
python src/job_seeker/main.py search_custom '{
  "job_sites": ["indeed.com"],
  "max_results": 5
}'
```

## Integration and Automation

### Scheduling Regular Searches

Using cron (Unix/Linux/macOS):
```bash
# Add to crontab for daily searches at 9 AM
0 9 * * * cd /path/to/job_seeker && python src/job_seeker/main.py run
```

Using Windows Task Scheduler:
1. Create basic task
2. Set trigger for daily execution
3. Set action to run Python script

### Data Export and Integration

The SQLite database can be queried for custom analysis:

```sql
-- Export opportunities to CSV
.mode csv
.output opportunities.csv
SELECT title, company, location, match_score, url
FROM job_opportunities
ORDER BY match_score DESC;
```

### API Integration (Future)

Planned features for future releases:
- REST API for external integrations
- Webhook notifications for new opportunities
- Integration with job tracking tools

## Best Practices

### Search Strategy

1. **Start Broad:** Use general searches to understand the market
2. **Refine Gradually:** Narrow down based on initial results
3. **Regular Updates:** Run searches weekly or bi-weekly
4. **Profile Evolution:** Update profile as skills and preferences change

### Result Analysis

1. **Review Match Scores:** Understand why jobs scored high/low
2. **Skills Gap Analysis:** Identify areas for improvement
3. **Market Trends:** Track salary and requirement changes
4. **Company Research:** Use generated insights for applications

### Application Workflow

1. **Prioritize High Scores:** Focus on 80+ match scores first
2. **Customize Applications:** Use generated strategies
3. **Track Progress:** Update database with application status
4. **Iterate Search:** Refine based on application success

## Next Steps

After mastering basic usage:

1. **Understand Output**: Learn about [generated reports](output-files.md)
2. **Optimize Profile**: Fine-tune for better matches
3. **Advanced Features**: Explore training and customization
4. **Troubleshooting**: Resolve issues with the [troubleshooting guide](troubleshooting.md)

For technical details, see:
- [Architecture Documentation](architecture.md)
- [API Reference](api-reference.md)
- [Development Guide](development.md)