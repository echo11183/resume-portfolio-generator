---
name: resume-to-website
description: Convert a resume PDF into a personal portfolio website. Use when the user wants to generate a website, portfolio, or personal page from their resume or CV (PDF).
---

# Resume to Website

Convert a resume PDF into a portfolio website with a style of your choice.

## Available Templates

Run this to see available templates:

```bash
python generate_website.py
```

Or scan programmatically:

```python
from website_generator import list_templates
for t in list_templates():
    print(f"  {t['id']} ({t['type']})")
```

Ask the user which template they want before generating. Describe each template's visual style to help them choose.

## Workflow

### Step 1: Extract Text from PDF

```python
from pdf_extractor import extract_text_from_pdf
resume_text = extract_text_from_pdf("path/to/resume.pdf")
```

### Step 2: Parse Resume into Structured Data

Read the extracted text and parse it into a JSON object following the schema in `REFERENCE.md`.

Save the parsed data as `resume_data.json`.

### Step 3: Ask User to Choose Template

Present available templates and ask which one they prefer.

### Step 4: Generate Website

```bash
python generate_website.py resume_data.json <template_id> [output_dir]
```

Example:
```bash
python generate_website.py resume_data.json julia my_website
```

The output is a folder containing the website with all assets (CSS, JS, images). Open `my_website/index.html` in a browser to preview.

## Template Structure

Templates live in `templates/`:

- **Single-file** (e.g. `portfolio.html`): Self-contained HTML with inline CSS, no external dependencies
- **Folder-based** (e.g. `julia/`, `aurora/`): Full template with CSS/JS/images, requires the whole folder

Both types use the same Jinja2 variables for dynamic content.

## Adding New Templates

To add a new template:

1. Create a folder in `templates/` (e.g. `templates/my-template/`)
2. Add an `index.html` with Jinja2 variables
3. Include any CSS/JS/images the template needs
4. That's it — it will be auto-detected

## Template Variables

All templates have access to these variables:

| Variable | Type | Description |
|----------|------|-------------|
| `{{ name }}` | string | Full name |
| `{{ title }}` | string | Job title / headline |
| `{{ email }}` | string | Email address |
| `{{ phone }}` | string | Phone number |
| `{{ location }}` | string | City, Country |
| `{{ summary }}` | string | Career summary / bio |
| `{{ year }}` | int | Current year (for footer) |
| `{{ experiences }}` | list | Work experience items |
| `{{ education }}` | list | Education items |
| `{{ skills }}` | list | Skill groups |
| `{{ projects }}` | list | Project items |

Loop syntax:
- `{% for exp in experiences %}` ... `{% endfor %}`
- `{% for edu in education %}` ... `{% endfor %}`
- `{% for group in skills %}` with `group.category`, `group.get('items', [])`
- `{% for proj in projects %}` with `proj.name`, `proj.description`, `proj.technologies`

## Notes

- The skill uses `pypdf` for PDF reading and `jinja2` for HTML generation
- If the resume is in a non-English language, generate the website in the same language
- Folder-based templates may use external CDN (Bootstrap, Google Fonts) — requires internet to view
