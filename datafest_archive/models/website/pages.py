from typing import List, Optional, Union

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Image:
    name: str
    caption: str
    focal_point: str
    preview_only: bool
    path: str


@dataclass
class Social:
    icon: str
    icon_pack: str
    link: str


@dataclass
class Organization:
    name: str
    url: Optional[str]


@dataclass
class Course:
    course: str
    institution: str
    year: Optional[int]


@dataclass
class Education:
    courses: list[Course]


@dataclass
class PeoplePage:
    title: Optional[str]
    role: str
    first_name: str
    last_name: str
    user_groups: list[str]
    social: list[Social]
    bio: str
    education: Optional[Education]
    email: str
    organizations: Optional[list[Organization]]


@dataclass
class ProjectPage:
    title: str
    summary: str
    authors: list[str]
    tags: list[str]
    categories: list[str]
    date: str
    weight: int
    external_link: Optional[str]
    image: Optional[Image]
    url_code: Optional[str]
    url_pdf: Optional[str]
    url_slides: Optional[str]
    url_video: Optional[str]
    slides: Optional[str]


@dataclass
class Pages:
    name: str
    url: str
    weight: int


@dataclass
class Header:
    caption: str
    image: Image


@dataclass
class SimplePage:
    title: str
    summary: str
    header: Optional[Header]


@dataclass
class Filters:
    folders: list[str]
    tags: list[str]
    exclude_tags: list[str]
    kinds: list[str]


@dataclass
class Portafolio:
    title: str
    filters: Filters
    sort_by: str
    sort_ascending: bool
    default_button_index: int


@dataclass
class Block:
    id: str
    block: str
    content: Portafolio


@dataclass
class ComplexPage:
    title: str
    date: str
    type: str
    sections: list[Block]


Page = Union[PeoplePage, ProjectPage, SimplePage]
DateTimeNone = Union[datetime, None]
