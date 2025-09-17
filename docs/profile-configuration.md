# Profile Configuration Guide

Learn how to configure your personal and professional profile for optimal job matching.

## Overview

The AI-powered job search system requires a detailed user profile to provide accurate job matching and personalized recommendations. Your profile is stored in `knowledge/resume_template.json` and serves as the foundation for all job evaluations.

## Profile Structure

### Required Fields

These fields are essential for the system to function properly:

```json
{
  "name": "string",
  "email": "string",
  "current_role": "string",
  "years_experience": "number",
  "location": "string",
  "preferred_locations": ["array"],
  "expected_salary": "number",
  "skills": ["array"]
}
```

### Complete Profile Template

```json
{
  "name": "Your Full Name",
  "email": "your.email@example.com",
  "phone": "(555) 123-4567",
  "current_role": "Software Engineer",
  "years_experience": 5,
  "location": "San Francisco, CA",
  "preferred_locations": ["San Francisco, CA", "Remote", "New York, NY"],
  "expected_salary": 150000,
  "preferred_company_type": "tech_startup",
  "skills": [
    "Python",
    "JavaScript",
    "React",
    "Node.js",
    "AWS",
    "Docker",
    "Kubernetes"
  ],
  "education": [
    {
      "degree": "Bachelor of Science in Computer Science",
      "institution": "University of Technology",
      "graduation_year": 2018
    }
  ],
  "experience": [
    {
      "title": "Senior Software Engineer",
      "company": "Tech Company Inc.",
      "duration": "2020-Present",
      "achievements": [
        "Led development of microservices architecture",
        "Mentored junior developers",
        "Implemented CI/CD pipelines"
      ]
    }
  ],
  "certifications": [
    "AWS Certified Solutions Architect",
    "Certified Kubernetes Administrator"
  ],
  "projects": [
    {
      "name": "E-commerce Platform",
      "description": "Built scalable microservices platform",
      "technologies": ["Python", "React", "PostgreSQL"],
      "url": "https://github.com/username/project"
    }
  ],
  "languages": ["English (Native)", "Spanish (Conversational)"],
  "interests": ["Cloud Architecture", "Machine Learning", "Open Source"]
}
```

## Field-by-Field Guide

### Personal Information

#### name
- **Type**: String (required)
- **Purpose**: Used in reports and application materials
- **Example**: `"John Doe"`
- **Tips**: Use your professional name as it appears on your resume

#### email
- **Type**: String (required)
- **Purpose**: Primary contact for applications
- **Example**: `"john.doe@email.com"`
- **Tips**: Use a professional email address

#### phone
- **Type**: String (optional)
- **Purpose**: Contact information for recruiters
- **Example**: `"(555) 123-4567"`
- **Tips**: Include country/area code for international opportunities

### Professional Information

#### current_role
- **Type**: String (required)
- **Purpose**: Defines your professional level and search criteria
- **Example**: `"Senior Software Engineer"`
- **Tips**: Use the title you're targeting if unemployed

#### years_experience
- **Type**: Number (required)
- **Purpose**: Matches experience requirements in job postings
- **Example**: `5`
- **Tips**: Count total professional experience in your field

#### skills
- **Type**: Array of strings (required)
- **Purpose**: Core matching criteria for job opportunities
- **Example**: `["Python", "React", "AWS", "Machine Learning"]`
- **Tips**:
  - Include 10-20 most relevant skills
  - Mix technical and soft skills
  - Use industry-standard terminology
  - Keep current with technologies you actively use

### Location and Preferences

#### location
- **Type**: String (required)
- **Purpose**: Current location for local job searches
- **Example**: `"San Francisco, CA"`
- **Tips**: Use city, state/province format

#### preferred_locations
- **Type**: Array of strings (required)
- **Purpose**: Expands search to multiple locations
- **Example**: `["San Francisco, CA", "Remote", "Seattle, WA"]`
- **Tips**:
  - Include "Remote" if open to remote work
  - Add cities within commuting distance
  - Consider relocation opportunities

#### expected_salary
- **Type**: Number (required)
- **Purpose**: Filters opportunities and salary negotiations
- **Example**: `150000`
- **Tips**:
  - Research market rates for your role and location
  - Use base salary, not total compensation
  - Be realistic based on experience level

#### preferred_company_type
- **Type**: String (optional)
- **Purpose**: Filters companies by type and culture
- **Options**: `"startup"`, `"enterprise"`, `"nonprofit"`, `"healthcare_tech"`, `"fintech"`
- **Example**: `"tech_startup"`

### Experience and Education

#### education
- **Type**: Array of objects (optional)
- **Purpose**: Educational background for role requirements
- **Structure**:
```json
{
  "degree": "Bachelor of Science in Computer Science",
  "institution": "University of Technology",
  "graduation_year": 2018,
  "gpa": "3.8" // optional
}
```

#### experience
- **Type**: Array of objects (optional)
- **Purpose**: Work history and achievements
- **Structure**:
```json
{
  "title": "Senior Software Engineer",
  "company": "Tech Company Inc.",
  "duration": "2020-Present",
  "description": "Brief role description",
  "achievements": [
    "Quantifiable achievement 1",
    "Quantifiable achievement 2"
  ]
}
```

