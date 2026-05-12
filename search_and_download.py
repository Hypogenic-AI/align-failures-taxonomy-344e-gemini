import arxiv
import requests
import os
import json

def search_arxiv(query, max_results=10):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = []
    for result in search.results():
        results.append({
            'title': result.title,
            'authors': [a.name for a in result.authors],
            'year': result.published.year,
            'summary': result.summary,
            'pdf_url': result.pdf_url,
            'entry_id': result.entry_id.split('/')[-1]
        })
    return results

def download_pdf(url, filename):
    if os.path.exists(filename):
        print(f"Skipping {filename}, already exists.")
        return True
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
            return True
        else:
            print(f"Failed to download {url}, status: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

queries = [
    "alignment failure AI automated research",
    "AI safety automated scientist",
    "scientific research misconduct AI",
    "omitting negative findings AI science",
    "AI-driven discovery alignment failures"
]

all_results = []
os.makedirs('papers', exist_ok=True)

for q in queries:
    print(f"Searching for: {q}")
    results = search_arxiv(q, max_results=5)
    all_results.extend(results)

# Deduplicate
unique_results = {r['entry_id']: r for r in all_results}.values()

print(f"Found {len(unique_results)} unique papers.")

with open('papers/metadata.json', 'w') as f:
    json.dump(list(unique_results), f, indent=2)

for r in unique_results:
    title_slug = "".join([c if c.isalnum() else "_" for c in r['title'][:50]])
    filename = f"papers/{r['entry_id']}_{title_slug}.pdf"
    download_pdf(r['pdf_url'], filename)

print("Done.")
EOF
