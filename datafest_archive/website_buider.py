from typing import List

import logging
from dataclasses import dataclass
from pathlib import Path

import yaml

from datafest_archive.database.models import Resource
from datafest_archive.page_builder import (
    generate_resource_page,
    generate_simple_page,
    get_resource_path,
)
from datafest_archive.templates.models import SimplePage
from datafest_archive.utils import write_file


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
    content_directory = output_directory / CONTENT_DIRECTORY
    for resource in resources:
        content = generate_resource_page(resource)
        resource_path = get_resource_path(resource, content_directory)
        write_file(content, resource_path)
