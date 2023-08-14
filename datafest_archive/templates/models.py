from typing import List, Optional

from dataclasses import dataclass

import yaml


@dataclass
class Image:
    name: str
    caption: str
    focal_point: str
    preview_only: bool


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
    title: str
    role: str
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
    external_link: str
    image: Image
    url_code: str
    url_pdf: str
    url_slides: str
    url_video: str
    slides: str


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
class MenuItem:
    name: str
    url: str
    weight: int
    parent: Optional[str]
