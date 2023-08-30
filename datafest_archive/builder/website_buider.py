from typing import List

import logging
from pathlib import Path

from datafest_archive.builder.menu_builder import generate_menu
from datafest_archive.builder.page_builder import (
    generate_resource_page,
    generate_simple_page,
    get_resource_path,
)
from datafest_archive.builder.semester_page_builder import generate_edition_directory
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


def generate_website(resources: list[Resource], content_directory: Path) -> None:
    generate_content(resources, content_directory)


def generate_content(resources: list[Resource], content_directory: Path) -> None:
    # generate_info_for_advisors(content_directory)
    # generate_info_for_students(content_directory)
    generate_resources(resources, content_directory)


def generate_resources(resources: list[Resource], content_directory: Path) -> None:
    # config_directory = content_directory / CONFIG_DIRECTORY
    editions: list[Edition] = []
    for resource in resources:
        editions = add_editions(editions, resource)
        content = generate_resource_page(resource)
        resource_path = get_resource_path(resource, content_directory)
        validate_write(content, resource_path)

    # get projects

    # menu_content = generate_menu(editions)
    # validate_write(menu_content, config_directory / MENUS_FILE_NAME)

    # get projects from resources
    projects = [resource for resource in resources if isinstance(resource, Project)]
    for edition in editions:
        generate_edition_directory(edition, projects, content_directory)


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
