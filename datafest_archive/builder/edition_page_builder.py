from pathlib import Path

import yaml

from datafest_archive.constants import (
    ALL_TAG,
    ALL_TAG_NAME,
    CONTENT_EDITION_DIRECTORY,
    EDITION_PEOPLE_PAGE,
    EDITION_PROJECTS_PAGE,
    EDITION_PROJECTS_WINNER_PAGE,
    FEATURED_TAG,
    FEATURED_TAG_NAME,
    INDEX_REGULAR_PAGE,
    ROLE_ADVISOR,
)
from datafest_archive.models.database import Edition, Semesters
from datafest_archive.models.website.pages import (
    FilterButton,
    Filters,
    PeopleContent,
    PeopleWidget,
    PortfolioWidget,
    WidgetPage,
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
    with open(project_edition_directory / EDITION_PROJECTS_PAGE, "w") as f:
        f.write(generate_edition_potfolio_page(edition))
    with open(project_edition_directory / EDITION_PEOPLE_PAGE, "w") as f:
        f.write(generate_edition_people_page(edition))
    with open(project_edition_directory / INDEX_REGULAR_PAGE, "w") as f:
        f.write(generate_index_page())


def generate_index_page() -> str:
    content = {
        "type": "widget_page",
    }
    structured_content = yaml.dump(content)
    unstructured_content = ""
    return f"---\n{structured_content}\n---\n{unstructured_content}"


def generate_edition_people_page(edition: Edition) -> str:
    content = PeopleContent(
        user_groups=[ROLE_ADVISOR],
    )
    widget_page = PeopleWidget(
        title="Advisors",
        subtitle=f"{edition.semester} {edition.year}",
        date=generate_datetime_from_event(edition),
        headless=True,
        widget="people",
        content=content,
    )
    structured_content = yaml.dump(widget_page)
    unstructured_content = ""
    return f"---\n{structured_content}\n---\n{unstructured_content}"


def generate_edition_potfolio_page(
    edition: Edition, filter_featured: bool = False
) -> str:
    date_created = generate_datetime_from_event(edition)
    tags = [f"{edition.semester} {edition.year}"]
    title = f"{edition.semester} {edition.year} Projects"
    filters = Filters(
        folders=["projects"],
        tags=tags,
        exclude_tags=[],
        kinds=["page"],
    )
    filter_featured_button = FilterButton(
        name=FEATURED_TAG_NAME, tag=FEATURED_TAG, weight=1
    )
    filter_all_button = FilterButton(name=ALL_TAG_NAME, tag=ALL_TAG, weight=2)

    content = PortfolioWidget(
        title=f"{edition.semester} {edition.year} Projects",
        filters=filters,
        filter_button=[filter_all_button, filter_featured_button],
        sort_by="Title",
        sort_ascending=False,
        default_button_index=0,
    )
    portfolio = WidgetPage(
        title=title,
        subtitle=f"{edition.semester} {edition.year}",
        date=date_created,
        type="landing",
        widget="portfolio",
        content=content,
        headless=True,
    )
    structured_content = yaml.dump(portfolio)
    unstructured_content = ""
    return f"---\n{structured_content}\n---\n{unstructured_content}"
