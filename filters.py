

class Filter:
    def __init__(self, *args, **kwargs):
        ...

    def filter(self, urls: list[str]):
        raise NotImplementedError("Implement in child class.")


class SubDomainFilter(Filter):
    def __init__(self, allowed_domains):
        super().__init__()
        self._allowed_domains = allowed_domains

    def filter(self, urls: list[str]):
        




class