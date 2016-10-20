import asyncio
import sys
from abc import ABC, abstractmethod
from collections.abc import Iterable, Sized

PY_35 = sys.version_info >= (3, 5)


class AbstractRouter(ABC):

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def resolve(self, request):
        """Return MATCH_INFO for given request"""


class AbstractMatchInfo(ABC):

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def handler(self, request):
        """Execute matched request handler"""

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def expect_handler(self, request):
        """Expect handler for 100-continue processing"""

    @property  # pragma: no branch
    @abstractmethod
    def http_exception(self):
        """HTTPException instance raised on router's resolving, or None"""

    @abstractmethod  # pragma: no branch
    def get_info(self):
        """Return a dict with additional info useful for introspection"""

    @property  # pragma: no branch
    @abstractmethod
    def nested_apps(self):
        """Stack of nested applications.

        Top level application is not encounted.

        """



class AbstractView(ABC):

    def __init__(self, request):
        self._request = request

    @property
    def request(self):
        return self._request

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def __iter__(self):
        while False:  # pragma: no cover
            yield None

    if PY_35:  # pragma: no branch
        @abstractmethod
        def __await__(self):
            return  # pragma: no cover


class AbstractResolver(ABC):

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def resolve(self, hostname):
        """Return IP address for given hostname"""

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def close(self):
        """Release resolver"""


class AbstractCookieJar(Sized, Iterable):

    def __init__(self, *, loop=None):
        self._loop = loop or asyncio.get_event_loop()

    @abstractmethod
    def clear(self):
        """Clear all cookies."""

    @abstractmethod
    def update_cookies(self, cookies, response_url=None):
        """Update cookies."""

    @abstractmethod
    def filter_cookies(self, request_url):
        """Return the jar's cookies filtered by their attributes."""
