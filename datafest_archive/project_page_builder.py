from datafest_archive.database.models import Project
from datafest_archive.templates.models import ProjectPage
from datafest_archive.utils import dump_yaml


def build_project_structed_section(project: Project) -> ProjectPage:
    students = [student.name for student in project.students]
    advisors = [advisor.name for advisor in project.advisors]
    authors = students + advisors
    edition = f"{project.semester} {project.year}"
    tags = [edition]

    project_page = ProjectPage(
        title=project.name,
        summary=project.project_overview,
        authors=authors,
        tags=tags,
        categories=[topic.name for topic in project.topic],
        external_link=project.final_presentation,
        image=None,
        url_code=None,
        url_pdf=None,
        url_slides=project.final_presentation,
        url_video=None,
        slides=project.final_presentation,
        date=None,
        weight=10,
    )
    return project_page


def build_project_unstructed_section(project: Project) -> str:
    return f"""
    ## Links
    """


def generate_project_page(project: Project) -> str:
    structed_section = build_project_structed_section(project)
    unstructed_section = build_project_unstructed_section(project)
    structed_section_yaml = dump_yaml(structed_section)
    return f"---\n{structed_section_yaml}---\n{unstructed_section}"
