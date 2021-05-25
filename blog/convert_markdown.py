import markdown

# markdown.markdownFromFile(input='petshop_cfg.md', output='petshop_cfg.html')

with open('blog/petshop_cfg.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text, extensions=['toc', 'fenced_code', 'codehilite'])

#print(html)
with open('public/build/petshop_cfg.html', 'w') as f:
    f.write(html)