# Resume Portfolio Generator

将 PDF 简历转换为个人作品集网站。

## 安装

```bash
pip install -r requirements.txt
```

## 使用

1. 提取 PDF 文本：
```bash
python generate_website.py resume.pdf
```

2. 解析文本为 JSON（参考 reference.md）

3. 生成网站：
```bash
python generate_website.py resume_data.json
```

## 许可证

MIT