from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: Optional[str]
    email: Optional[str]
    degree_program: Optional[str]
    school: Optional[str]


class Project(BaseModel):
    id: int
    name: Optional[str]
    semester: Optional[str]
    year: Optional[int]
    project_overview: Optional[str]
    final_presentation: Optional[str]
    award_id: Optional[int]
    skill_required_id: Optional[int]
    topic_id: Optional[int]


class ProjectHasStudent(BaseModel):
    project_id: Optional[int]
    student_id: Optional[int]


class Advisor(BaseModel):
    id: int
    name: Optional[str]
    email: Optional[str]
    organization: Optional[str]
    title: Optional[str]
    primary_school: Optional[str]


class ProjectHasAdvisor(BaseModel):
    project_id: Optional[int]
    advisor_id: Optional[int]


class HasAward(BaseModel):
    recipient_id: Optional[int]
    award: Optional[int]


class SkillOrSoftware(BaseModel):
    id: int
    name: Optional[str]
    type: Optional[str]


class Topic(BaseModel):
    id: int
    name: Optional[str]
