---
name: resume-to-website
description: 将 PDF 简历转换为个人作品集网站。当用户想要从简历或 PDF 生成网站、作品集或个人页面时使用。
---

# 简历转网站

将 PDF 简历转换为个人作品集网站。

## 可用模板

运行以下命令查看可用模板：

```bash
python generate_website.py
```

或通过代码扫描：

```python
from website_generator import list_templates
for t in list_templates():
    print(f"  {t['id']} ({t['type']})")
```

在生成之前询问用户想要哪个模板。描述每个模板的视觉风格以帮助他们选择。

## 工作流程

### 步骤一：从 PDF 提取文本

```python
from pdf_extractor import extract_text_from_pdf
resume_text = extract_text_from_pdf("path/to/resume.pdf")
```

### 步骤二：解析简历为结构化数据

读取提取的文本并按照 `reference.md` 中的 schema 将其解析为 JSON 对象。

将解析后的数据保存为 `resume_data.json`。

### 步骤三：让用户选择模板

展示可用的模板并询问他们更喜欢哪一个。

### 步骤四：生成网站

```bash
python generate_website.py resume_data.json <template_id> [output_dir]
```

示例：
```bash
python generate_website.py resume_data.json portfolio my_website
```

输出是一个包含所有资源（CSS、JS、图片）的文件夹。在浏览器中打开 `my_website/index.html` 预览。

## 模板结构

模板位于 `templates/` 目录：

- **单文件**（如 `portfolio.html`）：自包含 HTML，内联 CSS，无外部依赖
- **文件夹式**（如 `julia/`、`aurora/`）：完整模板，包含 CSS/JS/图片，需要整个文件夹

两种类型使用相同的 Jinja2 变量来处理动态内容。

## 添加新模板

添加新模板：

1. 在 `templates/` 中创建文件夹（如 `templates/my-template/`）
2. 添加包含 Jinja2 变量的 `index.html`
3. 添加模板所需的任何 CSS/JS/图片
4. 完成 — 它会被自动检测到

## 模板变量

所有模板可用的变量：

| 变量 | 类型 | 说明 |
|----------|------|-------------|
| `{{ name }}` | 字符串 | 姓名 |
| `{{ title }}` | 字符串 | 职位 / 头衔 |
| `{{ email }}` | 字符串 | 邮箱地址 |
| `{{ phone }}` | 字符串 | 电话号码 |
| `{{ location }}` | 字符串 | 城市、国家 |
| `{{ summary }}` | 字符串 | 职业简介 |
| `{{ year }}` | 整数 | 当前年份（用于页脚） |
| `{{ experiences }}` | 列表 | 工作经历 |
| `{{ education }}` | 列表 | 教育背景 |
| `{{ skills }}` | 列表 | 技能分组 |
| `{{ projects }}` | 列表 | 项目作品 |

循环语法：
- `{% for exp in experiences %}` ... `{% endfor %}`
- `{% for edu in education %}` ... `{% endfor %}`
- `{% for group in skills %}` 使用 `group.category`、`group.get('items', [])`
- `{% for proj in projects %}` 使用 `proj.name`、`proj.description`、`proj.technologies`

## 注意事项

- 此 Skill 使用 `pypdf` 读取 PDF，使用 `jinja2` 生成 HTML
- 如果简历是非英语语言，使用相同的语言生成网站
- 文件夹式模板可能使用外部 CDN（Bootstrap、Google Fonts）— 需要联网查看