import readline
import sys


class Remove:
    @staticmethod
    def remove_comments(filename, comments):
        try:
            fh = open(filename, "r")
            temp_fh = open(f"/tmp/commenthub_tmp.py", "w")
            line_indices = Remove._lines_to_remove(comments)  # start: end

            line_num = 0
            while True:
                line = fh.readline()

                if not line:
                    break

                if line_num in line_indices:
                    end = line_indices[line_num]
                    line = None

                    while line_num <= end:
                        fh.readline()
                        line_num += 1
                        continue

                if line:
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

    @staticmethod
    def _lines_to_remove(comments):
        line_indices = {}
        for comment in comments:
            start = comment["start"]
            end = comment["end"]
            line_indices[start] = end

        return line_indices
