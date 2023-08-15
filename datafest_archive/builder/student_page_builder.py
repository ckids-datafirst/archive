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
    email: Social = Social(
        icon="envelope",
        icon_pack="fas",
        link=student.email,
    )

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
    student_page = PeoplePage(
        first_name=first_name,
        last_name=last_name,
        title=student.name,
        role=ROLE_STUDENT,
        user_groups=[ROLE_STUDENT],
        social=[email],
        email=student.email,
        bio="",
        education=education,
        organizations=[],
    )
    return student_page


def build_student_unstructured_section(student: Student) -> str:
    return f"""
    {student.name}
    """
