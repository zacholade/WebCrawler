import unittest

from filters import *


class TestFilters(unittest.TestCase):
    def test_abc_filter(self):
        self.filter = Filter()
        with self.assertRaises(NotImplementedError):
            self.filter(set())

    def test_subdomain_filter(self):
        self.subdomain_filter = SubDomainFilter([
            "https://www.minibems.com/",
        ])

        # These should not be removed by the filter
        allowed_urls = {
            URL("https://www.minibems.com/"),
            URL("https://www.minibems.com/support/"),
            URL("https://www.minibems.com/blog-events/events/"),
        }

        # These should be removed by the filter
        blocked_urls = {
            URL("https://www.google.com/"),
            URL("https://www.admin.minibems.com/"),
            URL("randomtext"),
            URL(".com"),
        }

        all_urls = allowed_urls | blocked_urls

        # Test filtering using __call__ method
        filtered = self.subdomain_filter(all_urls)
        self.assertEqual(allowed_urls, filtered)

        # Test filtering using filter method
        filtered = self.subdomain_filter.filter(all_urls)
        self.assertEqual(allowed_urls, filtered)
