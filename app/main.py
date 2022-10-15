from core.parser import Parser
import pprint
parser_settings = {
    "token": "COMMENT",
    "opening_tag": {"left": "<", "right": ">"},
    "closing_tag": {"left": "</", "right": ">"},
}


parser = Parser()
parser.load_parser_settings(parser_settings)
output = parser.parse("/home/kabir/Desktop/hackout_2022/CommentHub/dummy/file1.py")
pprint.pprint(output)
