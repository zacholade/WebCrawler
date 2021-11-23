import asyncio
import logging
import aiohttp

from filters import Filter
from html_parser import HTMLParser
from logger import LoggingMixin
from url import URL

logging.getLogger("root")


class Scraper(LoggingMixin):
    def __init__(self, url_filters: list[Filter]):
        self._url_filters = url_filters
        self._client_session = aiohttp.ClientSession()
        self._html_parser = HTMLParser
        self._visited_urls: set[URL] = set()

    async def crawl(self, url: URL):
        """
        Starting URL to crawl.
        """
        await asyncio.create_task(self._crawl(url))

    async def _crawl(self, url: URL):
        print(url)
        # If statement in case we get an HTTP response Error.
        if html := await self.make_request(url):
            # Extract urls from HTML href a tags.
            unfiltered_urls = self._html_parser.find_all_urls(html)
            # Filter URLS.
            filtered_urls = self._filter_urls(unfiltered_urls)
            # Remove URLS which have already been visited.
            urls_to_visit = filtered_urls - self._visited_urls
            print(f"Visited {url.fully_qualified_url} and "
                  f"found {len(unfiltered_urls)} URL(s). "
                  f"After filtering there were {len(filtered_urls)} URL(s), "
                  f"of which after removing already visited was: {len(urls_to_visit)} URL(s), ",
                  f"which are as follows: {list(map(str, urls_to_visit))}")

            if len(urls_to_visit) > 0:
                print('IIIIIIIIIIIIII')
                await asyncio.sleep(3)
                # self._visited_urls = self._visited_urls.union(urls_to_visit)
                print(self._visited_urls)
                await asyncio.gather(*[self._crawl(u) for u in urls_to_visit])

    async def make_request(self, url: URL) -> str:
        if not url.is_valid:
            raise ValueError(f"URL {url} format is not valid")

        self._visited_urls.add(url)
        try:
            async with self._client_session.get(url.fully_qualified_url, allow_redirects=True) as response:
                response.raise_for_status()
                html = await response.text()
                return html
        except aiohttp.ClientConnectionError as e:
            self.logger.warning(e)

    def _filter_urls(self, urls: set[URL]):
        for url_filter in self._url_filters:
            urls = url_filter(urls)

        return urls
