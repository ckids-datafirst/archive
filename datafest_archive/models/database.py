from typing import List, Union

from dataclasses import dataclass
from enum import Enum

from datafest_archive.constants import FALL, SPRING, SUMMER, WINTER


@dataclass
class Award:
    id: int
    name: str
    description: str


@dataclass
class SkillOrSoftware:
    id: int
    name: str
    type: str


@dataclass
class Topic:
    id: int
    name: str


@dataclass
class Student:
    id: int
    name: str
    email: str
    degree_program: str
    school: str


@dataclass
class Advisor:
    id: int
    name: str
    email: str
    organization: str
    title: str
    primary_school: str


@dataclass
class Project:
    id: int
    name: str
    semester: str
    year: int
    project_overview: str
    final_presentation: str
    awards: list[Award]
    skill_required: list[SkillOrSoftware]
    topic: list[Topic]
    students: list[Student]
    advisors: list[Advisor]


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
