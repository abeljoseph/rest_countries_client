from pydantic import BaseModel, Field



class NativeName(BaseModel):
    official: str
    common: str


class Name(BaseModel):
    common: str
    official: str
    nativeName: dict[str, NativeName]


class CurrencyDetail(BaseModel):
    symbol: str | None = None
    name: str | None = None


class CountryInfo(BaseModel):
    name: Name
    cioc: str = Field(description="code")
    status: str
    unMember: bool
    currencies: dict[str, CurrencyDetail] | None = None
    capital: list[str] | None = None
    altSpellings: list[str]
    region: str
    languages: dict[str, str]
    latlng: list[float]
    landlocked: bool
    borders: list[str] | None = None
    area: float
    population: int
    timezones: list[str]
    continents: list[str]
