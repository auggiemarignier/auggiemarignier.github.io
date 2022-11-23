import markdown
from bs4 import BeautifulSoup
import os
import yaml

content_dir = "content"
pubs_dir = os.path.join(content_dir, "publication")
pubs = [d for d in os.listdir(pubs_dir) if d != "_index.md"]
content = []
for p in pubs:
    with open(os.path.join(pubs_dir, p, "index.md"), "r") as f:
        text = f.read()
        text = text[3:-3]  # trim --- at start and end of file
        full = yaml.safe_load(text)
        content.append(
            {k: full[k] for k in ("title", "authors", "date", "publication_short")}
        )
for cont in content:
    print(yaml.safe_dump(cont))
    print("---------------")
