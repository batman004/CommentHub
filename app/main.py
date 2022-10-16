"""Commenthub entry point script."""
from CommentHub import __cli_name__
from CommentHub.handlers import app


def main():
    app(prog_name=__cli_name__)


if __name__ == "__main__":
    main()
