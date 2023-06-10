# Create the HTML content with inline styles
# Create the HTML content
html_content = f'''
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        table {{
            border-collapse: collapse;
            border-spacing: 0;
            width: 100%;
            border: 1px solid #ddd;
        }}

        th, td {{
            text-align: left;
            padding: 8px;
        }}

        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <table>
        <caption><h3>DATE - {tdy.strftime("%d/%m/%Y")}</h3></caption>
        <tr>
            <th>Name</th>
            <th>Leetcode Problems</th>
            <th>Codechef Problems</th>
            <th>Codeforces Problems</th>
        </tr>
'''

# Generate the table rows
for coder in coders:
    html_content += '<tr>\n'
    html_content += f'<td>{coder.name}</td>\n'
    html_content += '<td>\n'
    for problem in coder.problems_leetcode:
        html_content += f'<span>{problem.html_str()}</span><br>\n'
    html_content += '</td>\n'
    html_content += '<td>\n'
    for problem in coder.problems_codechef:
        html_content += f'<span>{problem.html_str()}</span><br>\n'
    html_content += '</td>\n'
    html_content += '<td>\n'
    for problem in coder.problems_codeforces:
        html_content += f'<span>{problem.html_str()}</span><br>\n'
    html_content += '</td>\n'
    html_content += '</tr>\n'

html_content += '''
    </table>
</body>
</html>
'''
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)