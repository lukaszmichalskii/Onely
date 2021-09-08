class Settings:
    """
    Class responsible for storing settings
    """

    def __init__(self):
        self.query_prefix = 'site:https://www.searchenginejournal.com/ '

        self.searches_web_site_filter = 'www.searchenginejournal.com'
        self.desktop_user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                                 'KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
        self.searches_nr = 10

        self.google_url = 'https://www.google.com/search?q='

        self.links_file = 'links.csv'
        self.results_file = 'results.csv'
