from bs4 import BeautifulSoup
from url import URL


class HTMLParser:

    @staticmethod
    def find_all_urls(html) -> set[URL]:
        """
        Given an HTML string, this function returns a list of all domains on the webpage.
        """
        html_soup = BeautifulSoup(html, "html.parser")
        links = html_soup.find_all('a')  # Returns empty list if None found.
        links = set(URL(link.get('href')) for link in links)
        return links


