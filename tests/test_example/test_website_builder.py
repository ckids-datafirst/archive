from pathlib import Path

import pytest

from datafest_archive.database.factory import (
    AdvisorFactory,
    ProjectFactory,
    StudentFactory,
)
from datafest_archive.website_buider import generate_website


def test_file_written_to_path(tmp_path):
    # Set up
    students = StudentFactory.batch(size=5)
    advisors = AdvisorFactory.batch(size=5)
    projects = ProjectFactory.batch(size=5)
    resources = students + advisors + projects
    generate_website(resources, tmp_path)
