from datafest_archive.database.models import Student
from datafest_archive.templates.models import Course, Education, PeoplePage, Social
from datafest_archive.utils import dump_yaml

STUDENT_ROLE = "Student"


def build_student_structed_section(student: Student) -> PeoplePage:
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

    student_page = PeoplePage(
        title=student.name,
        role=STUDENT_ROLE,
        user_groups=[STUDENT_ROLE],
        social=[email],
        email=student.email,
        bio="",
        education=education,
        organizations=[],
    )
    return student_page


def build_student_unstructed_section(project: Student) -> str:
    return f"""
    ## Links
    """


def generate_student_page(project: Student) -> str:
    structed_section = build_student_structed_section(project)
    unstructed_section = build_student_unstructed_section(project)
    structed_section_yaml = dump_yaml(structed_section)
    return f"---\n{structed_section_yaml}---\n{unstructed_section}"
