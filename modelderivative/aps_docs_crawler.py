#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys

# ——— CONFIGURATION ———
JSON_URL        = "https://developer.doc.config.autodesk.com/bPlouYTd/viewer_v7.json"
HTML_BASE       = "https://developer.doc.autodesk.com/bPlouYTd/"
OUTPUT_MARKDOWN = "viewer-v7.md"
# ——— END CONFIGURATION ———

def fetch_json(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def collect_leaves(node, leaves):
    """
    Walk the entire tree and collect every leaf node (no "children").
    """
    children = node.get("children") or []
    if not children:
        leaves.append(node)
    else:
        for child in children:
            collect_leaves(child, leaves)

def build_page_url(leaf):
    """
    Prepend HTML_BASE to the leaf's "source" path.
    """
    src = leaf.get("source")
    if not src:
        raise ValueError(f"No source for leaf: {leaf}")
    return HTML_BASE + src

def parse_page(html_text):
    """
    Extract:
      - title = first <h1>
      - full_text = all textual content in <body> (headings, paragraphs, lists)
      - code_blocks = all <pre>... blocks with fencing
    """
    soup = BeautifulSoup(html_text, "html.parser")

    # Title = first <h1>
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else "Untitled"

    # Full text = concatenate all text nodes in <body>, preserving spacing
    body = soup.body or soup
    # Remove scripts/styles
    for tag in body(["script", "style"]):
        tag.decompose()
    # Get text with reasonable spacing
    texts = []
    for elem in body.find_all(
        ["h1","h2","h3","h4","h5","h6","p","li","td","th"]
    ):
        txt = elem.get_text(strip=True)
        if txt:
            texts.append(txt)
    full_text = "\n\n".join(texts)

    # Code blocks = all <pre>
    code_blocks = []
    for pre in soup.find_all("pre"):
        code = pre.find("code") or pre
        text = code.get_text()
        lang = ""
        if code.has_attr("class"):
            for cls in code["class"]:
                if cls.startswith("language-"):
                    lang = cls.split("-", 1)[1]
                    break
        fence = f"```{lang}" if lang else "```"
        code_blocks.append((fence, text))

    return title, full_text, code_blocks

def main():
    try:
        tree = fetch_json(JSON_URL)
    except Exception as e:
        print(f"Error fetching JSON: {e}", file=sys.stderr)
        sys.exit(1)

    leaves = []
    collect_leaves(tree, leaves)
    if not leaves:
        print("No leaf nodes found!", file=sys.stderr)
        sys.exit(1)

    md_parts = []
    for idx, leaf in enumerate(leaves, 1):
        try:
            url = build_page_url(leaf)
        except ValueError as e:
            print(f"Skipping leaf #{idx}: {e}", file=sys.stderr)
            continue

        print(f"[{idx}/{len(leaves)}] Fetching {url}…")
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except Exception as e:
            print(f"  ❌ Failed to download: {e}", file=sys.stderr)
            continue

        title, full_text, blocks = parse_page(resp.text)

        # Assemble markdown
        md_parts.append(f"# {title}\n")
        md_parts.append(f"{full_text}\n")
        for fence, code in blocks:
            md_parts.append(f"{fence}\n{code}\n```\n")
        md_parts.append("\n---\n")

    # Write to file
    with open(OUTPUT_MARKDOWN, "w", encoding="utf-8") as out:
        out.write("\n".join(md_parts))

    print(f"\n✅ Finished. See `{OUTPUT_MARKDOWN}`")

if __name__ == "__main__":
    main()