from typing import Union

import pathlib

import yaml

from datafest_archive.templates.models import (
    Image,
    Organization,
    PeoplePage,
    ProjectPage,
    Social,
)


def project_page_representer(dumper, data):
    data_dict = {
        "title": data.title,
        "summary": data.summary,
        "authors": data.authors,
        "tags": data.tags,
        "categories": data.categories,
        "date": data.date,
        "weight": data.weight,
        "external_link": data.external_link,
        "image": data.image,
        "url_code": data.url_code,
        "url_pdf": data.url_pdf,
        "url_slides": data.url_slides,
        "url_video": data.url_video,
        "slides": data.slides,
    }
    return dumper.represent_mapping("!ProjectPage", data_dict)


def organization_representer(dumper, data):
    return dumper.represent_mapping(
        "!Organization", {"name": data.name, "url": data.url}
    )


def image_representer(dumper, data):
    return dumper.represent_mapping(
        "!Image", {"path": data.path, "caption": data.caption}
    )


def social_representer(dumper, data):
    return dumper.represent_mapping(
        "!Social",
        {
            "icon": data.icon,
            "icon_pack": data.icon_pack,
            "link": data.link,
        },
    )


def get_dumper():
    """Add representers to a YAML seriailizer."""
    safe_dumper = yaml.Dumper
    safe_dumper.add_representer(ProjectPage, project_page_representer)
    safe_dumper.add_representer(Organization, organization_representer)
    safe_dumper.add_representer(Image, image_representer)
    safe_dumper.add_representer(Social, social_representer)
    return safe_dumper


def dump_yaml(resource: Union[ProjectPage | PeoplePage]) -> str:
    return yaml.dump(resource, Dumper=get_dumper(), sort_keys=True)


def write_file(content: str, path: pathlib.Path):
    if path.is_dir():
        raise ValueError(f"Path {path} is a directory.")
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with open(path, "w") as f:
        f.write(content)
