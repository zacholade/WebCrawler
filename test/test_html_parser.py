import unittest

from html_parser import HTMLParser
from url import URL


class TestHTMLParser(unittest.TestCase):
    def test_find_all_urls(self):
        html = """<!DOCTYPE html>
<html>
<body>

<a href="https://www.foo.com/">This contains a link</a>
<h2>This is an HTML unittest site</h2>
<p>Where HTML links are defined with the a tag</p>

<a href="https://www.examplelink.com/">This contains a link</a>

</body>
</html>
"""
        links = {URL("https://www.examplelink.com/"),
                 URL("https://www.foo.com/")}
        found_links = HTMLParser.find_all_urls(html)
        self.assertEqual(links, found_links)
