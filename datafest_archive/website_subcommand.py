from typing import Annotated, Optional

from pathlib import Path

import typer

from datafest_archive.reader.sqlite_reader import handle_sqlite

app = typer.Typer()


@app.command()
def create(
    path: Annotated[Path, typer.Option(help="Database file to use.", default=None)],
    website_output_directory: Annotated[
        Path,
        typer.Option(
            help="The content directory of the website to output to. (e.g. content/)",
            default=None,
        ),
    ],
) -> None:
    handle_sqlite(path, website_output_directory)


if __name__ == "__main__":
    app()
