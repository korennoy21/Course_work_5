import abc
import requests


class ApiClient(abc.ABC):
    @property
    @abc.abstractmethod
    def base_url(self) -> str:
        pass

    def _get(self, url: str, params=None) -> dict:
        if params is None:
            params = {}
        full_url = self.base_url + url
        response = requests.get(full_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
