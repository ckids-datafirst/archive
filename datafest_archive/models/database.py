from typing import List, Optional, Union

from dataclasses import dataclass
from enum import Enum

from dataclass_wizard import JSONWizard

from datafest_archive.constants import FALL, SPRING, SUMMER, WINTER


@dataclass
class Award(JSONWizard):
    id: int
    name: str
    description: str


@dataclass
class SkillOrSoftware:
    name: str
    type: str
    id: Optional[int] = None


@dataclass
class Topic:
    id: int
    name: str


@dataclass
class Student:
    id: int
    name: str
    email: str
    degree_program: Optional[str] = None
    school: Optional[str] = None


@dataclass
class Advisor:
    name: str
    email: Optional[str] = None

    organization: Optional[str] = None
    title: Optional[str] = None
    primary_school: Optional[str] = None
    id: Optional[int] = None


@dataclass
class Project(JSONWizard):
    id: int
    name: str
    semester: str
    year: int
    project_overview: str
    skill_required: list[SkillOrSoftware]
    awards: Optional[list[Award]] = None
    topic: Optional[list[Topic]] = None
    students: Optional[list[Student]] = None
    final_presentation: Optional[str] = None
    advisors: Optional[list[Advisor]] = None


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
