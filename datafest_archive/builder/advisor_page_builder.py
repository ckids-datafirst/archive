from datafest_archive.constants import ROLE_ADVISOR
from datafest_archive.models.database import Advisor
from datafest_archive.models.website.pages import Organization, PeoplePage, Social
from datafest_archive.utils import dump_yaml


def build_advisor_structured_section(advisor: Advisor) -> PeoplePage:
    email: Social = Social(
        icon="envelope",
        icon_pack="fas",
        link=advisor.email,
    )

    organization: Organization = Organization(
        name=advisor.organization,
        url=None,
    )

    advisor_page = PeoplePage(
        title=advisor.name,
        role=ROLE_ADVISOR,
        user_groups=[ROLE_ADVISOR],
        social=[email],
        email=advisor.email,
        bio="",
        education=None,
        organizations=[organization],
    )
    return advisor_page


def build_advisor_unstructured_section(advisor: Advisor) -> str:
    return f"""
    ## Links
    """


def generate_advisor_page(advisor: Advisor) -> str:
    structured_section = build_advisor_structured_section(advisor)
    unstructured_section = build_advisor_unstructured_section(advisor)
    structed_section_yaml = dump_yaml(structured_section)
    return f"---\n{structed_section_yaml}---\n{unstructured_section}"
