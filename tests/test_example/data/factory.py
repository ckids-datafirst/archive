from typing import List

from faker import Faker
from polyfactory import Use
from polyfactory.factories import DataclassFactory

from datafest_archive.models.database import (
    Advisor,
    Award,
    Project,
    SkillOrSoftware,
    Student,
    Topic,
)
from tests.test_example.data.fake_data import (
    awards,
    degree_programs,
    organizations,
    primary_schools,
    project_names,
    titles,
    topics,
)


class AwardFactory(DataclassFactory[Award]):
    __model__ = Award
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__random__.choice(awards)

    @classmethod
    def description(cls) -> str:
        return cls.__random__.choice(awards)


class SkillOrSoftwareFactory(DataclassFactory[SkillOrSoftware]):
    __model__ = SkillOrSoftware
    __random_seed__ = 1
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.sentence(nb_words=3)

    @classmethod
    def type(cls) -> str:
        return cls.__random__.choice(["skill", "software"])


class TopicFactory(DataclassFactory[Topic]):
    __model__ = Topic
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__random__.choice(topics)


class StudentFactory(DataclassFactory[Student]):
    __model__ = Student
    __random_seed__ = 2
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.name()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()

    @classmethod
    def degree_program(cls) -> str:
        return cls.__random__.choice(degree_programs)

    @classmethod
    def school(cls) -> str:
        return cls.__random__.choice(primary_schools)


class AdvisorFactory(DataclassFactory[Advisor]):
    __model__ = Advisor
    __random_seed__ = 1
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.name()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()

    @classmethod
    def organization(cls) -> str:
        return cls.__random__.choice(organizations)

    @classmethod
    def title(cls) -> str:
        return cls.__random__.choice(titles)

    @classmethod
    def primary_school(cls) -> str:
        return cls.__random__.choice(primary_schools)


class ProjectFactory(DataclassFactory[Project]):
    __model__ = Project
    __random_seed__ = 1
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__random__.choice(project_names)

    @classmethod
    def semester(cls) -> str:
        return cls.__random__.choice(["Fall", "Spring"])

    @classmethod
    def year(cls) -> int:
        return cls.__random__.randint(2015, 2021)

    @classmethod
    def project_overview(cls) -> str:
        return cls.__faker__.paragraph(nb_sentences=3)

    @classmethod
    def final_presentation(cls) -> str:
        return cls.__faker__.url()

    @classmethod
    def topic(cls) -> list[Topic]:
        return TopicFactory.batch(size=1)

    @classmethod
    def awards(self) -> list[Award]:  # type: ignore
        if self.__random__.random() < 0.1:
            return AwardFactory.batch(size=1)

    skill_required = Use(SkillOrSoftwareFactory.batch, size=3)
