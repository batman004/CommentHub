from distutils.log import error
import re


class Parser:
    def __init__(self):
        self._settings = None

    def load_parser_settings(self, parser_settings):
        self._settings = parser_settings
        self.__op_tag_regex()  # compile regex for opening tag
        self.__cls_tag_regex()  # regex for closing tag

    def parse(self, filename):
        comments = []
        start_line, end_line = 0, 0
        comment = ""
        tag_open = False

        with open(filename, "r") as fh:
            for line_num, line in enumerate(fh):
                if tag_open and self._op_tag_pattern.search(line):
                    raise error(f'tag mismatch: \nexpected: {self._cls_tag_pattern}\ngot: {self._op_tag_pattern}')

                if self._op_tag_pattern.search(line):
                    tag_open = True
                    start_line = line_num

                if tag_open:
                    comment += line

                if self._cls_tag_pattern.search(line):
                    tag_open = False
                    end_line = line_num
                    comments.append({
                        "start": start_line,
                        "end": end_line,
                        "comment": comment
                    })

                    comment = ""
                    tag_open = False

    def __op_tag_regex(self):
        self._token = self._settings["token"]
        self._left = self._settings["opening_tag"]["left"]
        self._right = self._settings["opening_tag"]["right"]

        tag = f"{self._left}{self._token}{self._right}"
        versioned_tag = f"({self._left}{self._token}-v[1-9]+[0-9]*{self._right})"

        self._op_tag_pattern = re.compile(f"{tag}|{versioned_tag}")

    def __cls_tag_regex(self):
        self._token = self._settings["token"]
        self._left = self._settings["closing_tag"]["left"]
        self._right = self._settings["closing_tag"]["right"]

        tag = f"{self._left}{self._token}{self._right}"
        versioned_tag = f"({self._left}{self._token}-v[1-9]+[0-9]*{self._right})"

        self._cls_tag_pattern = re.compile(f"{tag}|{versioned_tag}")
