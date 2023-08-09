# type: ignore[attr-defined]
from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

from enum import Enum
from random import choice

import typer
from rich.console import Console

from datafest_archive import version
from datafest_archive.example import hello


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


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
    database: Annotated[Path, typer.Argument(help="The database to use.")],
    website_output_directory: Annotated[Path, typer.Argument(help="The directory to output the website to.")],
) -> None:
    if not database.exists():
        console.print(f"[bold red]Database {database} does not exist![/]")
        raise typer.Exit(code=1)
    if not website_output_directory.exists():
        console.print(f"[bold red]Website output directory {website_output_directory} does not exist![/]")
        raise typer.Exit(code=1)

    console.print(f"[bold {database}]{website_output_directory}[/]")
if __name__ == "__main__":
    app()
