import os
import yaml
from dateutil import parser
import warnings


class SiteReader:
    def __init__(self, content_dir):
        self.content_dir = content_dir
        self.pubs_dir = os.path.join(self.content_dir, "publication")
        self.content = {"publications": [], "talks": [], "codes": [], "contact": {}}
        self._find_pages()

    def get_publications(self):
        pages = self._get_relevant_pages("publication")
        if not pages:
            warnings.warn("No publications found")
            return
        for page in pages:
            full = self._read_indexmd(page)
            d = {k: full[k] for k in ("title", "authors", "date", "publication_short")}
            for i, author in enumerate(d["authors"]):
                if "Marignier" in author:
                    d["authors"][i] = f"**{d['authors'][i]}**"
            d["date"] = parser.parse(d["date"])
            self.content["publications"].append(d)

    def get_talks(self):
        pages = self._get_relevant_pages("talk")
        if not pages:
            warnings.warn("No talks found")
            return
        for page in pages:
            full = self._read_indexmd(page)
            is_talk = False
            for link in full["links"]:
                if link and link["name"] in ("Slides",):
                    is_talk = True
                    break
            if is_talk:
                d = {k: full[k] for k in ("title", "event", "date")}
                d["date"] = parser.parse(d["date"])
                self.content["talks"].append(d)

    def get_contact(self):
        params_file = os.path.join(
            self.content_dir, "..", "config", "_default", "params.yaml"
        )
        with open(params_file, "r") as f:
            params = yaml.safe_load(f)
        self.content["contact"]["email"] = params["email"]
        self.content["contact"]["address"] = params["address"]
        if self.content["contact"]["address"]["country_code"]:
            del self.content["contact"]["address"]["country"]

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


def write_pubs(cv, reader):
    for cont in sorted(
        reader.content["publications"], key=lambda d: d["date"], reverse=True
    ):
        authors = ", ".join(cont["authors"])
        title = cont["title"]
        journal = cont["publication_short"]
        year = cont["date"].strftime("%Y")
        cv.write(f"* {authors} ({year}). {title}. {journal}\n")


def write_talks(cv, reader):
    for cont in sorted(reader.content["talks"], key=lambda d: d["date"]):
        title = cont["title"]
        event = cont["event"]
        date = cont["date"].strftime("%d/%m/%y")
        cv.write(f"* {title}  \n*{event}*. {date}\n")


def write_education(cv):
    cv.write("2022 &emsp; PhD Data Intensive Science, University College London  \n")
    cv.write(
        "&emsp;&emsp;&emsp;&ensp; *From Dark Matter to the Earth's Deep Interior: There and Back Again*  \n"
    )
    cv.write(
        "&emsp;&emsp;&emsp;&ensp; Supervised by Prof Ana Ferreira and Prof Thomas Kitching  \n"
    )
    cv.write("&emsp;&emsp;&emsp;&ensp; Submitted 30/9/22, Defended 6/12/22\n\n")
    cv.write("2018 &emsp; MSci Geophysics, University College London  \n")
    cv.write("&emsp;&emsp;&emsp;&ensp; First Class Honours  \n")
    cv.write(
        "&emsp;&emsp;&emsp;&ensp; *Rayleigh wave ellipticity inversion for crustal velocity structre*  \n"
    )
    cv.write("&emsp;&emsp;&emsp;&ensp; Supervised by Prof Ana Ferreira\n")


def write_contact(cv):
    cv.write(f"Email: {reader.content['contact']['email']}  \n")
    cv.write(f"Address: {', '.join(reader.content['contact']['address'].values())}\n")


def write_professional(cv):
    cv.write(
        "Jan 23 - Dec 23 &emsp; PDRA Seismology, Research School of Earth Sciences, ANU  \n"
    )
    cv.write(
        "Sep 22 - Dec 22 &emsp;PDRA Seismology, Department of Earth Sciences, UCL  \n"
    )
    cv.write(
        "Jun 22 &emsp;&emsp;&emsp;&emsp;&emsp;&ensp;Scientist, Land seismometer deployment, Azores  \n"
    )
    cv.write(
        "Jun 21 - Aug 21 &emsp; Scientist, UPFLOW Ocean-bottom Seismometer deployment, Atlantic Ocean  \n"
    )
    cv.write("Oct 19 - May 20 &ensp; Machine Learning Intern, KageNova Ltd.  \n")
    cv.write(
        "Oct 18 - Sep 22 &emsp; PhD Student, Centre for Doctoral Training in Data Intensive Science, UCL  \n"
    )


def write_journals(cv):
    journals = [
        "Geophysical Journal International",
        "Journal of Geophysical Research - Solid Earth",
        "Physics of the Earth and Planetary Interiors",
    ]
    for journal in journals:
        cv.write(f"* {journal}\n")


def write_teaching(cv):
    cv.write("2021 - 2022 &emsp; Machine Learning with Big Data, UCL  \n")
    cv.write("2019 - 2021 &emsp; Seismology II, UCL  \n")
    cv.write("2019 - 2021 &emsp; Field Geophysics, UCL  \n")
    cv.write("2017 - 2021 &emsp; MATLAB, UCL  \n")


if __name__ == "__main__":
    content_dir = ".."
    CV = os.path.join(content_dir, "cv", "_index.md")
    reader = SiteReader(content_dir)
    reader.get_contact()
    reader.get_publications()
    reader.get_talks()

    with open(CV, "w") as cv:
        cv.write("# Dr Augustin Marignier CV  \n\n")
        write_contact(cv)
        cv.write("\n")
        cv.write("## Education \n\n")
        write_education(cv)
        cv.write("\n")
        cv.write("## Professional History \n\n")
        write_professional(cv)
        cv.write("\n")
        cv.write(("## Publications\n\n"))
        write_pubs(cv, reader)
        cv.write("\n")
        cv.write("## Teaching\n\n")
        write_teaching(cv)
        cv.write("\n")
        cv.write("## Talks\n\n")
        write_talks(cv, reader)
        cv.write("\n")
        cv.write("## Journal Peer Reviews\n\n")
        write_journals(cv)
