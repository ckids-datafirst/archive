from datafest_archive.models.database import Project
from tests.test_example.data.factory import ProjectFactory


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
