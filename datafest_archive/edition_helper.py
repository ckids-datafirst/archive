from pathlib import Path

from datafest_archive.database.models import Edition
from datafest_archive.utils import create_directory

CONTENT_EDITION_DIRECTORY = "editions"


def generate_edition_url(year: int, semester: str) -> str:
    return f"{CONTENT_EDITION_DIRECTORY}/{year}-{semester}"


def generate_edition_directory(edition: Edition, content_directory: Path):
    edition_directory = generate_edition_url(edition.year, edition.semester)
    project_edition_directory = create_directory(content_directory / edition_directory)
    with open(project_edition_directory / "index.md", "w") as f:
        f.write(generate_edition_content(edition))


def generate_edition_content(edition: Edition) -> str:
    return f"""---
title: {edition.semester} {edition.year}
date: {edition.year}-10-24
type: landing

sections:
  - block: portfolio
    id: projects
    content:
      title: {edition.semester} {edition.year} Projects
      filters:
        # folders to display content from
        folders:
          - projects
        # only show content with these tags
        tags: ["{edition.semester} {edition.year}"]
        # exclude content with these tags
        exclude_tags: []
        # which hugo page kinds to show (https://gohugo.io/templates/section-templates/#page-kinds)
        kinds:
          - page
      # field to sort by, such as date or title
      sort_by: "name"
      sort_ascending: false
      default_button_index: 0
---

"""
