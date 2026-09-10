import os
import re
import glob
import html
from viva_data import viva_content

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

    # Attempt to separate data inserts from queries
    # A rough heuristic: look for insertMany([ ... ]) block
    data_block = ""
    queries_block = content
    insert_match = re.search(r'(db\.[a-zA-Z0-9_]+\.insertMany\(\[.*?\]\);?)', content, re.DOTALL)
    if insert_match:
        data_block = insert_match.group(1)
        queries_block = content.replace(data_block, '')

    escaped_data = html.escape(data_block.strip())
    escaped_queries = html.escape(queries_block.strip())

    viva = viva_content.get(f, {"title": title, "concepts": [], "qna": []})

    html_snippet = f"""
    <article>
        <header>
            <h2>Viva Prep: {viva['title']}</h2>
            <p><strong>Source File:</strong> <code>{f}</code></p>
        </header>
    """

    if escaped_data:
        html_snippet += f"""
        <section style="margin-top: 2rem;">
            <h3>Dataset Context</h3>
            <p>The queries below run against this collection structure:</p>
            <pre><code class="language-json">{escaped_data}</code></pre>
        </section>
        """

    html_snippet += """
        <section style="margin-top: 2rem;">
            <h3>Raw Queries</h3>
            <pre><code class="language-mongodb">""" + escaped_queries + """</code></pre>
        </section>
    """

    if viva['concepts']:
        html_snippet += """<section style="margin-top: 2rem;"><h3>Deep Dive Concepts</h3>"""
        for concept in viva['concepts']:
            html_snippet += f"""
            <details style="margin-bottom: 1rem;" open>
                <summary><strong>{concept['name']}</strong></summary>
                <div style="padding-left: 1rem; border-left: 3px solid var(--primary); margin-top: 1rem;">
                    <p><strong>The Plain-English Breakdown:</strong> {concept['breakdown']}</p>
                    <p><strong>Real-World Use Case:</strong> {concept['use_case']}</p>
                    <p><strong>The "Gotcha" (Common Pitfalls):</strong> <mark>{concept['gotcha']}</mark></p>
                    <p><strong>Memorization Hook:</strong> <em>{concept['hook']}</em></p>
                </div>
            </details>
            """
        html_snippet += "</section>"

    if viva['qna']:
        html_snippet += """
        <section style="margin-top: 2rem; background: var(--card-sectionning-background-color); padding: 1.5rem; border-radius: var(--border-radius);">
            <h3>Examiner Q&A Simulator</h3>
            <p><small>Click a question to reveal the answer.</small></p>
        """
        for qna in viva['qna']:
            html_snippet += f"""
            <details style="margin-bottom: 0.5rem;">
                <summary><strong>{qna['q']}</strong></summary>
                <div style="padding: 1rem; background: var(--background-color); margin-top: 0.5rem; border-radius: var(--border-radius);">
                    {qna['a']}
                </div>
            </details>
            """
        html_snippet += "</section>"

    html_snippet += "\n    </article>"

    out_name = f"lesson_{num}.html"
    with open(f"pages/{out_name}", 'w') as out_file:
        out_file.write(html_snippet)

    nav_links.append(f'<li><a href="#" onclick="loadPage(\'{out_name}\'); return false;">{viva["title"]}</a></li>')

# Generate a default homepage snippet
home_snippet = """
<article>
    <header>
        <h2>Welcome to Viva Prep: MongoDB Edition</h2>
        <p>Select a topic from the sidebar to start your active recall session.</p>
        <p>This UI is optimized for exam preparation, separating dataset context from raw queries, highlighting "gotchas", and providing interactive examiner Q&A.</p>
    </header>
</article>
"""
with open("pages/home.html", 'w') as out_file:
    out_file.write(home_snippet)

nav_html = "<ul>\n" + "\n".join(nav_links) + "\n</ul>"
with open("pages/nav.html", 'w') as nav_file:
    nav_file.write(nav_html)

print("Build completed successfully!")