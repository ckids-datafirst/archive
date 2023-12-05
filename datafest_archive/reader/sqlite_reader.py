from pathlib import Path

from datafirst.database import Database

from datafest_archive.builder.website_buider import generate_website

PROJECT_KEY = "projects"
ADVISOR_KEY = "advisors"


def handle_sqlite(file: Path, content_directory: Path):
    database = Database(file)
    projects = database.get_projects()
    advisors = database.get_advisors()
    students = database.get_students()
    generate_website(
        projects=projects,
        advisors=advisors,
        students=students,
        content_directory=content_directory,
    )
