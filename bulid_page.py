def main():
    # 个人信息配置
    personal_info = {
        "name": "张三",
        "title": "AI Engineer",
        "description": "AI Engineer passionate about MLOps and automation.",
        "skills": ["Python", "TensorFlow", "Git", "CI/CD", "Docker"],
        "projects": [
            {"name": "项目一", "url": "https://github.com/yourusername/project1"},
            {"name": "项目二", "url": "https://github.com/yourusername/project2"}
        ],
        "contact": {
            "github": "https://github.com/yourusername",
            "linkedin": "https://linkedin.com/in/yourprofile"
        }
    }

    # HTML模板
    html_content = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{personal_info['name']} - {personal_info['title']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        h1 {{ color: #333; margin-bottom: 10px; }}
        h2 {{ color: #666; margin-top: 30px; }}
        .skill {{ background: #e7f3ff; padding: 5px 10px; margin: 5px; border-radius: 15px; display: inline-block; }}
        .projects ul {{ list-style-type: none; padding: 0; }}
        .projects li {{ margin: 10px 0; }}
        a {{ color: #007bff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .contact {{ margin-top: 20px; }}
    </style>
</head>
<body>
    <h1>{personal_info['name']}</h1>
    <h2>{personal_info['title']}</h2>
    <p>{personal_info['description']}</p>

    <h2>技能</h2>
    <div class="skills">
"""
    # 添加技能标签
    for skill in personal_info['skills']:
        html_content += f"        <span class='skill'>{skill}</span>\n"

    html_content += """    </div>

    <h2>项目经历</h2>
    <div class="projects">
        <ul>
"""
    # 添加项目链接
    for project in personal_info['projects']:
        html_content += f"            <li><a href='{project['url']}'>{project['name']}</a></li>\n"

    html_content += f"""        </ul>
    </div>

    <h2>联系方式</h2>
    <div class="contact">
        <a href="{personal_info['contact']['github']}">GitHub</a> | 
        <a href="{personal_info['contact']['linkedin']}">LinkedIn</a>
    </div>
</body>
</html>
    """

    # 写入文件
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("index.html generated successfully!")


if __name__ == "__main__":
    main()
