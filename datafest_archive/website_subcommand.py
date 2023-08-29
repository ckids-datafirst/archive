from typing import Annotated

from pathlib import Path

import typer

from datafest_archive.reader.sqlite_reader import handle_sqlite

app = typer.Typer()


@app.command()
def create(
    path: Annotated[
        Path,
        typer.Argument(metavar="INPUT_PATH", help="Database file to use."),
    ],
    website_output_directory: Annotated[
        Path,
        typer.Argument(
            help="The content directory of the website to output to. (e.g. content/)"
        ),
    ],
) -> None:
    handle_sqlite(path, website_output_directory)


if __name__ == "__main__":
    app()
