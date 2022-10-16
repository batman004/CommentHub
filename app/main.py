from core.dump_comments import StorageEngine
from core.parser import Parser
from core.remove import Remove
from core.insert import Insert

import pprint

parser_settings = {
    "token": "COMMENT",
    "opening_tag": {"left": "<", "right": ">"},
    "closing_tag": {"left": "</", "right": ">"},
}

filename = "/home/kabir/Desktop/hackout_2022/CommentHub/dummy/file1.py"

parser = Parser()
parser.load_parser_settings(parser_settings)
comments = parser.parse(filename)

storage = StorageEngine(1, "/home/kabir/Desktop/hackout_2022/CommentHub/", "123")

file_loc = storage.dump(comments)

Remove.remove_comments(filename, comments)

comments = StorageEngine.load(file_loc)

Insert.insert_comments(filename, comments)
