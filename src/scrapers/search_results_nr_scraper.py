import urllib.parse
import requests

from bs4 import BeautifulSoup

from src.keywords.keywords_handler import KeywordsHandler
from src.queries.queries_handler import QueriesHandler


class SearchResultsNrScraper:
    """
    Class extract the number of search results
    """

    def __init__(self, keywords: KeywordsHandler, queries: QueriesHandler, search_results_scraper_settings: dict):
        self.__queries = queries.queries
        self.__keywords = keywords.keywords
        self.__settings = search_results_scraper_settings

    def __scrap_search_results_nr(self) -> list:
        """
        Class method, extracts raw searches number
        """
        words = self.__parse_queries(self.__queries)
        url = self.__create_url(words, self.__settings['google_url'])
        search_results = self.__search_results(url, self.__settings['desktop_user_agent'])

        return search_results

    def organize_results(self) -> dict:
        """
        Organize results in dictionary (pairs -> keyword: search results number)
        """
        search_results = {}
        results = self.__scrap_search_results_nr()
        for i in range(len(self.__keywords)):
            search_results[self.__keywords[i]] = results[i]

        return search_results

    def __search_results(self, url: list, headers: dict) -> list:
        """
        Extracting the number of results from html text
        """
        search_results = []
        for u in url:
            html_text = requests.get(u, headers=headers).text
            soup = BeautifulSoup(html_text, 'lxml')  # alternative parser e.g. 'html.parser', lxml it's a lot faster
            result_text = soup.find('div', {'id': 'result-stats'}).text
            r = result_text.split()
            r.remove(r[0])
            r.remove(r[-1])
            r.remove(r[-1])
            r.remove(r[-1])
            result = ''.join(r)
            search_results.append(result)

        return search_results

    def __create_url(self, queries: list, google_url: str) -> list:
        """
        Creating list with url addresses
        """
        url = []
        for q in queries:
            url.append(google_url + q)

        return url

    def __parse_queries(self, queries: list) -> list:
        """
        Parsing the query to match the URL form
        """
        words = []
        for query in queries:
            word = urllib.parse.quote_plus(query)
            words.append(word)

        return words
