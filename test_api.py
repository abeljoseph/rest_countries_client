from api import *

class TestAPI:
    def setup_method(self):
        country_info = [
            {
                "name": {
                    "common": "India",
                    "official": "Republic of India",
                    "nativeName": {
                        "eng": {"official": "Republic of India", "common": "India"},
                        "hin": {"official": "भारत गणराज्य", "common": "भारत"},
                        "tam": {"official": "இந்தியக் குடியரசு", "common": "இந்தியா"},
                    },
                },
                "tld": [".in"],
                "cca2": "IN",
                "ccn3": "356",
                "cioc": "IND",
                "independent": True,
                "status": "officially-assigned",
                "unMember": True,
                "currencies": {"INR": {"symbol": "₹", "name": "Indian rupee"}},
                "idd": {"root": "+9", "suffixes": ["1"]},
                "capital": ["New Delhi"],
                "altSpellings": ["IN", "Bhārat", "Republic of India", "Bharat Ganrajya", "இந்தியா"],
                "region": "Asia",
                "subregion": "Southern Asia",
                "languages": {"eng": "English", "hin": "Hindi", "tam": "Tamil"},
                "latlng": [20.0, 77.0],
                "landlocked": False,
                "borders": ["BGD", "BTN", "MMR", "CHN", "NPL", "PAK"],
                "area": 3287590.0,
                "demonyms": {
                    "eng": {"f": "Indian", "m": "Indian"},
                    "fra": {"f": "Indienne", "m": "Indien"},
                },
                "cca3": "IND",
                "translations": {
                    "ara": {"official": "جمهورية الهند", "common": "الهند"},
                    "bre": {"official": "Republik India", "common": "India"},
                    "ces": {"official": "Indická republika", "common": "Indie"},
                    "cym": {"official": "Republic of India", "common": "India"},
                    "deu": {"official": "Republik Indien", "common": "Indien"},
                    "est": {"official": "India Vabariik", "common": "India"},
                    "fin": {"official": "Intian tasavalta", "common": "Intia"},
                    "fra": {"official": "République de l'Inde", "common": "Inde"},
                    "hrv": {"official": "Republika Indija", "common": "Indija"},
                    "hun": {"official": "Indiai Köztársaság", "common": "India"},
                    "ind": {"official": "Republik India", "common": "India"},
                    "ita": {"official": "Repubblica dell'India", "common": "India"},
                    "jpn": {"official": "インド共和国", "common": "インド"},
                    "kor": {"official": "인도 공화국", "common": "인도"},
                    "nld": {"official": "Republiek India", "common": "India"},
                    "per": {"official": "جمهوری هندوستان", "common": "هند"},
                    "pol": {"official": "Republika Indii", "common": "Indie"},
                    "por": {"official": "República da Índia", "common": "Índia"},
                    "rus": {"official": "Республика Индия", "common": "Индия"},
                    "slk": {"official": "Indická republika", "common": "India"},
                    "spa": {"official": "República de la India", "common": "India"},
                    "srp": {"official": "Република Индија", "common": "Индија"},
                    "swe": {"official": "Republiken Indien", "common": "Indien"},
                    "tur": {"official": "Hindistan Cumhuriyeti", "common": "Hindistan"},
                    "urd": {"official": "جمہوریہ بھارت", "common": "بھارت"},
                    "zho": {"official": "印度共和国", "common": "印度"},
                },
                "flag": "\ud83c\uddee\ud83c\uddf3",
                "maps": {
                    "googleMaps": "https://goo.gl/maps/WSk3fLwG4vtPQetp7",
                    "openStreetMaps": "https://www.openstreetmap.org/relation/304716",
                },
                "population": 1380004385,
                "gini": {"2011": 35.7},
                "fifa": "IND",
                "car": {"signs": ["IND"], "side": "left"},
                "timezones": ["UTC+05:30"],
                "continents": ["Asia"],
                "flags": {
                    "png": "https://flagcdn.com/w320/in.png",
                    "svg": "https://flagcdn.com/in.svg",
                    "alt": "The flag of India is composed of three equal horizontal bands of saffron, white and green. A navy blue wheel with twenty-four spokes — the Ashoka Chakra — is centered in the white band.",
                },
                "coatOfArms": {
                    "png": "https://mainfacts.com/media/images/coats_of_arms/in.png",
                    "svg": "https://mainfacts.com/media/images/coats_of_arms/in.svg",
                },
                "startOfWeek": "monday",
                "capitalInfo": {"latlng": [28.6, 77.2]},
                "postalCode": {"format": "######", "regex": "^(\\d{6})$"},
            },
            {
                "name": {
                    "common": "Myanmar",
                    "official": "Republic of the Union of Myanmar",
                    "nativeName": {
                        "mya": {"official": "ပြည်ထောင်စု သမ္မတ မြန်မာနိုင်ငံတော်", "common": "မြန်မာ"}
                    },
                },
                "tld": [".mm"],
                "cca2": "MM",
                "ccn3": "104",
                "cioc": "MYA",
                "independent": True,
                "status": "officially-assigned",
                "unMember": True,
                "currencies": {"MMK": {"symbol": "Ks", "name": "Burmese kyat"}},
                "idd": {"root": "+9", "suffixes": ["5"]},
                "capital": ["Naypyidaw"],
                "altSpellings": [
                    "MM",
                    "Burma",
                    "Republic of the Union of Myanmar",
                    "Pyidaunzu Thanmăda Myăma Nainngandaw",
                ],
                "region": "Asia",
                "subregion": "South-Eastern Asia",
                "languages": {"mya": "Burmese"},
                "latlng": [22.0, 98.0],
                "landlocked": False,
                "borders": ["BGD", "CHN", "IND", "LAO", "THA"],
                "area": 676578.0,
                "demonyms": {
                    "eng": {"f": "Burmese", "m": "Burmese"},
                    "fra": {"f": "Birmane", "m": "Birman"},
                },
                "cca3": "MMR",
                "translations": {
                    "ara": {"official": "جمهورية اتحاد ميانمار", "common": "ميانمار"},
                    "bre": {"official": "Republik Unaniezh Myanmar", "common": "Myanmar"},
                    "ces": {"official": "Republika Myanmarský svaz", "common": "Myanmar"},
                    "cym": {"official": "Republic of the Union of Myanmar", "common": "Myanmar"},
                    "deu": {"official": "Republik der Union Myanmar", "common": "Myanmar"},
                    "est": {"official": "Myanmari Liidu Vabariik", "common": "Myanmar"},
                    "fin": {"official": "Myanmarin liiton tasavalta", "common": "Myanmar"},
                    "fra": {"official": "République de l'Union du Myanmar", "common": "Birmanie"},
                    "hrv": {"official": "Republika Unije Mijanmar", "common": "Mijanmar"},
                    "hun": {
                        "official": "Mianmari Államszövetség Köztársasága",
                        "common": "Mianmar",
                    },
                    "ind": {"official": "Republik Persatuan Myanmar", "common": "Myanmar"},
                    "ita": {"official": "Repubblica dell'Unione di Myanmar", "common": "Birmania"},
                    "jpn": {"official": "ミャンマー連邦共和国", "common": "ミャンマー"},
                    "kor": {"official": "미얀마 연방 공화국", "common": "미얀마"},
                    "nld": {"official": "Republiek van de Unie van Myanmar", "common": "Myanmar"},
                    "per": {"official": "اتحادیه جمهوری میانمار", "common": "میانمار"},
                    "pol": {"official": "Republika Związku Mjanmy", "common": "Mjanma"},
                    "por": {"official": "República da União de Myanmar", "common": "Myanmar"},
                    "rus": {"official": "Республика Союза Мьянма", "common": "Мьянма"},
                    "slk": {"official": "Mjanmarská zväzová republika", "common": "Mjanmarsko"},
                    "spa": {"official": "República de la Unión de Myanmar", "common": "Myanmar"},
                    "srp": {"official": "Република Савез Мјанмара", "common": "Мјанмар"},
                    "swe": {"official": "Republiken Unionen Myanmar", "common": "Myanmar"},
                    "tur": {"official": "Myanmar Birliği Cumhuriyeti", "common": "Myanmar"},
                    "urd": {"official": "متحدہ جمہوریہ میانمار", "common": "میانمار"},
                    "zho": {"official": "缅甸联邦共和国", "common": "缅甸"},
                },
                "flag": "\ud83c\uddf2\ud83c\uddf2",
                "maps": {
                    "googleMaps": "https://goo.gl/maps/4jrZyJkDERUfHyp26",
                    "openStreetMaps": "https://www.openstreetmap.org/relation/50371",
                },
                "population": 54409794,
                "gini": {"2017": 30.7},
                "fifa": "MYA",
                "car": {"signs": ["BUR"], "side": "right"},
                "timezones": ["UTC+06:30"],
                "continents": ["Asia"],
                "flags": {
                    "png": "https://flagcdn.com/w320/mm.png",
                    "svg": "https://flagcdn.com/mm.svg",
                    "alt": "The flag of Myanmar is composed of three equal horizontal bands of yellow, green and red, with a large five-pointed white star superimposed at the center of the field.",
                },
                "coatOfArms": {
                    "png": "https://mainfacts.com/media/images/coats_of_arms/mm.png",
                    "svg": "https://mainfacts.com/media/images/coats_of_arms/mm.svg",
                },
                "startOfWeek": "monday",
                "capitalInfo": {"latlng": [19.76, 96.07]},
                "postalCode": {"format": "#####", "regex": "^(\\d{5})$"},
            },
        ]
        self.india_info = CountryInfo.model_validate(country_info[0])
        self.myanmar_info = CountryInfo.model_validate(country_info[1])

    def test_name_search(self):
        ns = NameSearch()
        
        india_info = ns("Republic of India")[0]
        assert india_info == self.india_info

        myanmar_info = ns("Myanmar")[0]
        assert myanmar_info == self.myanmar_info

    def test_code_search(self):
        cs = CodeSearch()

        india_info = cs("IND")[0]
        assert india_info == self.india_info

        myanmar_info = cs("MYA")[0]
        assert myanmar_info == self.myanmar_info


    def test_currency_search(self):
        cs = CurrencySearch()

        inr_info_list = cs("INR")
        cioc_list = [x.cioc for x in inr_info_list]

        assert "IND" in cioc_list

    def test_language_search(self):
        ls = LanguageSearch()

        hindi_info_list = ls("Hindi")
        cioc_list = [x.cioc for x in hindi_info_list]

        assert "IND" in cioc_list
    
    def test_border_info_list(self):
        gb = GetBorderInfo()

        usa_bordering = gb("USA")
        cioc_list = [x.cioc for x in usa_bordering]

        assert "CAN" in cioc_list
        assert "MEX" in cioc_list

