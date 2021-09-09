from googlesearch import search
from src.queries.queries_handler import QueriesHandler


class LinksScraper:
    """
    Class responsible for extract links from search results
    """

    def __init__(self, queries: QueriesHandler, scrap_links_settings: dict):
        self.__settings = scrap_links_settings
        self.__queries = queries.queries

    def scrap_links(self) -> list:
        links = []
        for query in self.__queries:
            for link in search(query, tld='com', num=self.__settings['links_per_page'],
                               stop=self.__settings['searches_nr'],
                               pause=self.__settings['delay']):

                if self.__settings['web_site_filter'] in link:
                    links.append(link)

        return links
