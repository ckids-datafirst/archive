from typing import List

import dataclasses
import json

import pytest

from datafest_archive.database.factory import ProjectFactory
from datafest_archive.database.models import (
    Advisor,
    Award,
    Project,
    SkillOrSoftware,
    Student,
    Topic,
)


def test_hello():
    """Example test with parametrization."""
    projects = ProjectFactory.batch(size=3)
    result = projects[0]
    assert isinstance(result, Project)
    assert isinstance(result.id, int)
    assert isinstance(result.name, str)
    assert isinstance(result.semester, str)
    assert isinstance(result.year, int)
    assert isinstance(result.project_overview, str)
    assert isinstance(result.final_presentation, str)
    with open("dump.json", "w") as f:
        f.write(json.dumps(dataclasses.asdict(result)))
    # assert isinstance(result.skill_required, List[SkillOrSoftware])
    # assert isinstance(result.topic, List[Topic])
    # assert isinstance(result.students, List[Student])
    # assert isinstance(result.advisors, List[Advisor])
