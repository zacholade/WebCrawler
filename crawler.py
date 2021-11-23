import asyncio

import aiohttp

from filters import Filter
from html_parser import HTMLParser
from logger import LoggingMixin
from url import URL


class Crawler(LoggingMixin):
    def __init__(self, url_filters: list[Filter], max_depth: int):
        self._url_filters = url_filters
        self._client_session = aiohttp.ClientSession()
        self._html_parser = HTMLParser
        self._visited_urls: set[URL] = set()
        self._max_depth: int = max_depth

    async def crawl(self, url: URL):
        """
        Starting URL to crawl.
        """
        self._visited_urls.add(url)
        await asyncio.create_task(self._crawl(url, current_depth=0))

    async def _crawl(self, url: URL, current_depth):
        if current_depth > self._max_depth:
            return

        # If statement in case we get an HTTP response Error.
        if html := await self._make_request(url):
            # TODO do something with the HTML returned? Scrape? Save it?

            # Extract urls from HTML href a tags.
            unfiltered_urls = self._html_parser.find_all_urls(html)
            # Filter URLS.
            filtered_urls = self._apply_filters(unfiltered_urls)
            # Remove URLS which have already been visited.
            urls_to_visit = filtered_urls - self._visited_urls
            self.logger.info(f"Visited {url.fully_qualified_url} and "
                  f"found {len(unfiltered_urls)} URL(s). "
                  f"After filtering there were {len(filtered_urls)} URL(s), "
                  f"of which after removing already visited was: {len(urls_to_visit)} URL(s)")

            if len(urls_to_visit) > 0:
                # TODO wrap function call with some sort of rate limiter FIFO queue.
                await asyncio.gather(*[self._crawl(u, current_depth + 1) for u in urls_to_visit])

    async def _make_request(self, url: URL) -> str:
        self._visited_urls.add(url)

        if not url.is_valid:
            raise ValueError(f"URL {url} format is not valid")

        try:
            async with self._client_session.get(url.fully_qualified_url, allow_redirects=True) as response:
                response.raise_for_status()
                html = await response.text()
                return html
        except (aiohttp.ClientConnectionError, aiohttp.ClientResponseError) as e:
            self.logger.warning(f"Connection Error: {e}")

    def _apply_filters(self, urls: set[URL]):
        for url_filter in self._url_filters:
            urls = url_filter(urls)

        return urls
