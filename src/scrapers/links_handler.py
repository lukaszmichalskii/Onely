from src.scrapers.links_scraper import LinksScraper


class LinksHandler:

    def __init__(self, links_scraper: LinksScraper):
        self.__links_scraper = links_scraper
        self.__links = self.__links_scraper.scrap_links()

    @property
    def links(self):
        return self.__links
