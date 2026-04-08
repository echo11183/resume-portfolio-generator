# resume-portfolio-generator
简历转网站Skill

将 PDF 简历转换为个人作品集网站。

## 底层原理

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PDF      │───▶│  文本提取   │───▶│  JSON     │───▶│  网站生成  │
│  简历     │    │ (pypdf)   │    │ 解析      │    │ (Jinja2)  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

1. **PDF 提取**: 使用 `pypdf` 库读取 PDF 文件并提取文本
2. **JSON 解析**: 将简历文本解析为结构化 JSON（参考 `reference.md`）
3. **模板渲染**: 使用 Jinja2 模板引擎生成 HTML 网站

## 安装

```bash
pip install -r requirements.txt
```

## 使用

### 方式一：直接生成（已有 JSON 数据）

```bash
python generate_website.py resume_data.json
```

### 方式二：提取 PDF 文本

```bash
python generate_website.py my_resume.pdf
```
输出提取的文本，然后手动解析为 JSON

### 选择模板

```bash
python generate_website.py resume_data.json portfolio
```

可用的模板：
- `portfolio` - 默认现代深色模板

## 如何在 Claude/OpenCode 中使用此 Skill

### 方法一：复制 SKILL.md 到内置 Skills 目录

**Windows:**
```powershell
Copy-Item SKILL.md "$env:USERPROFILE\.claude\skills\resume-to-website\SKILL.md"
```

**macOS/Linux:**
```bash
cp SKILL.md ~/.claude/skills/resume-to-website/SKILL.md
```

### 方法二：在项目目录下直接使用

当用户请求转换简历为网站时，AI 会自动读取项目中的 `SKILL.md` 并按照工作流执行。

## 项目结构

```
├── SKILL.md              # Skill 定义
├── reference.md         # JSON Schema 参考
├── requirements.txt    # 依赖：pypdf, jinja2
├── pdf_extractor.py    # PDF 文本提取
├── website_generator.py  # 网站生成引擎
├── generate_website.py  # CLI 入口
├── templates/
│   └── portfolio.html  # 默认模板
└── images/
    └── avatar.jpg
```

## 模板变量

所有模板可用的变量：

| 变量 | 类型 | 说明 |
|-------|------|------|
| `{{ name }}` | 字符串 | 姓名 |
| `{{ title }}` | 字符串 | 职位 |
| `{{ email }}` | 字符串 | 邮箱 |
| `{{ phone }}` | 字符串 | 电话 |
| `{{ location }}` | 字符串 | 地址 |
| `{{ summary }}` | 字符串 | 个人简介 |
| `{{ experiences }}` | 列表 | 工作经历 |
| `{{ education }}` | 列表 | 教育背景 |
| `{{ skills }}` | 列表 | 技能列表 |
| `{{ projects }}` | 列表 | 项目作品 |

## 许可证

MIT