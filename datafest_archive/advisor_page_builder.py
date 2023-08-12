from datafest_archive.database.models import Advisor
from datafest_archive.templates.models import Organization, PeoplePage, Social
from datafest_archive.utils import dump_yaml

ROLE = "Advisor"


def build_advisor_structed_section(advisor: Advisor) -> PeoplePage:
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
        role=ROLE,
        user_groups=[ROLE],
        social=email,
        email=advisor.email,
        bio="",
        education=None,
        organizations=[organization],
    )
    return advisor_page


def build_advisor_unstructed_section(advisor: Advisor) -> str:
    return f"""
    ## Links
    """


def generate_advisor_page(advisor: Advisor) -> str:
    structed_section = build_advisor_structed_section(advisor)
    unstructed_section = build_advisor_unstructed_section(advisor)
    structed_section_yaml = dump_yaml(structed_section)
    return f"---\n{structed_section_yaml}---\n{unstructed_section}"
