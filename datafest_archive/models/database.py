from typing import Optional, Union

from dataclasses import dataclass
from enum import Enum

from dataclass_wizard import JSONWizard

from datafest_archive.constants import FALL, SPRING, SUMMER, WINTER


@dataclass
class Award(JSONWizard):
    name: str
    id: Optional[int] = None
    description: Optional[str] = None

    def from_db(row: tuple[int, str, str]):
        return Award(name=row[1])


@dataclass
class SkillOrSoftware:
    name: str
    type: str
    id: Optional[int] = None

    def from_db(row: tuple[str, str]):
        return SkillOrSoftware(name=row[0], type=row[1])


@dataclass
class Topic:
    name: str
    id: Optional[int] = None

    def from_db(row: tuple[str]):
        return Topic(name=row[1])


@dataclass
class Student:
    name: str
    email: str
    id: Optional[int] = None
    degree_program: Optional[str] = None
    school: Optional[str] = None

    def from_db(row: tuple[int, str, str, str, str]):
        return Student(
            id=row[0], name=row[1], email=row[2], degree_program=row[3], school=row[4]
        )


@dataclass
class Advisor:
    name: str
    email: Optional[str] = None
    organization: Optional[str] = None
    title: Optional[str] = None
    primary_school: Optional[str] = None
    id: Optional[int] = None

    def from_db(row: tuple[int, str, str, str, str, str]):
        return Advisor(
            id=row[0],
            name=row[1],
            email=row[2],
            organization=row[3],
            primary_school=row[4],
        )


@dataclass
class Project(JSONWizard):
    id: int
    name: str
    semester: str
    year: int
    project_overview: str
    skill_required: Optional[list[SkillOrSoftware]] = None
    awards: Optional[list[Award]] = None
    topics: Optional[list[Topic]] = None
    students: Optional[list[Student]] = None
    final_presentation: Optional[str] = None
    advisors: Optional[list[Advisor]] = None

    def from_db(row: tuple[int, str, str, int, str, str]):
        return Project(
            id=row[0],
            name=row[1],
            semester=row[2],
            year=row[3],
            project_overview=row[4],
            final_presentation=row[5],
        )


class Semesters(Enum):
    FALL = FALL
    WINTER = WINTER
    SPRING = SPRING
    SUMMER = SUMMER


@dataclass
class Edition:
    semester: str
    year: int


Resource = Union[Project, Student, Advisor]
