from src.file_read_save.csv_save import csv_save_links, csv_save_results_nr
from src.keywords.keywords_handler import KeywordsHandler
from src.queries.queries_handler import QueriesHandler
from src.scrapers.links_handler import LinksHandler
from src.scrapers.links_scraper import LinksScraper
from src.scrapers.search_results_nr_handler import SearchResultsNrHandler
from src.scrapers.search_results_nr_scraper import SearchResultsNrScraper
from src.settings.settings import Settings


class WebScraper:
    """
    The main class is responsible for the process of setting up and running tasks.
    """

    def __init__(self):
        self.__settings = Settings()

        self.__keywords_handler = KeywordsHandler()
        self.__queries_handler = QueriesHandler(self.__keywords_handler, self.__settings.query_prefix)
        self.__links_scraper = LinksScraper(self.__queries_handler, self.__settings.links_scraper_settings)
        self.__links_handler = LinksHandler(self.__links_scraper)

        self.__search_results_nr_scraper = SearchResultsNrScraper(self.__keywords_handler, self.__queries_handler,
                                                                  self.__settings.search_results_scraper_settings)
        self.__search_results_nr_handler = SearchResultsNrHandler(self.__search_results_nr_scraper)

    def run(self):
        csv_save_links(self.__settings.links_file, self.__links_handler.links)
        csv_save_results_nr(self.__settings.results_file, self.__search_results_nr_handler.search_results)
