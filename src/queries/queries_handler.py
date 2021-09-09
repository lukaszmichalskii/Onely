from src.keywords.keywords_handler import KeywordsHandler
from src.queries.queries_setup import QueriesSetup


class QueriesHandler:
    """
    Class responsible for storing complete queries
    """

    def __init__(self, keywords_handler: KeywordsHandler, query_prefix: str):
        self.__query_prefix = query_prefix
        self.__keywords = keywords_handler.keywords
        self.__queries_setup = QueriesSetup(self.__query_prefix, self.__keywords)
        self.__queries = self.__queries_setup.create_queries()

    @property
    def queries(self) -> list:
        return self.__queries
