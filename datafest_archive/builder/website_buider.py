from typing import List

import logging
from pathlib import Path

import yaml

from datafest_archive.builder.edition_page_builder import generate_edition_directory
from datafest_archive.builder.menu_builder import generate_menu
from datafest_archive.builder.page_builder import (
    generate_resource_page,
    generate_simple_page,
    get_resource_path,
)
from datafest_archive.constants import (
    CONFIG_DIRECTORY,
    CONTENT_DIRECTORY,
    INDEX_LIST_PAGE,
    MENUS_FILE_NAME,
)
from datafest_archive.models.database import Edition, Project, Resource
from datafest_archive.models.website.pages import Pages, SimplePage
from datafest_archive.utils import write_file


def generate_config_file() -> None:
    logging.warning("generate_config_file is not implemented")


def generate_params_file() -> None:
    logging.warning("generate_params_file is not implemented")


PAGE_INFO_FOR_ADVISORS = Pages(name="InfoForAdvisors", url="info_advisors", weight=1)
PAGE_INFO_FOR_STUDENTS = Pages(name="InfoForStudents", url="info_students", weight=2)
PAGE_PROJECTS = Pages(name="Projects", url="projects", weight=3)
PAGE_PEOPLE = Pages(name="People", url="people", weight=4)
PAGE_SPONSORS = Pages(name="Sponsors", url="sponsors", weight=5)
PAGE_CONTACT = Pages(name="Contact", url="contact", weight=6)


def generate_website(resources: list[Resource], output_directory: Path) -> None:
    generate_content(resources, output_directory)


def generate_content(resources: list[Resource], output_directory: Path) -> None:
    generate_info_for_advisors(output_directory)
    generate_info_for_students(output_directory)
    generate_resources(resources, output_directory)


def generate_info_for_advisors(output_directory: Path):
    page = SimplePage("Information for Advisors", "We need to add content here", None)
    content = generate_simple_page(page, "We need to add content here")
    page_path = (
        output_directory
        / CONTENT_DIRECTORY
        / f"{PAGE_INFO_FOR_ADVISORS.url}"
        / INDEX_LIST_PAGE
    )
    write_file(content, page_path)


def generate_info_for_students(output_directory: Path):
    page = SimplePage("Information for Students", "We need to add content here", None)
    content = generate_simple_page(page, "We need to add content here")
    page_path = (
        output_directory
        / CONTENT_DIRECTORY
        / f"{PAGE_INFO_FOR_STUDENTS.url}"
        / INDEX_LIST_PAGE
    )
    write_file(content, page_path)


def generate_resources(resources: list[Resource], output_directory: Path) -> None:
    config_directory = output_directory / CONFIG_DIRECTORY
    content_directory = output_directory / CONTENT_DIRECTORY
    editions: list[Edition] = []
    for resource in resources:
        editions = add_editions(editions, resource)
        content = generate_resource_page(resource)
        resource_path = get_resource_path(resource, content_directory)
        validate_write(content, resource_path)

    menu_content = generate_menu(editions)
    validate_write(menu_content, config_directory / MENUS_FILE_NAME)
    for edition in editions:
        generate_edition_directory(edition, content_directory)


def validate_write(content: str, resource_path: Path):
    try:
        write_file(content, resource_path)
    except ValueError as e:
        logging.error(f"Could not write file: {resource_path}")
        logging.error(e)


def add_editions(editions: list[Edition], resource: Resource) -> list[Edition]:
    if isinstance(resource, Project):
        edition = Edition(resource.semester, resource.year)
        editions.append(edition)
    return editions
