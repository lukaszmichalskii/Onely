class QueriesSetup:
    """
    Class responsilble for setup queries
    """

    def __init__(self, prefix: str, keywords: list):
        self.prefix = prefix
        self.keywords = keywords

    def create_queries(self) -> list:
        queries = []
        for word in self.keywords:
            query = self.prefix + word
            queries.append(query)

        return queries
