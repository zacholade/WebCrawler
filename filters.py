from urllib.parse import urlparse

from url import URL


class Filter:
    def __call__(self, *args):
        return self.filter(*args)

    def filter(self, urls: set[URL]):
        raise NotImplementedError("Implement in child class.")


class ValidURLFilter(Filter):
    """
    Removes invalid URL objects from a set of URL objects by using
    the is_valid attribute of the URL class.
    """
    def filter(self, urls: set[URL]):
        return set(filter(lambda url: url.is_valid, urls))


class SubDomainFilter(Filter):
    """
    Filters out all URLS in a given set of URLS that do not belong
    to the same subdomain as the one specified by the allowed_domains
    parameter.
    """
    def __init__(self, allowed_domains: list[str]):
        super().__init__()
        # urlparse returns NamedTuple(scheme, netloc, path,
        # params, query, fragment)
        # It is used to extract the domain and subdomain
        self._allowed_domains = [URL(domain).netloc for
                                 domain in allowed_domains]

    def filter(self, urls: set[URL]):
        # The filter function. Returns True if on same subdomain. False otherwise
        urls = set(filter(lambda url:
                          True if url.netloc in self._allowed_domains else False,
                          urls))
        return urls

