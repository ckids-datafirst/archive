from pathlib import Path

import yaml

from datafest_archive.constants import CONTENT_EDITION_DIRECTORY, INDEX_REGULAR_PAGE
from datafest_archive.models.database import Edition, Semesters
from datafest_archive.models.website.pages import (
    Block,
    ComplexPage,
    Filters,
    Portafolio,
)
from datafest_archive.utils import (
    create_directory,
    get_fall_starting_date,
    get_spring_starting_date,
)


def generate_datetime_from_event(edition: Edition) -> str:
    if edition.semester and edition.semester == Semesters.FALL:
        return get_fall_starting_date(edition.year)
    elif edition.semester and edition.semester == Semesters.SPRING:
        return get_spring_starting_date(edition.year)
    return str(None)


def generate_edition_url(year: int, semester: str) -> str:
    name = f"{CONTENT_EDITION_DIRECTORY}/{year}-{semester}"
    return name.lower()


def generate_edition_directory(edition: Edition, content_directory: Path):
    edition_directory = generate_edition_url(edition.year, edition.semester)
    project_edition_directory = create_directory(content_directory / edition_directory)
    with open(project_edition_directory / INDEX_REGULAR_PAGE, "w") as f:
        f.write(generate_edition_content(edition))


def generate_edition_content(edition: Edition) -> str:
    date_created = generate_datetime_from_event(edition)
    filters = Filters(
        folders=["projects"],
        tags=[f"{edition.semester} {edition.year}"],
        exclude_tags=[],
        kinds=["page"],
    )
    section = Portafolio(
        title=f"{edition.semester} {edition.year} Projects",
        filters=filters,
        sort_by="Title",
        sort_ascending=False,
        default_button_index=0,
    )
    block = Block(block="portfolio", id="portfolio", content=section)
    edition_page = ComplexPage(
        title=f"{edition.semester} {edition.year}",
        date=date_created,
        type="landing",
        sections=[block],
    )
    structured_content = yaml.dump(edition_page)
    unstructured_content = ""
    return f"---\n{structured_content}\n---\n{unstructured_content}"
