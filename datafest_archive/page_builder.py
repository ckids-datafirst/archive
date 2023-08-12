from pathlib import Path

from datafest_archive.advisor_page_builder import generate_advisor_page
from datafest_archive.database.models import Project, Resource, Student
from datafest_archive.project_page_builder import generate_project_page
from datafest_archive.student_page_builder import generate_student_page

CONTENT_PEOPLE_DIRECTORY = "people"
CONTENT_PROJECT_DIRECTORY = "projects"


def get_resource_path(resource: Resource, parent_directory: Path) -> Path:
    if isinstance(resource, Project):
        return (
            parent_directory / CONTENT_PROJECT_DIRECTORY / f"project_{resource.id}.md"
        )
    elif isinstance(resource, Student):
        return parent_directory / CONTENT_PEOPLE_DIRECTORY / f"student_{resource.id}.md"
    else:
        return parent_directory / CONTENT_PEOPLE_DIRECTORY / f"advisor_{resource.id}.md"


def generate_page(resource: Resource) -> str:
    if isinstance(resource, Project):
        return generate_project_page(resource)
    elif isinstance(resource, Student):
        return generate_student_page(resource)
    else:
        return generate_advisor_page(resource)
