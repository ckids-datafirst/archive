from pathlib import Path

import yaml
from datafirst.models.database import Advisor, Project, Student
from datafirst.utils import people_name_to_directory_name

from datafest_archive.builder.project_page_builder import generate_project_url
from datafest_archive.constants import (
    CONTENT_PEOPLE_DIRECTORY,
    CONTENT_PROJECT_DIRECTORY,
    INDEX_LIST_PAGE,
)
from datafest_archive.models.website.pages import SimplePage
from datafest_archive.utils import create_directory


def create_advisor_directory(advisor: Advisor, parent_directory: Path) -> Path:
    if advisor.url_name == "":
        raise ValueError("Advisor url_name is None")
    advisor_directory = create_directory(
        parent_directory / CONTENT_PEOPLE_DIRECTORY / advisor.url_name
    )
    return advisor_directory / INDEX_LIST_PAGE


def create_student_directory(student: Student, parent_directory: Path):
    directory_name = people_name_to_directory_name(student.name)
    student_directory = create_directory(
        parent_directory / CONTENT_PEOPLE_DIRECTORY / directory_name
    )
    return student_directory / f"_index.md"


def create_project_directory(resource: Project, parent_directory: Path):
    edition = generate_project_url(resource)
    directory_name = f"{resource.id}"
    project_directory = create_directory(
        parent_directory / CONTENT_PROJECT_DIRECTORY / edition / directory_name
    )
    return project_directory / f"index.md"


def generate_simple_page(page: SimplePage, markdown_content: str) -> str:
    structured_section = yaml.dump(page)
    unstructured_section = f"""{markdown_content}"""
    return f"---\n{structured_section}---\n{unstructured_section}"
