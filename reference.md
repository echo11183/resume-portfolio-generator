# Resume to Website - Reference

## JSON Schema

The parsed resume data should follow this structure:

```json
{
  "personal": {
    "name": "John Smith",
    "title": "Senior Software Engineer",
    "email": "john@example.com",
    "phone": "+1-234-567-8900",
    "location": "San Francisco, CA",
    "summary": "Experienced engineer with 8+ years..."
  },
  "experience": [
    {
      "company": "Tech Corp",
      "position": "Senior Engineer",
      "start_date": "2020-03",
      "end_date": null,
      "description": "Led development of core platform services"
    }
  ],
  "education": [
    {
      "school": "MIT",
      "degree": "B.S.",
      "field": "Computer Science",
      "graduation_date": "2016-05",
      "gpa": "3.9"
    }
  ],
  "skills": [
    {
      "category": "Languages",
      "items": ["Python", "JavaScript", "Go"]
    }
  ],
  "projects": [
    {
      "name": "Open Source Tool",
      "description": "A CLI tool for automating deployments",
      "technologies": ["Python", "Docker", "Kubernetes"],
      "link": "https://github.com/example/tool"
    }
  ]
}
```

## Field Rules

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| personal.name | string | Yes | Full name |
| personal.title | string | Yes | Current role or headline |
| personal.email | string | Yes | Primary email |
| personal.phone | string | No | Phone number |
| personal.location | string | No | City, Country |
| personal.summary | string | No | Brief bio / career summary |
| experience[].company | string | Yes | Company name |
| experience[].position | string | Yes | Job title |
| experience[].start_date | string | Yes | Format: YYYY-MM |
| experience[].end_date | string | No | Format: YYYY-MM, null if current |
| experience[].description | string | Yes | Key responsibilities |
| education[].school | string | Yes | Institution name |
| education[].degree | string | Yes | e.g. B.S., M.S., Ph.D. |
| education[].field | string | Yes | Major / field of study |
| education[].graduation_date | string | Yes | Format: YYYY-MM |
| education[].gpa | string | No | GPA if available |
| skills[].category | string | Yes | e.g. "Frontend", "Backend" |
| skills[].items | string[] | Yes | List of skill names |
| projects[].name | string | Yes | Project name |
| projects[].description | string | Yes | Brief description |
| projects[].technologies | string[] | Yes | Tech stack used |
| projects[].link | string | No | URL to project |

## Design Customization

The generated website uses a modern, responsive design with:

- Sticky navigation bar
- Hero section with name, title, and CTA
- About section
- Experience timeline
- Skills grid cards
- Projects grid cards
- Education section
- Contact section with email/phone/location

To modify colors, edit CSS variables in `templates/portfolio.html`:

```css
:root {
    --primary: #2563eb;    /* Main accent color */
    --text: #1f2937;       /* Body text */
    --text-light: #6b7280; /* Secondary text */
    --bg: #ffffff;         /* Background */
    --bg-alt: #f9fafb;     /* Alternate section background */
}
```
