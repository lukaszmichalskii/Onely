from src.scrapers.search_results_nr_scraper import SearchResultsNrScraper


class SearchResultsNrHandler:

    def __init__(self, search_results_nr_scraper: SearchResultsNrScraper):
        self.__search_results = search_results_nr_scraper.organize_results()

    @property
    def search_results(self):
        return self.__search_results
