import unittest

from url import URL


class TestURL(unittest.TestCase):
    def test_hashing(self):
        # Hashing is used for Python set comparison.
        url = "https://www.foo.com/"
        u1 = URL(url)
        u2 = URL(url)
        self.assertEqual(hash(u1), hash(u2))

    def test_is_valid(self):
        valid_urls = [URL("https://www.minibems.com"),
                      URL("http://www.chess.com"),
                      URL("https://www.google.co.uk")]

        invalid_urls = [URL("google.com"),  # Requires http(s):// to be valid.
                        URL("www.google.com"),
                        URL("random_text"),
                        URL("random(dot)com"),
                        URL("."),
                        URL(".com"),
                        URL(" foo "),
                        URL(" ")]

        for url in valid_urls:
            self.assertTrue(url.is_valid)

        for url in invalid_urls:
            self.assertFalse(url.is_valid)

    def test_equality(self):
        url1 = URL("https://google.com/")
        url2 = URL("https://minibems.com/")
        self.assertFalse(url1.__eq__(url2))
        self.assertTrue(url1.__ne__(url2))

    def test_qualified_name(self):
        url_strings = ["https://www.minibems.com",
                       "http://www.minibems.com",
                       "https://www.google.co.uk"]

        for url_string in url_strings:
            url = URL(url_string)
            self.assertEqual(url_string, url.fully_qualified_url)
