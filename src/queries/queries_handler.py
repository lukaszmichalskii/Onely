from src.keywords.keywords_handler import KeywordsHandler
from src.queries.queries_setup import QueriesSetup
from src.settings.settings import Settings


class QueriesHandler:
    """
    Class responsible for store complete queries
    """

    def __init__(self, keywords_handler: KeywordsHandler):
        self.__query_prefix = Settings().query_prefix
        self.__keywords = keywords_handler.keywords
        self.__queries_setup = QueriesSetup(self.__query_prefix, self.__keywords)
        self.__queries = self.__queries_setup.create_queries()

    @property
    def queries(self):
        return self.__queries
