from typing import List

import json
import sqlite3
from pathlib import Path

from datafest_archive.builder.website_buider import generate_website
from datafest_archive.models.database import Advisor, Award, Project, Student, Topic

PROJECT_KEY = "projects"
ADVISOR_KEY = "advisors"


def handle_sqlite(file: Path, content_directory: Path):
    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    projects = get_projects(cursor)
    advisors = get_advisors(cursor)
    students = get_students(cursor)
    resources = projects + advisors + students
    generate_website(resources, content_directory)


def get_projects(cursor: sqlite3.Cursor) -> list[Project]:
    projects: list[Project] = []
    cursor.execute("SELECT * FROM project")
    for row in cursor.fetchall():
        project = Project.from_db(row)
        students = get_students_by_project_id(cursor, project.id)
        advisors = get_advisors_by_project_id(cursor, project.id)
        topics = get_topics_by_project_id(cursor, project.id)
        awards = get_awards_by_project_id(cursor, project.id)
        project.topic = topics
        project.awards = awards
        project.advisors = advisors
        project.students = students
        projects.append(project)
    return projects


def get_topics_by_project_id(cursor: sqlite3.Cursor, project_id: int) -> list[Topic]:
    topics: list[Topic] = []
    cursor.execute(
        "SELECT id, topic FROM project_has_topic WHERE id = ?",
        (project_id,),
    )
    for row in cursor.fetchall():
        topic = Topic.from_db(row)
        topics.append(topic)
    return topics


def get_awards_by_project_id(cursor: sqlite3.Cursor, project_id: int) -> list[Award]:
    awards: list[Award] = []
    cursor.execute(
        "SELECT project_id, award FROM project_has_award WHERE project_id = ?",
        (project_id,),
    )
    for row in cursor.fetchall():
        award = Award.from_db(row)
        awards.append(award)
    return awards


def get_students_by_project_id(
    cursor: sqlite3.Cursor, project_id: int
) -> list[Student]:
    students: list[Student] = []
    cursor.execute(
        "SELECT * FROM student WHERE student.id IN (SELECT student_id FROM project_has_student WHERE project_id = ?)",
        (project_id,),
    )
    for row in cursor.fetchall():
        student = Student.from_db(row)
        student.semesters_participated = get_semester_student(cursor, student)
        students.append(student)
    return students


def get_semester_student(cursor: sqlite3.Cursor, student: Student):
    if student.id:
        semester_participated: list[str] = []
        for project in get_projects_by_student_id(cursor, student.id):
            semester = f"{project.semester} {project.year}"
            if semester not in semester_participated:
                semester_participated.append(semester)

        return semester_participated


def get_semester_advisor(cursor: sqlite3.Cursor, advisor: Advisor):
    if advisor.id:
        semester_participated: list[str] = []
        for project in get_projects_by_advisor_id(cursor, advisor.id):
            semester = f"{project.semester} {project.year}"
            if semester not in semester_participated:
                semester_participated.append(semester)

        return semester_participated


def get_advisors_by_project_id(
    cursor: sqlite3.Cursor, project_id: int
) -> list[Advisor]:
    advisors: list[Advisor] = []
    cursor.execute(
        "SELECT * FROM advisor WHERE advisor.id IN (SELECT advisor_id FROM project_has_advisor WHERE project_id = ?)",
        (project_id,),
    )
    for row in cursor.fetchall():
        advisor = Advisor.from_db(row)
        advisor.semesters_participated = get_semester_advisor(cursor, advisor)
        advisors.append(advisor)
    return advisors


def get_advisors(cursor: sqlite3.Cursor) -> list[Advisor]:
    advisors: list[Advisor] = []
    cursor.execute("SELECT * FROM advisor")
    for row in cursor.fetchall():
        advisor = Advisor.from_db(row)
        advisor.semesters_participated = get_semester_advisor(cursor, advisor)
        advisors.append(advisor)

    return advisors


def get_students(cursor: sqlite3.Cursor) -> list[Student]:
    students: list[Student] = []
    cursor.execute("SELECT * FROM student")
    for row in cursor.fetchall():
        student = Student.from_db(row)
        student.semesters_participated = get_semester_student(cursor, student)
        students.append(student)
    return students


def get_projects_by_student_id(
    cursor: sqlite3.Cursor, student_id: int
) -> list[Project]:
    projects: list[Project] = []
    cursor.execute(
        "SELECT * FROM project WHERE project.id IN (SELECT project_id FROM project_has_student WHERE student_id = ?)",
        (student_id,),
    )

    for row in cursor.fetchall():
        project = Project.from_db(row)
        projects.append(project)
    return projects


def get_projects_by_advisor_id(
    cursor: sqlite3.Cursor, student_id: int
) -> list[Project]:
    projects: list[Project] = []
    cursor.execute(
        "SELECT * FROM project WHERE project.id IN (SELECT project_id FROM project_has_advisor WHERE advisor_id = ?)",
        (student_id,),
    )

    for row in cursor.fetchall():
        project = Project.from_db(row)
        projects.append(project)
    return projects
