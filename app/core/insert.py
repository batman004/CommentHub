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
            fh = open(filename, "r")
            temp_fh = open(f"/tmp/commenthub_tmp.py", "w")
            line_indices = Insert._lines_to_insert(comments)

            line_num, offset = 0, 0
            while True:
                line = fh.readline()

                # file is over but comments were not inserted!
                if not line and line_num - offset in line_indices:
                    break

                print(f"line_num: {line_num} | line_num - offset: {line_num - offset}")
                if line_num - offset in line_indices:
                    comment = line_indices[line_num - offset]
                    temp_fh.write(comment.comment)

                    num_of_lines = comment.end - comment.start + 1
                    line_num += num_of_lines
                    offset += num_of_lines
                    print(f"offset increase by: {num_of_lines}")

                temp_fh.write(line)
                line_num += 1

            temp_fh.close()
            fh.close()

            fh = open(filename, "w")
            temp_fh = open(f"/tmp/commenthub_tmp.py", "r")
            for line in temp_fh:
                fh.write(line)

            temp_fh.close()
            fh.close()

        except FileNotFoundError:
            print(f"file: {filename} not found")
            sys.exit(1)
        finally:
            fh.close()
            temp_fh.close()

    @staticmethod
    def _lines_to_insert(comments):
        line_indices = {}

        for comment in comments:
            start = comment["start"]
            end = comment["end"]
            comment = comment["comment"]

            line_indices[start] = Comment(start, end, comment)

        return line_indices
