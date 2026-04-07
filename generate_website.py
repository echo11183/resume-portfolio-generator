"""CLI entry point: extract PDF and generate website with template selection."""

import json
import sys
from pdf_extractor import extract_text_from_pdf
from website_generator import generate_website, list_templates


def main():
    if len(sys.argv) < 2:
        print("Available templates:")
        for t in list_templates():
            print(f"  [{t['type']}] {t['id']}")
        print(f"\nUsage:")
        print(f"  python generate_website.py <resume.pdf>                # Extract text for Claude to parse")
        print(f"  python generate_website.py <data.json> [template] [output_dir]")
        sys.exit(1)

    input_path = sys.argv[1]

    if input_path.lower().endswith(".pdf"):
        print(f"Extracting text from: {input_path}")
        text = extract_text_from_pdf(input_path)
        print(f"\n{'='*60}")
        print("EXTRACTED RESUME TEXT (give this to Claude to parse):")
        print(f"{'='*60}\n")
        print(text)
        print(f"\n{'='*60}")
        print("Next: Ask Claude to parse this text and save as JSON,")
        print("then run: python generate_website.py resume_data.json [template_id]")
    elif input_path.lower().endswith(".json"):
        template_id = sys.argv[2] if len(sys.argv) > 2 else None
        output_dir = sys.argv[3] if len(sys.argv) > 3 else "my_website"
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        result = generate_website(data, template_id, output_dir)
        print(f"Website generated: {result}")
    else:
        print("Unsupported file type. Use .pdf or .json")
        sys.exit(1)


if __name__ == "__main__":
    main()
