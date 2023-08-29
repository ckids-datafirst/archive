from typing import List

import json
from pathlib import Path

from datafest_archive.builder.website_buider import generate_website
from datafest_archive.models.database import Advisor, Project, Resource, Student

PROJECT_KEY = "projects"
ADVISOR_KEY = "advisors"


def get_resources(directory: Path) -> list[Advisor | Project]:
    files = [f for f in directory.iterdir() if f.is_file()]
    projects: list[Project] = []
    advisors: list[Advisor] = []
    students: list[Student] = []
    for file in files:
        if not file.suffix == ".json":
            raise ValueError(f"File {file} is not a json file")
        else:
            print(f"File {file} is a json file")
            with open(file) as f:
                content = json.load(f)
                for project_content in content[PROJECT_KEY]:
                    project = Project.from_dict(project_content)
                    projects.append(project)
                    if project.advisors is not None:
                        for advisor in project.advisors:
                            if advisor not in advisors:
                                advisors.append(advisor)
                    if project.students is not None:
                        for student in project.students:
                            if student not in students:
                                students.append(student)
    return projects + advisors + students


def validate_directory(directory: Path):
    # The main directory should exist and must contains subdirectory
    if not directory.exists():
        raise FileNotFoundError(f"Directory {directory} does not exist")
    if not directory.is_dir():
        raise NotADirectoryError(f"{directory} is not a directory")
    # list all files in the directory
    files = [f for f in directory.iterdir() if f.is_file()]
    if len(files) == 0:
        raise FileNotFoundError(f"Directory {directory} is empty")


def handle_json(directory: Path, output_directory: Path):
    validate_directory(directory)
    resources = get_resources(directory)
    generate_website(resources, output_directory)
