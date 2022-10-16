# dump non-versioned comments to disk
from typing import List

import pickle
from pathlib import PurePath


class StorageEngine:
    def __init__(self, version: int, location: str, unique_id: str) -> None:
        self.file_name = f"v{version}_{unique_id}.pkl"
        self.file_loc = PurePath(location, ".comment_hub", self.file_name)

    def dump(self, comments: List[dict]):
        comments = self.filter_comments(comments)

        with open(self.file_loc, "wb") as comments_file:
            pickle.dump(comments, comments_file, protocol=pickle.HIGHEST_PROTOCOL)
            comments_file.close()

        return self.file_loc

    @staticmethod
    def load(file_loc):
        with open(file_loc, "rb") as comments_dump:
            comments = pickle.load(comments_dump)
            return comments

    def filter_comments(self, comments):
        return list(filter(lambda c: not c["is_versioned"], comments))
