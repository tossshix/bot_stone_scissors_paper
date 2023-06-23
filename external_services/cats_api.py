import requests

API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
cats_link = requests.get(API_CATS_URL)