#### certifications
- **Type**: Array of strings (optional)
- **Purpose**: Professional credentials and qualifications
- **Example**: `["AWS Certified Solutions Architect 2023", "PMP Certified"]`
- **Tips**: Include year of certification if relevant

#### projects
- **Type**: Array of objects (optional)
- **Purpose**: Notable projects and portfolio items
- **Structure**:
```json
{
  "name": "Project Name",
  "description": "Brief project description and impact",
  "technologies": ["Tech1", "Tech2", "Tech3"],
  "url": "https://github.com/username/project"
}
```

### Additional Information

#### languages
- **Type**: Array of strings (optional)
- **Purpose**: Language skills for international opportunities
- **Example**: `["English (Native)", "Spanish (Fluent)", "French (Conversational)"]`

#### interests
- **Type**: Array of strings (optional)
- **Purpose**: Professional interests and passion areas
- **Example**: `["Machine Learning", "Cloud Architecture", "Open Source"]`

## Configuration Best Practices

### Skills Optimization

**Do Include:**
- Current technologies you use professionally
- Frameworks and tools you're proficient with
- Soft skills relevant to your role
- Industry-specific knowledge

**Avoid:**
- Technologies you haven't used in 2+ years
- Skills you're only casually familiar with
- Too many similar variations (e.g., "React", "ReactJS", "React.js")

### Location Strategy

**For Remote Work:**
- Always include "Remote" in preferred_locations
- Consider time zone preferences
- Include major tech hubs even if not local

**For Relocation:**
- Research target markets thoroughly
- Include cities with strong job markets in your field
- Consider cost of living adjustments

### Salary Guidelines

**Research Methods:**
- Use Glassdoor, Levels.fyi, PayScale
- Consider local market variations
- Factor in experience level and company size

**Setting Expectations:**
- Aim for 75th percentile of market rate
- Account for negotiation room
- Consider total compensation packages

## Profile Validation

### Automatic Validation

The system validates your profile for:
- Required field presence
- Proper JSON syntax
- Reasonable value ranges
- Email format validation

### Manual Review Checklist

**Completeness:**
- [ ] All required fields filled
- [ ] Skills list includes 10+ relevant items
- [ ] Experience entries have achievements
- [ ] Contact information is current

**Accuracy:**
- [ ] Salary expectations are market-realistic
- [ ] Skills reflect current capabilities
- [ ] Location preferences are genuinely acceptable
- [ ] Experience timeline is accurate

**Optimization:**
- [ ] Skills use industry-standard terms
- [ ] Achievements are quantifiable where possible
- [ ] Company type matches career goals
- [ ] Profile represents your best professional self

## Common Profile Mistakes

### Under-specification
- Too few skills listed
- Vague role descriptions
- Missing location preferences
- Unrealistic salary expectations

### Over-specification
- Too many irrelevant skills
- Overly narrow location requirements
- Inflated experience claims
- Unrealistic salary demands

### Inconsistencies
- Experience level doesn't match years
- Skills don't align with role
- Salary expectations too far from market
- Location conflicts with remote preferences

## Profile Updates

### When to Update

- **Skill Changes**: After learning new technologies
- **Role Changes**: When switching positions
- **Location Changes**: Moving or changing preferences
- **Market Changes**: Salary adjustments based on market research

### Update Command

```bash
python src/job_seeker/main.py update_profile
```

This command provides interactive guidance for profile updates.

### Version Control

Consider keeping profile versions for different search strategies:

```bash
# Create profile variants
cp knowledge/resume_template.json knowledge/profile_senior.json
cp knowledge/resume_template.json knowledge/profile_lead.json
```

## Privacy and Security

### Data Storage
- All profile data stays on your local machine
- No profile information is sent to external services
- The system only uses your profile for local job matching

### Sensitive Information
- Use a dedicated email for job searching
- Don't include SSN, passport, or other sensitive IDs
- Consider using a Google Voice number for phone

### Backup
- Keep backups of your profile configuration
- Store securely (encrypted if possible)
- Version control important changes

## Troubleshooting

### Profile Not Loading
1. Check JSON syntax with an online validator
2. Ensure all required fields are present
3. Verify file is saved in correct location
4. Check file permissions

### Poor Match Results
1. Review and expand skills list
2. Adjust location preferences
3. Verify salary expectations are realistic
4. Update experience level

### Validation Errors
1. Run the update_profile command for guidance
2. Check field types match requirements
3. Ensure arrays are properly formatted
4. Validate email format

## Next Steps

After configuring your profile:

1. **Test Configuration**: Run `python src/job_seeker/main.py test`
2. **First Search**: Execute your first job search
3. **Review Results**: Analyze match scores and recommendations
4. **Iterate**: Refine profile based on initial results

For more information:
- [Usage Guide](usage.md) - Running job searches
- [Output Files](output-files.md) - Understanding results
- [Troubleshooting](troubleshooting.md) - Common issues