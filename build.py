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

# Generate navigation links
nav_links = []
for f in files:
    num = re.search(r'^(\d+)', f).group(1)
    title = f.replace('.js', '').capitalize()
    viva = viva_content.get(f, {"title": title, "concepts": [], "qna": []})

    # We will assume GitHub Pages might serve this under a subdirectory like /mongo/
    # Using relative paths from the current document location is safer.
    # From root index.html: lesson1/
    # From lesson1/index.html: ../lesson1/

    nav_links.append({
        "num": num,
        "title": viva["title"]
    })

def generate_html_wrapper(title, content_html, active_lesson_num=None, is_root=False):
    base_path = "" if is_root else "../"

    nav_html = "<ul>\n"
    nav_html += f'<li><a href="{base_path}index.html" class="{"active" if active_lesson_num is None else ""}">Home</a></li>\n'
    for link in nav_links:
        active_class = ' class="active" style="font-weight: bold;"' if link["num"] == active_lesson_num else ''
        nav_html += f'<li><a href="{base_path}lesson{link["num"]}/"{active_class}>{link["title"]}</a></li>\n'
    nav_html += "</ul>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - MongoDB Learning Site</title>
    <!-- Pico.css for minimalistic styling -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <!-- Prism.css for syntax highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="{base_path}styles.css">
</head>
<body>
    <main class="container">
        <div class="grid">
            <aside>
                <nav>
                    <h3>Lessons</h3>
                    <div id="nav-container">
                        {nav_html}
                    </div>
                </nav>
            </aside>

            <section id="content-container">
                {content_html}
            </section>
        </div>

        <footer id="footer-container" style="margin-top: 3rem; border-top: 1px solid var(--muted-border-color); padding-top: 1.5rem;">
            <h3>Credits & Resources</h3>
            <p>
                The JavaScript examples and tutorials provided here are credited to my friend, the original author of the repository.
            </p>
            <p>
                <strong>Further Self-Study Resources:</strong>
                <ul>
                    <li><a href="https://www.mongodb.com/docs/manual/" target="_blank">Official MongoDB Manual</a></li>
                    <li><a href="https://www.mongodb.com/docs/drivers/node/current/" target="_blank">MongoDB Node.js Driver Documentation</a></li>
                </ul>
            </p>
        </footer>
    </main>

    <!-- Prism.js for syntax highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"></script>
</body>
</html>"""

# Generate lesson pages
for f in files:
    num = re.search(r'^(\d+)', f).group(1)
    title = f.replace('.js', '').capitalize()

    with open(f, 'r') as file:
        content = file.read()

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

    # Create directory for the lesson
    dir_name = f"lesson{num}"
    os.makedirs(dir_name, exist_ok=True)

    full_html = generate_html_wrapper(viva['title'], html_snippet, active_lesson_num=num, is_root=False)
    with open(f"{dir_name}/index.html", 'w') as out_file:
        out_file.write(full_html)

# Generate root index.html (home page)
home_snippet = """
<article>
    <header>
        <h2>Welcome to Viva Prep: MongoDB Edition</h2>
        <p>Select a topic from the sidebar to start your active recall session.</p>
        <p>This UI is optimized for exam preparation, separating dataset context from raw queries, highlighting "gotchas", and providing interactive examiner Q&A.</p>
    </header>
</article>
"""
home_html = generate_html_wrapper("Home", home_snippet, active_lesson_num=None, is_root=True)
with open("index.html", 'w') as out_file:
    out_file.write(home_html)

print("Build completed successfully!")