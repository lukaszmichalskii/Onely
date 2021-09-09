class QueriesSetup:
    """
    Class responsible for setup queries
    """

    def __init__(self, prefix: str, keywords: list):
        self.__prefix = prefix
        self.__keywords = keywords

    def create_queries(self) -> list:
        queries = []
        for word in self.__keywords:
            query = self.__prefix + word
            queries.append(query)

        return queries
