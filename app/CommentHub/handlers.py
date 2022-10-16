import typer
from typing import Optional
from CommentHub import __cli_name__, __version__, default_parser_settings

app = typer.Typer()

from core.parser import Parser
from core.remove import Remove
import pprint


@app.command()
def remove_comments(file_location: str = typer.Argument(...)):
    """Remove commented out code under comment-tag"""
    parser = Parser()
    parser.load_parser_settings(default_parser_settings)
    comments = parser.parse(file_location)
    pprint.pprint(comments)
    Remove.remove_comments(file_location, comments)


@app.command()
def retrieve_comments(file_location: str = typer.Argument(...)):
    """Retrieves previous versions of commented out blocks"""
    pass


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__cli_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
