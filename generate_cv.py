import os
import yaml
from dateutil import parser
import warnings


class SiteReader:
    def __init__(self, content_dir):
        self.content_dir = content_dir
        self.pubs_dir = os.path.join(self.content_dir, "publication")
        self.content = {"publications": [], "talks": [], "codes": []}
        self._find_pages()

    def get_publications(self):
        pages = self._get_relevant_pages("publication")
        if not pages:
            warnings.warn("No publications found")
            return
        for page in pages:
            full = self._read_indexmd(page)
            full["year"] = str((parser.parse(full["date"])).year)
            self.content["publications"].append(
                {k: full[k] for k in ("title", "authors", "year", "publication_short")}
            )

    def _find_pages(self):
        self.pages = []
        for root, _, files in os.walk(self.content_dir):
            try:
                page_type = root.split(os.sep)[1]
            except IndexError:
                continue
            else:
                if page_type in ("publication", "talk", "code"):
                    for file in files:
                        if file == "index.md":
                            self.pages.append(os.path.join(root, file))

    def _get_relevant_pages(self, page_type):
        return [page for page in self.pages if page.split(os.sep)[1] == page_type]

    @staticmethod
    def _read_indexmd(indexmd):
        with open(indexmd, "r") as f:
            text = f.read()
            text = text[3:-3]  # trim --- at start and end of file
            return yaml.safe_load(text)


if __name__ == "__main__":
    content_dir = "content"
    CV = os.path.join(content_dir, "cv", "_index.md")
    reader = SiteReader(content_dir)
    reader.get_publications()

    with open(CV, "w") as cv:
        cv.write("# Dr Augustin Marignier CV \n\n---\n\n")
        cv.write(("## Publications\n\n"))
        for cont in sorted(
            reader.content["publications"], key=lambda d: d["year"], reverse=True
        ):
            authors = ", ".join(cont["authors"])
            title = cont["title"]
            journal = cont["publication_short"]
            year = cont["year"]
            cv.write(f"{authors} ({year}). {title}. {journal}  \n\n")
