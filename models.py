from typing import Optional
from pydantic import BaseModel


class student(BaseModel):

    id: int
    name: Optional[str]
    email: Optional[str]
    degree_program: Optional[str]
    school: Optional[str]


class project(BaseModel):

    id: int
    name: Optional[str]
    semester: Optional[str]
    year: Optional[int]
    project_overview: Optional[str]
    final_presentation: Optional[str]
    award_id: Optional[int]
    skill_required_id: Optional[int]
    topic_id: Optional[int]


class projectHasStudent(BaseModel):

    project_id: Optional[int]
    student_id: Optional[int]


class advisor(BaseModel):

    id: int
    name: Optional[str]
    email: Optional[str]
    organization: Optional[str]
    title: Optional[str]
    primary_school: Optional[str]


class projectHasAdvisor(BaseModel):

    project_id: Optional[int]
    advisor_id: Optional[int]


class hasAward(BaseModel):

    recipient_id: Optional[int]
    award: Optional[int]


class skillOrSoftware(BaseModel):

    id: int
    name: Optional[str]
    type: Optional[str]


class topic(BaseModel):

    id: int
    name: Optional[str]
