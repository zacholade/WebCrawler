from urllib.parse import urlparse


class URL:
    __slots__ = ("scheme", "netloc", "path",
                 "params", "query", "fragment", "_raw_url")

    def __init__(self, raw_url: str):
        """https://docs.python.org/3/library/urllib.parse.html"""
        self.scheme, self.netloc, self.path,\
            self.params, self.query, self.fragment = urlparse(raw_url)
        self._raw_url = raw_url

    @property
    def is_valid(self) -> bool:
        # Bool returns False if string is empty.
        return bool(self.netloc)

    @property
    def fully_qualified_url(self) -> str:
        """
        Returns the fully qualified url for this URL object.
        This can be used to make a request against it.
        """
        return self._raw_url
        # return f"{self.scheme}://{self.netloc}{self.path}"

    def __str__(self) -> str:
        return self.fully_qualified_url

    def __repr__(self) -> str:
        return f"URL({self.fully_qualified_url})"

    def __hash__(self):
        """Allows us to implement __eq__ and still hash object in a Python set"""
        return hash(self.__key())

    def __key(self) -> tuple[str, str, str, str, str, str]:
        """A unique key to identify this url object"""
        return (self.scheme, self.netloc, self.path,
                self.params, self.query, self.fragment)

    def __eq__(self, other) -> bool:
        """Equality can be done through key comparison"""
        if isinstance(other, URL):
            return self.__key() == other.__key()
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
