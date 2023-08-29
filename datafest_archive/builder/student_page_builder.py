from typing import List

from datafest_archive.constants import ROLE_STUDENT
from datafest_archive.models.database import Student
from datafest_archive.models.website.pages import Course, Education, PeoplePage, Social
from datafest_archive.utils import dump_yaml, full_name_to_first_and_last_name


def generate_student_page(student: Student) -> str:
    structured_section = build_student_structured_section(student)
    unstructured_section = build_student_unstructured_section(student)
    structed_section_yaml = dump_yaml(structured_section)
    return f"---\n{structed_section_yaml}---\n{unstructured_section}"


def build_student_structured_section(student: Student) -> PeoplePage:
    # remove blank lines from email
    if student and student.email:
        student.email = student.email.replace("\n", "")
        social: Social = Social(
            icon="envelope",
            icon_pack="fas",
            link=f"mailto:{student.email}",
        )
    else:
        social: Social = Social(
            icon="envelope",
            icon_pack="fas",
            link="mosorio@isi.edu",
        )

    if student.degree_program is None and student.school is None:
        education = None
    else:
        education: Education = Education(
            courses=[
                Course(
                    course=student.degree_program,
                    institution=student.school,
                    year=None,
                )
            ]
        )

    first_name, last_name = full_name_to_first_and_last_name(student.name)
    users_groups: list[str] = []
    if student.semesters_participated:
        for year in student.semesters_participated:
            users_groups.append(f"{ROLE_STUDENT} ({year})")
    student_page = PeoplePage(
        first_name=first_name,
        last_name=last_name,
        title=student.name,
        role=ROLE_STUDENT,
        user_groups=users_groups,
        social=[social],
        email=student.email,
        bio="",
        education=education,
        organizations=[],
    )
    return student_page


def build_student_unstructured_section(student: Student) -> str:
    if student.semesters_participated:
        # split each semester into two parts (semester and year) and sort by year
        student.semesters_participated = sorted(
            [
                f"{semester.split()[1]} {semester.split()[0]}"
                for semester in student.semesters_participated
            ]
        )

        semesters_participated = "\n".join(
            [f"- {semester}" for semester in student.semesters_participated]
        )

    return f"""
## Previous involvement

{student.name} has been involved in the previous DataFest events:
{semesters_participated}

    """
    return f"""
    """
