# type: ignore[attr-defined]
from typing import Annotated, Optional

from enum import Enum
from pathlib import Path
from random import choice

import typer
from rich.console import Console

from datafest_archive import version
from datafest_archive.reader.json_reader import handle_json


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


class Reader(str, Enum):
    """The type of reader to use."""

    json = "json"
    sqlite = "sqlite"


app = typer.Typer(
    name="datafest-archive",
    help="DataFestArchive is a Python package designed to generate the DataFestArchive website from past versions of DataFest",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]datafest-archive[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command()
def main(
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the datafest-archive package.",
    ),
) -> None:
    console.print(f"[bold blue]DataFestArchive[/] version: [bold blue]{version}[/]")


@app.command()
def generate(
    path: Annotated[
        Path,
        typer.Argument(
            metavar="INPUT_PATH", help="The input path to use. Depends on the type."
        ),
    ],
    input_type: Annotated[
        Reader, typer.Option(help="The type of website to generate.")
    ],
    website_output_directory: Annotated[
        Path, typer.Argument(help="The directory to output the website to.")
    ],
) -> None:
    if input_type == Reader.json:
        handle_json(path, website_output_directory)
    elif input_type == Reader.sqlite:
        handle_sqlite(path, website_output_directory)


if __name__ == "__main__":
    app()
