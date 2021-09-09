class Settings:
    """
    Class responsible for storing and managing settings
    """

    def __init__(self):
        self.__query_prefix = 'site:https://www.searchenginejournal.com/ '

        self.__searches_web_site_filter = 'www.searchenginejournal.com'
        self.__desktop_user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                                   'KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

        # by default Google shows a total of 10 search results per page.
        # If we want more searches increase values
        self.__searches_nr = 10
        self.__links_per_page = 10
        # A lapse too long will make the search slow,
        # but a lapse too short may cause Google to block your IP.
        self.__delay = 2

        self.__google_url = 'https://www.google.com/search?q='

        self.__links_file = 'links.csv'
        self.__results_file = 'results.csv'

    @property
    def query_prefix(self) -> str:
        return self.__query_prefix

    @property
    def search_results_scraper_settings(self) -> dict:
        settings = {'desktop_user_agent': self.__desktop_user_agent,
                    'google_url': self.__google_url}

        return settings

    @property
    def links_scraper_settings(self) -> dict:
        settings = {'links_per_page': self.__links_per_page,
                    'web_site_filter': self.__searches_web_site_filter,
                    'searches_nr': self.__searches_nr,
                    'delay': self.__delay}

        return settings

    @property
    def links_file(self) -> str:
        return self.__links_file

    @property
    def results_file(self) -> str:
        return self.__results_file
