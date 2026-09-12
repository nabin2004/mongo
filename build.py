import os
import re
import glob
import html
import json
from viva_data import viva_content, slides_data

# Map lessons to related slide decks
lesson_to_slides = {}
for s in slides_data:
    for rl in s.get("related_lessons", []):
        num = rl["num"]
        if num not in lesson_to_slides:
            lesson_to_slides[num] = []
        lesson_to_slides[num].append(s)

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

    nav_links.append({
        "num": num,
        "title": viva["title"]
    })

def generate_html_wrapper(title, content_html, active_lesson_num=None, is_root=False, is_slides=False):
    base_path = "" if is_root else "../"
    slides_path = f"{base_path}slides/"

    nav_html = "<ul>\n"
    home_active = ' class="active"' if (active_lesson_num is None and not is_slides) else ''
    nav_html += f'<li><a href="{base_path}index.html"{home_active}><span>Home</span></a></li>\n'

    slides_active = ' class="active"' if is_slides else ''
    nav_html += f'<li><a href="{slides_path}"{slides_active}><span>Study Slides &amp; Playbooks</span> <span class="nav-badge">8</span></a></li>\n'
    nav_html += "</ul>\n"

    nav_html += '<div class="nav-section-heading">Hands-on Lessons</div>\n<ul>\n'
    for link in nav_links:
        active_class = ' class="active"' if link["num"] == active_lesson_num else ''
        nav_html += f'<li><a href="{base_path}lesson{link["num"]}/"{active_class}><span><span style="opacity: 0.55; margin-right: 0.35rem; font-size: 0.82rem;">#{link["num"]}</span>{link["title"]}</span></a></li>\n'
    nav_html += "</ul>"

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - MongoDB Learning &amp; Viva Prep</title>
    <!-- Prevent theme flash -->
    <script>
        (function() {{
            const savedTheme = localStorage.getItem('theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
        }})();
    </script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Pico.css for minimalistic styling -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <!-- Prism.css for syntax highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="{base_path}styles.css?v=20260912_v6">
</head>
<body>
    <!-- Floating expand button when sidebar is collapsed -->
    <button id="floating-sidebar-toggle" type="button" onclick="toggleSidebar()" title="Expand Sidebar">
        <span>☰</span>
        <span>Navigation</span>
    </button>

    <main class="container">
        <div class="grid">
            <aside id="main-sidebar">
                <div class="sidebar-header-bar">
                    <a href="{base_path}index.html" class="brand-badge">
                        <span class="icon">🍃</span>
                        <span>MongoViva</span>
                    </a>
                    <div class="sidebar-action-btns">
                        <button class="icon-btn" id="theme-toggle-btn" type="button" onclick="toggleTheme()" title="Toggle Dark/Light Mode">🌙</button>
                        <button class="icon-btn" id="collapse-sidebar-btn" type="button" onclick="toggleSidebar()" title="Collapse Sidebar">◀</button>
                    </div>
                </div>

                <nav>
                    <h3>Navigation</h3>
                    <div id="nav-container">
                        {nav_html}
                    </div>
                </nav>
            </aside>

            <section id="content-container">
                {content_html}
            </section>
        </div>

        <footer id="footer-container">
            <h3>Credits &amp; Self-Study Resources</h3>
            <p>
                The JavaScript examples and tutorials are credited to the original repository author. Presentation slide decks and viva questions are curated for active recall and exam preparation.
            </p>
            <p>
                <strong>Quick Links:</strong>
                <ul>
                    <li><a href="{slides_path}">Study Slides &amp; Playbooks Hub</a></li>
                    <li><a href="https://www.mongodb.com/docs/manual/" target="_blank" rel="noopener">Official MongoDB Documentation</a></li>
                    <li><a href="https://www.mongodb.com/docs/drivers/node/current/" target="_blank" rel="noopener">MongoDB Node.js Driver Guide</a></li>
                </ul>
            </p>
        </footer>
    </main>

    <!-- Prism.js for syntax highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"></script>
    <script>
        // Copy code helper
        function copyCode(btn) {{
            const wrapper = btn.closest('.code-wrapper');
            const codeEl = wrapper ? wrapper.querySelector('code') : null;
            if (codeEl) {{
                navigator.clipboard.writeText(codeEl.innerText).then(() => {{
                    const orig = btn.innerText;
                    btn.innerText = '✓ Copied';
                    btn.style.color = 'var(--primary)';
                    btn.style.borderColor = 'var(--primary)';
                    setTimeout(() => {{
                        btn.innerText = orig;
                        btn.style.color = '';
                        btn.style.borderColor = '';
                    }}, 2000);
                }}).catch(() => {{
                    btn.innerText = 'Error';
                }});
            }}
        }}

        // Theme toggle logic
        function toggleTheme() {{
            const current = document.documentElement.getAttribute('data-theme') || 'dark';
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
            updateThemeButton(next);
        }}

        function updateThemeButton(theme) {{
            const btn = document.getElementById('theme-toggle-btn');
            if (btn) {{
                btn.textContent = theme === 'dark' ? '🌙' : '☀️';
            }}
        }}

        // Collapsible sidebar logic
        function toggleSidebar() {{
            document.body.classList.toggle('sidebar-collapsed');
            const isCollapsed = document.body.classList.contains('sidebar-collapsed');
            localStorage.setItem('sidebar_collapsed', isCollapsed);
        }}

        // Initialize saved preferences
        (function() {{
            const savedTheme = localStorage.getItem('theme') || 'dark';
            updateThemeButton(savedTheme);

            const savedSidebar = localStorage.getItem('sidebar_collapsed');
            // On mobile (<= 768px), default to collapsed unless explicitly set to false
            if (savedSidebar === 'true' || (window.innerWidth <= 768 && savedSidebar !== 'false')) {{
                document.body.classList.add('sidebar-collapsed');
            }}
        }})();

        // Close mobile drawer when tapping outside
        document.addEventListener('click', function(e) {{
            if (window.innerWidth <= 768 && !document.body.classList.contains('sidebar-collapsed')) {{
                const sidebar = document.getElementById('main-sidebar');
                const toggleBtn = document.getElementById('floating-sidebar-toggle');
                if (sidebar && !sidebar.contains(e.target) && toggleBtn && !toggleBtn.contains(e.target)) {{
                    toggleSidebar();
                }}
            }}
        }});
    </script>
</body>
</html>"""

# Generate lesson pages
for f in files:
    num = re.search(r'^(\d+)', f).group(1)
    title = f.replace('.js', '').capitalize()

    with open(f, 'r', encoding='utf-8') as file:
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
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                <span class="nav-badge">Lesson {num}</span>
                <span style="font-size: 0.82rem; color: var(--muted-color); font-family: var(--font-mono);"><code>{f}</code></span>
            </div>
            <h2>Viva Prep: {viva['title']}</h2>
            <p>Review the collection schema, explore targeted queries, understand key gotchas, and test yourself with examiner questions.</p>
        </header>
    """

    # Related slides banner if available
    if num in lesson_to_slides:
        for slide in lesson_to_slides[num]:
            html_snippet += f"""
        <div class="lesson-slide-banner">
            <div class="banner-info">
                <div class="banner-icon">{slide.get('icon', '📑')}</div>
                <div class="banner-text">
                    <strong>Recommended Slide Deck: {html.escape(slide['title'])}</strong>
                    <span>Visual diagrams, syntax tables &amp; reference cheat sheet ({slide['size']})</span>
                </div>
            </div>
            <div class="banner-actions">
                <a href="../slides/{slide['filename']}" target="_blank" role="button">↗ Open Slide Deck</a>
                <a href="../slides/" role="button" class="secondary outline">All Decks</a>
            </div>
        </div>
            """

    if escaped_data:
        html_snippet += f"""
        <section>
            <h3>Dataset Context</h3>
            <p style="font-size: 0.9rem; color: var(--muted-color); margin-bottom: 0.6rem;">The queries below run against this collection structure and sample documents:</p>
            <div class="code-wrapper">
                <div class="code-header">
                    <span>JSON DATASET</span>
                    <button class="copy-code-btn" type="button" onclick="copyCode(this)">Copy</button>
                </div>
                <pre><code class="language-json">{escaped_data}</code></pre>
            </div>
        </section>
        """

    html_snippet += f"""
        <section>
            <h3>Raw Queries &amp; Operations</h3>
            <p style="font-size: 0.9rem; color: var(--muted-color); margin-bottom: 0.6rem;">Key query execution patterns demonstrated in this lesson:</p>
            <div class="code-wrapper">
                <div class="code-header">
                    <span>JAVASCRIPT / MONGODB SHELL</span>
                    <button class="copy-code-btn" type="button" onclick="copyCode(this)">Copy</button>
                </div>
                <pre><code class="language-javascript">{escaped_queries}</code></pre>
            </div>
        </section>
    """

    if viva['concepts']:
        html_snippet += """<section><h3>Deep Dive Concepts &amp; Mechanics</h3>"""
        for concept in viva['concepts']:
            html_snippet += f"""
            <details open>
                <summary><strong>{concept['name']}</strong></summary>
                <div class="concept-body">
                    <div class="concept-field">
                        <strong>The Plain-English Breakdown:</strong>
                        <span>{concept['breakdown']}</span>
                    </div>
                    <div class="concept-field">
                        <strong>Real-World Use Case:</strong>
                        <span>{concept['use_case']}</span>
                    </div>
                    <div class="callout-box gotcha">
                        <strong>⚠️ The "Gotcha":</strong>
                        <span>{concept['gotcha']}</span>
                    </div>
                    <div class="callout-box hook">
                        <strong>💡 Memorization Hook:</strong>
                        <span>{concept['hook']}</span>
                    </div>
                </div>
            </details>
            """
        html_snippet += "</section>"

    if viva['qna']:
        qna_items = ""
        for qna in viva['qna']:
            qna_items += f"""
            <details class="qna-details">
                <summary><strong>{qna['q']}</strong></summary>
                <div class="qna-answer">
                    {qna['a']}
                </div>
            </details>
            """

        html_snippet += f"""
        <section class="qna-container">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
                <h3 style="margin: 0; font-size: 1.15rem;">Examiner Q&amp;A Simulator</h3>
                <span style="font-size: 0.78rem; color: var(--primary); font-weight: 600;">ACTIVE RECALL</span>
            </div>
            <p style="font-size: 0.88rem; color: var(--muted-color); margin-bottom: 1.25rem;">Click any question below to test your recall and reveal the model examiner answer.</p>
            {qna_items}
        </section>
        """

    html_snippet += "\n    </article>"

    # Create directory for the lesson
    dir_name = f"lesson{num}"
    os.makedirs(dir_name, exist_ok=True)

    full_html = generate_html_wrapper(viva['title'], html_snippet, active_lesson_num=num, is_root=False)
    with open(f"{dir_name}/index.html", 'w', encoding='utf-8') as out_file:
        out_file.write(full_html)

# Generate slides/index.html (Clean Slides Hub & Catalog)
slides_dir = "slides"
os.makedirs(slides_dir, exist_ok=True)

catalog_cards_html = ""

# Compute categories
categories = ["All"]
for s in slides_data:
    cat = s.get("category", "General")
    if cat not in categories:
        categories.append(cat)

category_tabs_html = ""
for cat in categories:
    count = len(slides_data) if cat == "All" else len([s for s in slides_data if s.get("category") == cat])
    is_active = ' active' if cat == "All" else ''
    category_tabs_html += f'<button type="button" class="category-tab{is_active}" data-cat="{html.escape(cat)}" onclick="filterByCategory(\'{html.escape(cat)}\')">{cat} ({count})</button>\n'

for i, s in enumerate(slides_data):
    icon = s.get("icon", "📑")
    cat = s.get("category", "General")
    deck_no = s.get("deck_number", i + 1)
    
    # Chips for topics
    chips_html = "".join([f'<span class="topic-chip">{html.escape(t)}</span>' for t in s["topics"]])

    # Highlights list
    highlights_html = ""
    if s.get("highlights"):
        highlights_items = "".join([f'<li>{html.escape(h)}</li>' for h in s["highlights"]])
        highlights_html = f'<ul class="card-highlights-list">{highlights_items}</ul>'

    # Related lessons links
    related_html = ""
    if s.get("related_lessons"):
        lesson_links = [f'<a href="../lesson{rl["num"]}/" onclick="event.stopPropagation()">Lesson {rl["num"]}</a>' for rl in s["related_lessons"]]
        related_html = f'<div class="card-related-lessons"><strong>Related Lessons:</strong> {" · ".join(lesson_links)}</div>'

    catalog_cards_html += f"""
    <div class="slide-deck-card" id="card-{s['id']}" data-cat="{html.escape(cat)}" onclick="window.open('{s['filename']}', '_blank')">
        <div>
            <div class="card-top-header">
                <div class="card-title-combo">
                    <span class="card-icon">{icon}</span>
                    <div>
                        <h4>{html.escape(s['title'])}</h4>
                        <div style="display: flex; gap: 0.4rem; align-items: center; margin-top: 0.25rem;">
                            <span class="badge-tag">Deck #{deck_no}</span>
                            <span class="badge-tag badge-blue">{cat}</span>
                        </div>
                    </div>
                </div>
                <span class="nav-badge" style="margin: 0; white-space: nowrap;">{s['size']}</span>
            </div>
            <p class="card-description">{html.escape(s['description'])}</p>
            {highlights_html}
            <div class="slide-topics-list">
                {chips_html}
            </div>
            {related_html}
        </div>
        <div class="slide-card-footer">
            <span class="size-tag">{icon} Presentation ({s['size']})</span>
            <div class="slide-card-actions">
                <a href="{s['filename']}" target="_blank" role="button" onclick="event.stopPropagation()">↗ Open Slide Deck</a>
                <a href="{s['filename']}" download role="button" class="secondary outline" onclick="event.stopPropagation()" title="Download PDF">⬇ Download</a>
            </div>
        </div>
    </div>
    """

slides_content_html = f"""
<article>
    <header style="margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
            <span class="nav-badge">8 Playbook Decks</span>
            <span style="font-size: 0.82rem; color: var(--muted-color);">Full-Screen Browser Presentations</span>
        </div>
        <h2>Study Slides &amp; Visual Playbooks</h2>
        <p>Curated revision slide decks and visual cheat sheets. Click on any card below to open the complete presentation in a new tab, or download for offline revision.</p>
    </header>

    <!-- Category Filter Tabs -->
    <div class="category-filter-bar" id="category-filter-strip">
        {category_tabs_html}
    </div>

    <section>
        <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem;">
            <h3 style="margin: 0;">All Presentation Decks</h3>
            <span style="font-size: 0.85rem; color: var(--muted-color);" id="catalog-count-label">{len(slides_data)} Decks Available</span>
        </div>
        <div class="slides-catalog-grid" id="slides-catalog-grid">
            {catalog_cards_html}
        </div>
    </section>
</article>

<script>
    function filterByCategory(category) {{
        // Update active tab styling
        document.querySelectorAll('.category-tab').forEach(tab => {{
            if (tab.getAttribute('data-cat') === category) {{
                tab.classList.add('active');
            }} else {{
                tab.classList.remove('active');
            }}
        }});

        // Filter catalog cards
        let visibleCount = 0;
        document.querySelectorAll('.slide-deck-card').forEach(card => {{
            const cardCat = card.getAttribute('data-cat');
            if (category === 'All' || cardCat === category) {{
                card.style.display = 'flex';
                visibleCount++;
            }} else {{
                card.style.display = 'none';
            }}
        }});

        const countLabel = document.getElementById('catalog-count-label');
        if (countLabel) {{
            countLabel.textContent = `${{visibleCount}} Decks (${{category}})`;
        }}
    }}
</script>
"""

slides_full_html = generate_html_wrapper("Study Slides & Playbooks", slides_content_html, active_lesson_num=None, is_root=False, is_slides=True)
with open("slides/index.html", 'w', encoding='utf-8') as out_file:
    out_file.write(slides_full_html)

# Generate root index.html (home page with featured slides showcase)
home_cards_html = ""
for s in slides_data[:4]:
    icon = s.get("icon", "📑")
    cat = s.get("category", "General")
    home_cards_html += f"""
    <div class="slide-deck-card" onclick="window.open('slides/{s['filename']}', '_blank')">
        <div>
            <div class="card-top-header">
                <div class="card-title-combo">
                    <span class="card-icon">{icon}</span>
                    <div>
                        <h4>{html.escape(s['title'])}</h4>
                        <span class="badge-tag" style="margin-top: 0.2rem; display: inline-block;">{cat}</span>
                    </div>
                </div>
                <span class="nav-badge" style="margin: 0;">{s['size']}</span>
            </div>
            <p class="card-description" style="margin-top: 0.5rem;">{html.escape(s['description'])}</p>
        </div>
        <div class="slide-card-footer">
            <span class="size-tag">{icon} Presentation ({s['size']})</span>
            <div class="slide-card-actions">
                <a href="slides/{s['filename']}" target="_blank" role="button" onclick="event.stopPropagation()">↗ Open Slide Deck</a>
            </div>
        </div>
    </div>
    """

home_snippet = f"""
<article>
    <div class="hero-card">
        <span class="hero-pill">⚡ MongoDB Viva &amp; Exam Preparation Hub</span>
        <h1 class="hero-title">Master MongoDB Through Active Recall &amp; Visual Playbooks</h1>
        <p class="hero-subtitle">
            A clean, minimal, distraction-free learning site crafted for fast revision, viva preparation, and deep conceptual understanding. Explore real queries, memorize key gotchas, and study comprehensive slide playbooks.
        </p>
        <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
            <a href="lesson1/" role="button">Start Lesson 1: Basic Structure &amp; CRUD &rarr;</a>
            <a href="slides/" role="button" class="secondary outline">Browse All 8 Slide Decks</a>
        </div>
        <div class="hero-stats-row">
            <div class="stat-item">
                <span class="stat-value">13</span>
                <span class="stat-label">Hands-on Lessons</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">8</span>
                <span class="stat-label">Visual PDF Decks</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">30+</span>
                <span class="stat-label">Examiner Q&amp;A Gotchas</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">100%</span>
                <span class="stat-label">Offline Accessible</span>
            </div>
        </div>
    </div>

    <section style="margin-top: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
            <div>
                <h3 style="margin: 0;">Featured Study Slides &amp; Playbooks</h3>
                <p style="margin: 0.25rem 0 0 0; font-size: 0.88rem; color: var(--muted-color);">Visual summaries and architectural cheat sheets for fast reference.</p>
            </div>
            <a href="slides/" style="font-size: 0.9rem; font-weight: 600;">View All 8 Slide Decks &rarr;</a>
        </div>
        <div class="slides-catalog-grid">
            {home_cards_html}
        </div>
    </section>
</article>
"""

home_html = generate_html_wrapper("Home", home_snippet, active_lesson_num=None, is_root=True, is_slides=False)
with open("index.html", 'w', encoding='utf-8') as out_file:
    out_file.write(home_html)

print("Build completed successfully: Clean slides catalog with direct new tab opening!")