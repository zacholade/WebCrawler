from crawler import Crawler
import unittest


class TestCrawler(unittest.TestCase):
    def test_crawl(self):
        ...

    def test_url_only_visits_once(self):
        """
        # TODO In practice I would:
        - Use the MockServer class and create some HTML templates.
        - Log in the class how many times each route has a GET request made.
        - Make sure that each page on the mockserver only has 1 request made
            by using the counter dictionary in that class.
        """
