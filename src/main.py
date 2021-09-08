from src.file_read_save.csv_save import csv_save_links
from src.keywords.keywords_handler import KeywordsHandler
from src.queries.queries_handler import QueriesHandler
from src.scrapers.links_handler import LinksHandler
from src.scrapers.links_scraper import LinksScraper

if __name__ == '__main__':
    lh = LinksHandler(LinksScraper(QueriesHandler(KeywordsHandler())))
    print(lh.links)
    csv_save_links('links.csv', lh.links)
