import os
import re
import glob
import html

# Get all target js files
files = glob.glob('*.js')
files = [f for f in files if re.match(r'^\d+', f)]

# Sort by the leading number
files.sort(key=lambda x: int(re.search(r'^(\d+)', x).group(1)))

nav_links = []

for f in files:
    num = re.search(r'^(\d+)', f).group(1)
    title = f.replace('.js', '').capitalize()

    with open(f, 'r') as file:
        content = file.read()

    escaped_content = html.escape(content)

    # Simple heuristic for mocked output
    mocked_output = '''[
  {
    "_id": "60d5ec49f1b2c8b1f8e4e1a1",
    "acknowledged": true,
    "message": "Query executed successfully"
  }
]'''
    if 'aggregate' in content.lower():
        mocked_output = '''[
  {
    "_id": "exampleCategory",
    "totalCount": 42,
    "average": 100.5
  }
]'''
    elif 'insert' in content.lower():
        mocked_output = '''{
  "acknowledged": true,
  "insertedId": "60d5ec49f1b2c8b1f8e4e1a1"
}'''

    html_snippet = f"""
    <article>
        <header>
            <h2>Lesson: {title}</h2>
            <p><strong>Core Concept:</strong> This section covers concepts demonstrated in <code>{f}</code>.</p>
        </header>

        <section>
            <h3>Explanation</h3>
            <p>The code below illustrates various MongoDB concepts, commands, and queries. Pay attention to the comments within the code for specific details on what each operation accomplishes.</p>
        </section>

        <section>
            <h3>Original JavaScript Code</h3>
            <pre><code class="language-javascript">{escaped_content}</code></pre>
        </section>

        <section>
            <h3>Mocked Expected JSON Output</h3>
            <pre><code class="language-json">{mocked_output.strip()}</code></pre>
        </section>
    </article>
    """

    out_name = f"lesson_{num}.html"
    with open(f"pages/{out_name}", 'w') as out_file:
        out_file.write(html_snippet)

    nav_links.append(f'<li><a href="#" onclick="loadPage(\'{out_name}\'); return false;">{title}</a></li>')

# Generate a default homepage snippet
home_snippet = """
<article>
    <header>
        <h2>Welcome to MongoDB Learning</h2>
        <p>Select a lesson from the sidebar to view the MongoDB concepts and queries.</p>
    </header>
</article>
"""
with open("pages/home.html", 'w') as out_file:
    out_file.write(home_snippet)

nav_html = "<ul>\n" + "\n".join(nav_links) + "\n</ul>"
with open("pages/nav.html", 'w') as nav_file:
    nav_file.write(nav_html)

print("Build completed successfully!")
