from pathlib import Path

import yaml

from datafest_archive.advisor_page_builder import generate_advisor_page
from datafest_archive.database.models import Project, Resource, Student
from datafest_archive.project_page_builder import generate_project_page
from datafest_archive.student_page_builder import generate_student_page
from datafest_archive.templates.models import SimplePage
from datafest_archive.utils import create_directory

CONTENT_PEOPLE_DIRECTORY = "authors"
CONTENT_PROJECT_DIRECTORY = "projects"


def get_resource_path(resource: Resource, parent_directory: Path) -> Path:
    if isinstance(resource, Project):
        project_directory = create_directory(
            parent_directory / CONTENT_PROJECT_DIRECTORY / str(resource.id)
        )
        return project_directory / f"_index.md"
    elif isinstance(resource, Student):
        student_directory = create_directory(
            parent_directory / CONTENT_PEOPLE_DIRECTORY / f"student_{str(resource.id)}"
        )
        return student_directory / f"_index.md"
    else:
        advisor_directory = create_directory(
            parent_directory / CONTENT_PEOPLE_DIRECTORY / f"advisor_{str(resource.id)}"
        )
        return advisor_directory / f"_index.md"


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
