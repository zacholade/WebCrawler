import argparse
import asyncio

from crawler import Crawler
from filters import SubDomainFilter, ValidURLFilter
from logger import setup_logging
from url import URL


async def main(url: str):
    # TODO Allow user to specify filters through command line.
    filters = [
        ValidURLFilter(),
        SubDomainFilter([
            url  # Add option to restrict to other sub domains too.
        ]),
    ]

    # TODO Rate Limit Logic
    number_requests = 10
    per_n_seconds = 5

    max_depth = 10

    s = Crawler(filters, max_depth=max_depth)
    url = URL(url)
    task = asyncio.create_task(s.crawl(url))
    await task

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", type=str, required=True)  # The starting URL
    args = parser.parse_args()
    url: str = args.url

    loop = asyncio.get_event_loop()
    with setup_logging(debug=True):
        loop.run_until_complete(main(url))
    loop.close()

