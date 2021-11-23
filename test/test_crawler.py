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
        ...

    def test_crawler_finds_all_valid_urls(self):
        """
        TODO
        In production I would have wrote tests which pass a url to the
        crawl(url) function inside the Crawler class. I would make sure
        the visited_urls attribute is populated correctly.
        """
        ...

    def test_http_errors(self):
        """
        # TODO
        Would have made sure the application doesn't terminate
        when faced with an HTTP error. Make sure they are handled all handled.
        https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        """
        ...

    def test_maximum_depth(self):
        """
        TODO Make sure maximum depth isn't exceeded.
        Implement a simple MockServer with several pages referencing
        eachother in sequence. Ensure application breaks out of
        recursive _crawl() function by the depth value specified.
        """
