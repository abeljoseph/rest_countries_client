# 🌍 REST Countries Python Client

A lightweight Python client for interacting with the [REST Countries API](https://restcountries.com/), built using `requests` and `pydantic`.

Supports structured queries by country name, code, currency, and language — with validation and deserialization into typed `CountryInfo` models.

---

## 📦 Features

- Search countries by:
    - **Name**
    - **Alpha code** (2- or 3-letter)
    - **Currency code** (e.g. `CAD`)
    - **Language code** (e.g. `eng`, `fra`)
- Get **bordering countries** by code
- Find **countries sharing the same language**
- Parses responses into rich, nested `pydantic` models
- Raises informative errors on API failure (e.g., 404)

---

## 🔧 Installation

    pip install requests pydantic

---

## 🚀 Quick Start

### Import and use any of the clients:

    from countries import NameSearch, CodeSearch, CurrencySearch, LanguageSearch

    canada = NameSearch()("canada")[0]
    print(canada.name.common)  # → "Canada"

    usa = CodeSearch()("US")[0]
    print(usa.capital)         # → ["Washington, D.C."]

---

### Bordering Countries

    from countries import GetBorderInfo

    borders = GetBorderInfo()("FRA")  # Get countries bordering France
    for country in borders:
        print(country.name.common)

---

### Countries That Speak the Same Language

    from countries import GetCountriesSpeakingSameLanguage

    neighbors = GetCountriesSpeakingSameLanguage()("CAN")
    for country in neighbors:
        print(f"{country.name.common}: {list(country.languages.values())}")

---

## 🎯 Supported Query Types

| Class                               | Input Example         | Description                            |
|-------------------------------------|------------------------|----------------------------------------|
| `NameSearch()`                      | `"canada"`             | Search by full or partial name         |
| `CodeSearch()`                      | `"CA"` or `"CAN"`      | ISO alpha-2 or alpha-3 code            |
| `CurrencySearch()`                  | `"CAD"`                | Currency code                          |
| `LanguageSearch()`                  | `"fra"`                | Language code                          |
| `GetBorderInfo()`                   | `"FRA"`                | Countries sharing a border             |
| `GetCountriesSpeakingSameLanguage()`| `"CAN"`                | Countries with overlapping languages   |

All queries return a `list[CountryInfo]`.

---

## 📂 File Structure

    countries/
    ├── countries.py      # Client classes
    ├── models.py         # Pydantic data models
    └── README.md         # This file

---

## 🙋 Author

Created by **Abel Joseph**
