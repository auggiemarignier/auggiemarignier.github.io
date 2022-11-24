import markdown
from bs4 import BeautifulSoup
import os
import yaml
from dateutil import parser

content_dir = "content"
pubs_dir = os.path.join(content_dir, "publication")
pubs = [d for d in os.listdir(pubs_dir) if d != "_index.md"]
content = []
for p in pubs:
    with open(os.path.join(pubs_dir, p, "index.md"), "r") as f:
        text = f.read()
        text = text[3:-3]  # trim --- at start and end of file
        full = yaml.safe_load(text)
        full["year"] = str((parser.parse(full["date"])).year)
        content.append(
            {k: full[k] for k in ("title", "authors", "year", "publication_short")}
        )
for cont in sorted(content, key=lambda d: d["year"], reverse=True):
    authors = ", ".join(cont["authors"])
    title = cont["title"]
    journal = cont["publication_short"]
    year = cont["year"]
    print(f"{authors} ({year}). {title}. {journal}")
    print("---------------")
