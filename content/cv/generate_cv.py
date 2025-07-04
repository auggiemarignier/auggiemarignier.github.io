"""
Generate a markdown CV from the latex CV in the cv submodule.

This is done by using pandoc to convert latex to markdown.

First the latex source needs to be cleaned to remove custom things
that pandoc can't handle, like custom commands and environments.

The strategy for cleaning is to explicitly say what blocks need to be removed.
This avoids trying to figure out regexes and match multiple lines.
Thus this script is fairly brittle and will fail if the latex source changes too much.
"""

import os
from pathlib import Path
import subprocess


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CV_CONTENT_PATH = PROJECT_ROOT / "content" / "cv"
CV_SOURCE_PATH = CV_CONTENT_PATH / "cv"

REMOVE_THESE_BLOCKS = [
    r"""
% Redefine sectioning commands to be unnumbered by default
% Save original sectioning commands
\makeatletter
\let\origsection\section
\renewcommand{\section}{\@ifstar{\subsection*}{\subsection*}}
\makeatother
""",
    r"""
\let\oldthebibliography\thebibliography
\let\endoldthebibliography\endthebibliography
\renewenvironment{thebibliography}[1]{
  \begin{oldthebibliography}{#1}
    \setlength{\itemsep}{0em}
    % \setlength{\parskip}{0em}
}
{
  \end{oldthebibliography}
}
""",
    r"""
\renewcommand\refname{Publications}
""",
]


def get_source_files() -> list[Path]:
    """
    Get the source files for the CV.
    """
    return list(CV_SOURCE_PATH.glob("*.tex"))


def clean_source_files(source_files: list[Path]) -> None:
    """
    Clean the source files by removing blocks that pandoc can't handle.
    """
    for source_file in source_files:
        content = source_file.read_text(encoding="utf-8")
        for block in REMOVE_THESE_BLOCKS:
            content = content.replace(block, "")
        source_file.write_text(content, encoding="utf-8")


def call_pandoc() -> None:
    """
    Call pandoc to convert the cleaned latex source to markdown.
    """
    output_file = CV_CONTENT_PATH / "_index.md"
    command = [
        "pandoc",
        str(CV_SOURCE_PATH / "main.tex"),
        "--output",
        str(output_file),
        "--from=latex",
        "--to=markdown",
        "--bibliography",
        str(CV_SOURCE_PATH / "publications.bib"),
        "--citeproc",
    ]

    subprocess.run(command, check=True)


def main() -> None:
    """
    Main function to generate the CV.
    """
    os.chdir(CV_SOURCE_PATH)
    source_files = get_source_files()
    clean_source_files(source_files)
    call_pandoc()


if __name__ == "__main__":
    main()
