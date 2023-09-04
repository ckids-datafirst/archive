import random
from pathlib import Path

from datafest_archive.builder.website_buider import generate_website
from tests.test_example.data.factory import (
    AdvisorFactory,
    ProjectFactory,
    StudentFactory,
)


def test_build_website(tmp_path: Path):
    # Set up
    students = StudentFactory.batch(size=30)
    advisors = AdvisorFactory.batch(size=20)
    projects = ProjectFactory.batch(size=4)

    selected_students = students.copy()
    for project in projects:
        project.students = random.sample(selected_students, 3)
        project.advisors = random.sample(advisors, 2)

        # remove selected students from the pool
        for student in project.students:
            selected_students.remove(student)

    generate_website(projects, advisors, students, tmp_path)
