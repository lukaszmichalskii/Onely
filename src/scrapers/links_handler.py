from src.scrapers.links_scraper import LinksScraper


class LinksHandler:
    """
    Class responsible for storing gathered links
    """

    def __init__(self, links_scraper: LinksScraper):
        self.__links = links_scraper.scrap_links()

    @property
    def links(self) -> list:
        return self.__links
