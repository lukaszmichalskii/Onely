from googlesearch import search
from src.queries.queries_handler import QueriesHandler
from src.settings.settings import Settings


class LinksScraper:
    """
    Class responsible for extract links from search results
    """

    def __init__(self, queries: QueriesHandler):
        self.__settings = Settings()
        self.__queries = queries.queries

    def scrap_links(self):
        links = []
        for query in self.__queries:
            for link in search(query, num=self.__settings.searches_nr, stop=self.__settings.searches_nr, pause=2):
                if self.__settings.searches_web_site_filter in link:
                    links.append(link)

        return links
