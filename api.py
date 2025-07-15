"""Client interacting with REST Countries API. Support search by name, code, currency, and language."""

import requests

from models import *


class CountriesAPI:
    """Base class for the REST Countries API"""

    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1/"

    def __call__(self, path: str):
        response = requests.get(self.base_url + path.lstrip("/"))
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()


class NameSearch(CountriesAPI):
    def __call__(self, name: str) -> list[CountryInfo]:
        response = super().__call__(f"name/{name}")
        return [CountryInfo.model_validate(c) for c in response]


class CodeSearch(CountriesAPI):
    def __call__(self, code: str) -> list[CountryInfo]:
        response = super().__call__(f"alpha/{code}")
        return [CountryInfo.model_validate(c) for c in response]


class CurrencySearch(CountriesAPI):
    def __call__(self, cur: str) -> list[CountryInfo]:
        response = super().__call__(f"currency/{cur}")
        return [CountryInfo.model_validate(c) for c in response]


class LanguageSearch(CountriesAPI):
    def __call__(self, lang: str):
        response = super().__call__(f"lang/{lang}")
        return [CountryInfo.model_validate(x) for x in response]


class GetBorderInfo:
    """Given a country code, return a list of CountryInfo of all of the neighbouring countries"""

    def __call__(self, code: str) -> list[CountryInfo]:
        cs = CodeSearch()
        border_codes = cs(code)[0].borders

        response = []

        for bdr_code in border_codes:
            response.extend(cs(bdr_code))

        return response


class GetCountriesSpeakingSameLanguage:
    """Given a country code, return a list of CountryInfo of all the countries who speak the same language"""

    def __call__(self, code: str) -> list[CountryInfo]:
        cs = CodeSearch()
        lang_list = cs(code)[0].languages.keys()

        countries = []
        ls = LanguageSearch()

        for lang in lang_list:
            countries.extend(ls(lang))

        return countries
