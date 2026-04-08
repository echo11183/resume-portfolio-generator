# 简历转网站 - 参考文档

## JSON Schema

解析后的简历数据应遵循以下结构：

```json
{
  "personal": {
    "name": "张三",
    "title": "高级软件工程师",
    "email": "zhangsan@example.com",
    "phone": "+86 138-1234-5678",
    "location": "北京",
    "summary": "8年经验的资深工程师..."
  },
  "experience": [
    {
      "company": "某科技公司",
      "position": "高级工程师",
      "start_date": "2020-03",
      "end_date": null,
      "description": "负责核心平台服务开发"
    }
  ],
  "education": [
    {
      "school": "清华大学",
      "degree": "硕士",
      "field": "计算机科学",
      "graduation_date": "2018-06",
      "gpa": "3.8"
    }
  ],
  "skills": [
    {
      "category": "编程语言",
      "items": ["Python", "JavaScript", "Go"]
    }
  ],
  "projects": [
    {
      "name": "开源工具",
      "description": "自动化部署的 CLI 工具",
      "technologies": ["Python", "Docker", "Kubernetes"],
      "link": "https://github.com/example/tool"
    }
  ]
}
```

## 字段规则

| 字段 | 类型 | 必填 | 说明 |
|-------|------|----------|-------|
| personal.name | 字符串 | 是 | 姓名 |
| personal.title | 字符串 | 是 | 当前职位或头衔 |
| personal.email | 字符串 | 是 | 主要邮箱 |
| personal.phone | 字符串 | 否 | 电话号码 |
| personal.location | 字符串 | 否 | 城市、国家 |
| personal.summary | 字符串 | 否 | 简要个人简介 |
| experience[].company | 字符串 | 是 | 公司名称 |
| experience[].position | 字符串 | 是 | 职位 |
| experience[].start_date | 字符串 | 是 | 格式：YYYY-MM |
| experience[].end_date | 字符串 | 否 | 格式：YYYY-MM，当前职位填 null |
| experience[].description | 字符串 | 是 | 主要职责 |
| education[].school | 字符串 | 是 | 学校名称 |
| education[].degree | 字符串 | 是 | 如：本科、硕士、博士 |
| education[].field | 字符串 | 是 | 专业 |
| education[].graduation_date | 字符串 | 是 | 格式：YYYY-MM |
| education[].gpa | 字符串 | 否 | GPA（如果有） |
| skills[].category | 字符串 | 是 | 如"前端"、"后端" |
| skills[].items | 字符串数组 | 是 | 技能名称列表 |
| projects[].name | 字符串 | 是 | 项目名称 |
| projects[].description | 字符串 | 是 | 简要描述 |
| projects[].technologies | 字符串数组 | 是 | 使用的技术栈 |
| projects[].link | 字符串 | 否 | 项目链接 |

## 设计自定义

生成的网站使用现代响应式设计，包括：

- 固定导航栏
- 带有姓名、标题的首页横幅
- 关于我 section
- 工作经历时间线
- 技能卡片网格
- 项目作品卡片网格
- 教育背景 section
- 联系 section（邮箱/电话/地址）

如需修改颜色，编辑 `templates/portfolio.html` 中的 CSS 变量：

```css
:root {
    --primary: #2563eb;    /* 主色调 */
    --text: #1f2937;       /* 正文颜色 */
    --text-light: #6b7280; /* 次要文字 */
    --bg: #ffffff;         /* 背景色 */
    --bg-alt: #f9fafb;     /* 交替背景 */
}
```