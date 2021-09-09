from src.file_read_save.csv_save import get_filepath
from src.file_read_save.file_reader import read_file


class KeywordsHandler:
    """
    Class stores raw keywords read from keywords.txt file
    """

    def __init__(self):
        self.__filepath = get_filepath('keywords.txt')
        self.__keywords = read_file(self.__filepath)

    @property
    def keywords(self) -> list:
        return self.__keywords
