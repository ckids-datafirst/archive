import csv
from pathlib import Path

from datafest_archive.models.database import Advisor, Project, SkillOrSoftware
from datafest_archive.reader.sqlite_writer import SQLITE_MANAGER

TIMESTAMP_COLUMN = 0
FACULTY_EMAIL_COLUMN = 1
FACULTY_NAME_COLUMN = 2
FACULTY_TITLE_COLUMN = 3
PROJECT_TITLE_COLUMN = 4
PROJECT_DESCRIPTION_COLUMN = 5
PROJECT_SKILLS_COLUMN = 6


def read_csv_file(path: Path) -> list[Project]:
    semester = "Fall"
    year = 2023

    projects: list[Project] = []
    with open(path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        counter = 0
        for row in reader:
            counter += 1
            if counter > 1:
                advisor = get_advisor(row)
                skills = get_skills(row)
                project = getProject(semester, year, row, advisor, skills)
                projects.append(project)
    return projects


def getProject(
    semester: str,
    year: int,
    row: list[str],
    advisor: Advisor,
    skills: list[SkillOrSoftware],
):
    return Project.from_spreadsheet(
        name=row[PROJECT_TITLE_COLUMN],
        project_overview=row[PROJECT_DESCRIPTION_COLUMN],
        semester=semester,
        year=year,
        skill_required=skills,
        advisors=[advisor],
    )


def get_skills(row: list[str]) -> list[SkillOrSoftware]:
    skills = row[PROJECT_SKILLS_COLUMN].split(",")
    # remove trailing spaces
    skills = [skill.strip() for skill in skills]
    return [SkillOrSoftware(name=skill, type="software") for skill in skills]


def get_advisor(row: list[str]):
    advisor_email: str = row[FACULTY_EMAIL_COLUMN]
    advisor_name: str = row[FACULTY_NAME_COLUMN]
    if advisor_name and "and" in advisor_name:
        advisors = advisor_name.split(" and ")
        advisor: Advisor = Advisor.from_spreadsheet(
            name=advisors[0],
            email=advisor_email,
            title=row[FACULTY_TITLE_COLUMN],
        )
    else:
        advisor_name = row[FACULTY_NAME_COLUMN]
        advisor: Advisor = Advisor.from_spreadsheet(
            name=advisor_name,
            email=advisor_email,
            title=row[FACULTY_TITLE_COLUMN],
        )

    return advisor


def import_spreadsheet(spreadsheet_path: Path, database_file: Path) -> None:
    projects = read_csv_file(spreadsheet_path)
    sqlite_manager = SQLITE_MANAGER(database_file)
    for project in projects:
        project_id = sqlite_manager.insert_project(project)
        advisors = project.advisors
        skills = project.skill_required
        if skills:
            for skill in skills:
                skill_id = sqlite_manager.insert_project_has_skill(project_id, skill)
        if advisors:
            for advisor in advisors:
                advisor_id = sqlite_manager.insert_advisor(advisor)
                sqlite_manager.insert_project_has_advisor(project_id, advisor_id)
