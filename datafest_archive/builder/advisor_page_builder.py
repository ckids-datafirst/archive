from datafirst.models.database import Advisor
from datafirst.utils import full_name_to_first_and_last_name

from datafest_archive.builder.templating import jinja_environment
from datafest_archive.constants import ROLE_ADVISOR, ROLE_CHAIR
from datafest_archive.models.website.pages import Organization, PeoplePage, Social
from datafest_archive.utils import dump_yaml


def build_advisor_structured_section(advisor: Advisor) -> PeoplePage:
    email: Social = Social(
        icon="envelope",
        icon_pack="fas",
        link=f"mailto:{advisor.email}",
    )

    if advisor.primary_school is not None:
        if isinstance(advisor.primary_school, str):
            organization: Organization = Organization(
                name=advisor.primary_school,
                url="",
            )
        else:
            organization: Organization = Organization(
                name=advisor.primary_school.name,
                url=advisor.primary_school.url,
            )
    else:
        organization = Organization(
            name="",
            url="",
        )

    first_name, last_name = full_name_to_first_and_last_name(advisor.name)

    users_groups: list["str"] = []

    if advisor.semesters_participated:
        for year in advisor.semesters_participated:
            users_groups.append(f"{ROLE_ADVISOR} ({year})")

    if advisor.semesters_participated_as_chair:
        for year in advisor.semesters_participated_as_chair:
            users_groups.append(f"{ROLE_CHAIR} ({year})")

    role = advisor.title or ROLE_ADVISOR
    advisor_page = PeoplePage(
        title=advisor.name,
        first_name=first_name,
        last_name=last_name,
        role=role,
        user_groups=users_groups,
        social=[email],
        email=advisor.email,
        bio="",
        education=None,
        organizations=[organization],
    )
    return advisor_page


def build_advisor_unstructured_section(advisor: Advisor) -> str:
    # convert a list of semesters_participated in a markdown items
    template = jinja_environment.get_template("advisor_page.md.jinja")
    return template.render(
        advisor=advisor,
    )


def generate_advisor_page(advisor: Advisor) -> str:
    structured_section = build_advisor_structured_section(advisor)
    unstructured_section = build_advisor_unstructured_section(advisor)
    structed_section_yaml = dump_yaml(structured_section)
    return f"---\n{structed_section_yaml}---\n{unstructured_section}"
