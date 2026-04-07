"""Generate portfolio website from resume JSON data. Supports multiple templates."""

import os
import shutil
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


def list_templates() -> list:
    """Auto-detect available templates in the templates/ directory."""
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    templates = []
    for name in sorted(os.listdir(template_dir)):
        full = os.path.join(template_dir, name)
        if name.endswith(".html") and os.path.isfile(full):
            templates.append({"id": name.replace(".html", ""), "name": name, "type": "file"})
        elif os.path.isdir(full) and os.path.exists(os.path.join(full, "index.html")):
            templates.append({"id": name, "name": name, "type": "folder"})
    return templates


def copy_images(base_dir: str, output_dir: str) -> str:
    """复制 images 目录到输出目录，返回 avatar 路径"""
    images_src = os.path.join(base_dir, "images")
    images_dst = os.path.join(output_dir, "images")
    
    avatar_path = ""
    
    if os.path.exists(images_src):
        if os.path.exists(images_dst):
            shutil.rmtree(images_dst)
        shutil.copytree(images_src, images_dst)
        # 检查 avatar.jpg 是否存在
        if os.path.exists(os.path.join(images_src, "avatar.jpg")):
            avatar_path = "images/avatar.jpg"
    
    return avatar_path


def generate_website(resume_data: dict, template_id: str | None = None, output_dir: str = "my_website") -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, "templates")

    # Auto-select first template if none specified
    if template_id is None:
        templates = list_templates()
        if not templates:
            raise FileNotFoundError("No templates found in templates/")
        template_id = templates[0]["id"]

    # Determine template type
    folder_path = os.path.join(template_dir, template_id)
    file_path = os.path.join(template_dir, f"{template_id}.html")

    if os.path.isdir(folder_path):
        # Folder-based template: copy folder, then render index.html
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        shutil.copytree(folder_path, output_dir, ignore=shutil.ignore_patterns("*.html"))
        env = Environment(loader=FileSystemLoader(folder_path))
        template = env.get_template("index.html")
        output_path = os.path.join(output_dir, "index.html")
    elif os.path.isfile(file_path):
        # Single-file template: render to output dir as index.html
        os.makedirs(output_dir, exist_ok=True)
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(f"{template_id}.html")
        output_path = os.path.join(output_dir, "index.html")
    else:
        raise FileNotFoundError(f"Template '{template_id}' not found")

    # 复制 images 目录并获取 avatar 路径
    avatar_path = copy_images(base_dir, output_dir)

    p = resume_data.get("personal", {})
    html = template.render(
        name=p.get("name", ""),
        title=p.get("title", ""),
        email=p.get("email", ""),
        phone=p.get("phone", ""),
        location=p.get("location", ""),
        summary=p.get("summary", ""),
        avatar=avatar_path,
        experiences=resume_data.get("experience", []),
        education=resume_data.get("education", []),
        skills=resume_data.get("skills", []),
        projects=resume_data.get("projects", []),
        services=resume_data.get("services", []),
        year=datetime.now().year,
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Available templates:")
        for t in list_templates():
            print(f"  [{t['type']}] {t['id']}")
        print(f"\nUsage:")
        print(f"  python generate_website.py <data.json> [template_id] [output_dir]")
        sys.exit(1)

    json_path = sys.argv[1]
    template_id = sys.argv[2] if len(sys.argv) > 2 else None
    output_dir = sys.argv[3] if len(sys.argv) > 3 else "my_website"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = generate_website(data, template_id, output_dir)
    print(f"Website generated: {result}")
