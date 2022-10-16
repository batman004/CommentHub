import sys


class Comment:
    def __init__(self, start=0, end=0, comment="") -> None:
        self.start = start
        self.end = end
        self.comment = comment
        self.num_lines = end - start + 1


class Insert:
    @staticmethod
    def insert_comments(filename, comments):
        try:
            fh = open(filename, "a")
            fh.write("\n")

            for comment in comments:
                fh.write(comment["comment"])
                fh.write("\n")

            fh.close()

        except FileNotFoundError:
            print(f"file: {filename} not found")
            sys.exit(1)
        finally:
            fh.close()

    @staticmethod
    def _lines_to_insert(comments):
        line_indices = {}

        for comment in comments:
            start = comment["start"]
            end = comment["end"]
            comment = comment["comment"]

            line_indices[start] = Comment(start, end, comment)

        return line_indices
