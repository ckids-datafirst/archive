from typing import List

import logging
from dataclasses import dataclass
from pathlib import Path

import yaml

from datafest_archive.database.models import Edition, Project, Resource
from datafest_archive.edition_helper import (
    generate_edition_directory,
    generate_edition_url,
)
from datafest_archive.page_builder import (
    generate_resource_page,
    generate_simple_page,
    get_resource_path,
)
from datafest_archive.templates.models import MenuItem, SimplePage
from datafest_archive.utils import sanitanize_name, write_file


@dataclass
class Pages:
    name: str
    url: str
    weight: int


def generate_menu_page(pages: list[Pages]) -> str:
    return yaml.dump(pages)


def generate_config_file() -> None:
    logging.warning("generate_config_file is not implemented")


def generate_params_file() -> None:
    logging.warning("generate_params_file is not implemented")


CONTENT_DIRECTORY = "content"

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
        / "_index.md"
    )
    write_file(content, page_path)


def generate_info_for_students(output_directory: Path):
    page = SimplePage("Information for Students", "We need to add content here", None)
    content = generate_simple_page(page, "We need to add content here")
    page_path = (
        output_directory
        / CONTENT_DIRECTORY
        / f"{PAGE_INFO_FOR_STUDENTS.url}"
        / "_index.md"
    )
    write_file(content, page_path)


def generate_resources(resources: list[Resource], output_directory: Path) -> None:
    config_directory = output_directory / "config"
    content_directory = output_directory / CONTENT_DIRECTORY
    editions: list[Edition] = []
    for resource in resources:
        editions = add_editions(editions, resource)
        content = generate_resource_page(resource)
        resource_path = get_resource_path(resource, content_directory)
        validate_write(content, resource_path)

    menu_content = generate_menu(editions)
    validate_write(menu_content, config_directory / "menus.yaml")
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


def generate_menu(editions: list[Edition]) -> str:
    menu_base: str = """# Navigation Links
#   To link a homepage widget, specify the URL as a hash `#` followed by the filename of the
#     desired widget in your `content/home/` folder.
#   The weight parameter defines the order that the links will appear in.

main:
  - name: Advisors
    url: info-advisors
    weight: 10
  - name: Students
    url: info-students
    weight: 11
  - name: Previous projects
    url: projects
    weight: 12
  # - name: Projects
  #   url: projects
  #   weight: 10
  - name: People
    url: people
    weight: 20
  - name: Events
    url: event
    weight: 40
  # - name: Publications
  #   url: publication
  #   weight: 50
  - name: Contact
    url: contact
    weight: 60
    """
    menu_items = generate_menu_item(editions)
    return menu_base + menu_items


def generate_menu_item(editions: list[Edition]) -> str:
    menu_items: list[MenuItem] = []
    weight = 1
    for edition in editions:
        name = f"{edition.semester} {edition.year}"
        url_name = generate_edition_url(edition.year, edition.semester)
        menu_item = MenuItem(name, url_name, weight, "Previous Projects")
        menu_items.append(menu_item)
        weight += 1
    return yaml.dump(menu_items)
