import random
from pathlib import Path

import pytest

from datafest_archive.database.factory import (
    AdvisorFactory,
    ProjectFactory,
    StudentFactory,
)
from datafest_archive.website_buider import generate_website


def test_build_website(tmp_path):
    # Set up
    students = StudentFactory.batch(size=60)
    advisors = AdvisorFactory.batch(size=10)
    projects = ProjectFactory.batch(size=20)

    selected_students = students.copy()
    for project in projects:
        project.students = random.sample(selected_students, 3)
        project.advisors = random.sample(advisors, 2)

        # remove selected students from the pool
        for student in project.students:
            selected_students.remove(student)

    resources = students + advisors + projects
    generate_website(resources, tmp_path)
