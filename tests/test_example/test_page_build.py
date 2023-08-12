from datafest_archive.advisor_page_builder import generate_advisor_page
from datafest_archive.database.factory import (
    AdvisorFactory,
    ProjectFactory,
    StudentFactory,
)
from datafest_archive.page_builder import generate_project_page
from datafest_archive.student_page_builder import generate_student_page


def test_build_project_page_test():
    project = ProjectFactory.build()
    project_page = generate_project_page(project)
    with open("project_page_example.md", "w") as f:
        f.write(project_page)


# def test_build_advisor_page_test():
#     advisor = AdvisorFactory.build()
#     advisor_page = generate_advisor_page(advisor)
#     with open("advisor_page_example.md", "w") as f:
#         f.write(advisor_page)


# def test_build_student_page_test():
#     student = StudentFactory.build()
#     student_page = generate_student_page(student)
#     with open("student_page_example.md", "w") as f:
#         f.write(student_page)
