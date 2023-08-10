from faker import Faker
from polyfactory import Use
from polyfactory.factories import DataclassFactory

from datafest_archive.database.models import (
    Advisor,
    Award,
    Project,
    SkillOrSoftware,
    Student,
    Topic,
)

awards = [
    "Best in Show",
    "Best in Category",
    "Best in Class",
    "Best in Division",
    "Best in Grade",
]
organizations = [
    "University of Southern California",
    "University of California, Los Angeles",
]
titles = ["Professor", "Associate Professor", "Assistant Professor"]
primary_schools = ["Viterbi School of Engineering", "School of Cinematic Arts"]
degree_programs = ["Computer Science", "Computer Engineering", "Electrical Engineering"]
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]


class AwardFactory(DataclassFactory[Award]):
    __model__ = Award
    __random_seed__ = 1
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__random__.choice(awards)

    @classmethod
    def description(cls) -> str:
        return cls.__faker__.paragraph(nb_sentences=3)


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
    __random_seed__ = 1
    __faker__ = Faker(locale="en_US")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.sentence(nb_words=3)


class StudentFactory(DataclassFactory[Student]):
    __model__ = Student
    __random_seed__ = 1
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
        return cls.__faker__.sentence(nb_words=3)

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

    awards = Use(AwardFactory, size=1)
    skill_required = Use(SkillOrSoftwareFactory.batch, size=3)
    topic = Use(TopicFactory.batch, size=3)
    students = Use(StudentFactory.batch, size=3)
    advisors = Use(AdvisorFactory.batch, size=3)
