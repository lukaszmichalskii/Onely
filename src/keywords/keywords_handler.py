from pathlib import Path

from src.file_read_save.file_reader import read_file


class KeywordsHandler:
    """
    Class stores raw keywords read from keywords.txt file
    """

    def __init__(self):
        self.__filepath = self.__get_filepath('keywords.txt')
        self.__keywords = read_file(self.__filepath)

    @property
    def keywords(self):
        return self.__keywords

    def __get_filepath(self, file_to_open: str):
        files_fd = Path('files/')
        filepath = files_fd / file_to_open

        return filepath
