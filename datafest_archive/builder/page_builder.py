from pathlib import Path

import yaml

from datafest_archive.builder.advisor_page_builder import generate_advisor_page
from datafest_archive.builder.project_page_builder import (
    generate_project_page,
    generate_project_url,
)
from datafest_archive.builder.student_page_builder import generate_student_page
from datafest_archive.constants import (
    CONTENT_PEOPLE_DIRECTORY,
    CONTENT_PROJECT_DIRECTORY,
    INDEX_LIST_PAGE,
)
from datafest_archive.models.database import Advisor, Project, Resource, Student
from datafest_archive.models.website.pages import SimplePage
from datafest_archive.utils import (
    create_directory,
    full_name_to_first_and_last_name,
    people_name_to_directory_name,
)


def get_resource_path(resource: Resource, parent_directory: Path) -> Path:
    if isinstance(resource, Project):
        return create_project_directory(resource, parent_directory)
    elif isinstance(resource, Advisor):
        return create_student_directory(resource, parent_directory)
    else:
        return create_advisor_directory(resource, parent_directory)


def create_advisor_directory(advisor: Advisor, parent_directory: Path):
    advisor_directory = create_directory(
        parent_directory / CONTENT_PEOPLE_DIRECTORY / advisor.url_name
    )
    return advisor_directory / INDEX_LIST_PAGE


def create_student_directory(student: Student, parent_directory: Path):
    first_name, last_name = full_name_to_first_and_last_name(student.name)
    directory_name = people_name_to_directory_name(first_name, last_name)
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


def generate_resource_page(resource: Resource) -> str:
    if isinstance(resource, Project):
        return generate_project_page(resource)
    elif isinstance(resource, Student):
        return generate_student_page(resource)
    else:
        return generate_advisor_page(resource)


def generate_simple_page(page: SimplePage, markdown_content: str) -> str:
    structured_section = yaml.dump(page)
    unstructured_section = f"""{markdown_content}"""
    return f"---\n{structured_section}---\n{unstructured_section}"
