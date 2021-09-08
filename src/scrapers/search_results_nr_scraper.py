import urllib.parse
import requests

from bs4 import BeautifulSoup

from src.keywords.keywords_handler import KeywordsHandler
from src.queries.queries_handler import QueriesHandler
from src.settings.settings import Settings


class SearchResultsNrScraper:
    """
    Class extract the number of search results
    """

    def __init__(self, keywords: KeywordsHandler, queries: QueriesHandler, headers: dict):
        self.__queries = queries.queries
        self.__keywords = keywords.keywords
        self.__google_url = Settings().google_url
        self.__headers = headers

    def __scrap_search_results_nr(self):
        words = self.__parse_queries(self.__queries)
        url = self.__create_url(words, self.__google_url)
        search_results = self.__search_results(url, self.__headers)

        return search_results

    def organize_results(self) -> dict:
        """
        Organize results in dictionary (pairs keyword -> search results number)
        """
        search_results = {}
        results = self.__scrap_search_results_nr()
        for i in range(len(self.__keywords)):
            search_results[self.__keywords[i]] = results[i]

        return search_results

    def __search_results(self, url: list, headers: dict) -> list:
        """
        Extracting the number of results
        """
        search_results = []
        for u in url:
            html_text = requests.get(u, headers=headers).text
            soup = BeautifulSoup(html_text, 'html.parser')
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
