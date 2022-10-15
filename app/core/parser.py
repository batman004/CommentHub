import re
from core.errors import TagMismatchError


class Parser:
    def __init__(self):
        self._settings = {}

    def load_parser_settings(self, parser_settings):
        self._settings = parser_settings
        self._token = self._settings["token"]
        self._op_left = self._settings["opening_tag"]["left"]
        self._op_right = self._settings["opening_tag"]["right"]
        self._cls_left = self._settings["closing_tag"]["left"]
        self._cls_right = self._settings["closing_tag"]["right"]

        self.__op_tag_regex()  # compile regex for opening tag
        self.__cls_tag_regex()  # regex for closing tag

    def parse(self, filename):
        comments = []

        with open(filename, "r") as fh:
            start_line, end_line = 0, 0
            comment = ""
            tag_open = False
            opening_tag = None

            for line_num, line in enumerate(fh):
                if not tag_open:
                    opening_tag = self._op_tag_pattern.search(line)

                closing_tag = self._cls_tag_pattern.search(line)

                if tag_open and self._op_tag_pattern.search(line):
                    raise TagMismatchError(
                        line,
                        f"on line: {line_num} expected: {self._cls_tag_pattern.pattern} but got: {self._op_tag_pattern.pattern}",
                    )

                if opening_tag:
                    tag_open = True
                    start_line = line_num

                if tag_open:
                    comment += line

                if (
                    closing_tag
                    and opening_tag
                    and not self.__is_tag_pair(
                        opening_tag.group(0), closing_tag.group(0)
                    )
                ):
                    raise TagMismatchError(
                        line,
                        f"on line: {line_num} expected: {self._cls_tag_pattern.pattern} but got: {self._op_tag_pattern.pattern}",
                    )

                if opening_tag and closing_tag:
                    end_line = line_num
                    comments.append(
                        {"start": start_line, "end": end_line, "comment": comment}
                    )

                    comment = ""
                    tag_open = False

        return comments

    def __op_tag_regex(self):
        tag = f"{self._op_left}{self._token}{self._op_right}"
        versioned_tag = (
            f"({self._op_left}{self._token}-v([1-9]+[0-9])*{self._op_right})"
        )

        self._op_tag_pattern = re.compile(f"{tag}|{versioned_tag}")

    def __cls_tag_regex(self):
        tag = f"{self._cls_left}{self._token}{self._cls_right}"
        versioned_tag = (
            f"({self._cls_left}{self._token}-v([1-9]+[0-9])*{self._cls_right})"
        )

        self._cls_tag_pattern = re.compile(f"{tag}|{versioned_tag}")

    def __is_tag_pair(self, opening, closing):
        op_token = opening.strip(self._op_left).strip(self._op_right)
        cls_token = closing.strip(self._cls_left).strip(self._cls_right)

        return op_token == cls_token
