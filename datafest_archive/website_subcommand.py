from typing import Annotated

from pathlib import Path

import typer

from datafest_archive.reader.sqlite_reader import handle_sqlite

app = typer.Typer()


@app.command()
def create(
    path: Annotated[Path, typer.Argument(help="Database file to use")],
    website_output_directory: Annotated[
        Path,
        typer.Argument(
            help="The content directory of the website to output to. (e.g. content/)"
        ),
    ],
):
    """
    Create pages of projects and people (students and advisors) from the database (sqlite3) using wowchemy-hugo-academic.
    """
    handle_sqlite(path, website_output_directory)
