import markdown
from bs4 import BeautifulSoup
import os
import json

# markdown.markdownFromFile(input='petshop_cfg.md', output='petshop_cfg.html')
script_path = os.path.dirname(os.path.realpath(__file__))

h1s = []

import os
for file in os.listdir(script_path):
    if file.endswith('.md'):
        file_path = os.path.join(script_path, file)

        with open(file_path, 'r') as f:
            text = f.read()
            html = markdown.markdown(text, extensions=['toc', 'fenced_code', 'codehilite'])
            bsh = BeautifulSoup(html, 'html.parser')
            h1s.append({'title': bsh.h1.text, 'date': bsh.time.text, 'file': '/build/' + file.split('.')[0] + '.html'})
            print(bsh.h1.text)

            with open('public/build/' + file.split('.')[0] + '.html', 'w') as f:
                f.write(html)
jsonStr = json.dumps(h1s)

with open('public/build/blog_data.html', 'w') as f:
    f.write(jsonStr)