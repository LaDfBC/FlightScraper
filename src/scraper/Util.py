from bs4 import BeautifulSoup, NavigableString, Tag
import requests

def build_expedia_url(departure_airport_code, arrival_airport_code):
    url = "https://www.expedia.com/Flights-Search?trip=roundtrip%leg1=from%3A("
    url += departure_airport_code
    url += ")%2Cto%3A("
    url += arrival_airport_code
    url += ")%2Cdeparture%3A01%2F12%2F2018TANYT&leg2=from$3A("
    url += arrival_airport_code
    url += ")%2Cto%3A("
    url += departure_airport_code
    url += ")%2Cdeparture%3A01%2F18%2F2018TANYT&passengers=adults%3A2%2Cchildren%3A0%2C" \
           "seniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com"

    return url

