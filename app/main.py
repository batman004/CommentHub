from core.parser import Parser
from core.remove import Remove
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
pprint.pprint(comments)

Remove.remove_comments(filename, comments)
