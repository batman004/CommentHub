__cli_name__ = "CommentHub"
__version__ = "0.0.1"

default_parser_settings = {
    "token": "COMMENT",
    "opening_tag": {"left": "<", "right": ">"},
    "closing_tag": {"left": "</", "right": ">"},
}

(
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    INSERT_COMMENT_ERROR,
    REMOVE_COMMENT_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    INSERT_COMMENT_ERROR: "error while inserting comments",
    REMOVE_COMMENT_ERROR: "error while removing comments",
}
