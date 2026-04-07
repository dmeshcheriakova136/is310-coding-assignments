import requests
import apikey
import os

europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

# Search the Europeana collection for "Alfred Book"
response = requests.get("https://api.europeana.eu/record/v2/search.json", params={"wskey": europeana_api_key, "query": "Alfred Book", "rows": 1000})
data = response.json()
print(f"Got {data['totalResults']} total results")
print()
print(data['items'][0])
print()
print(f"First item browser link: {data['items'][0]['guid']}")

# Entity API - search for people (agents)
response = requests.get("https://api.europeana.eu/entity/suggest", params={"wskey": europeana_api_key, "text": "Tolkien", "type": "agent"})
print()
print('tolkien', response.json())

# Entity API - search for concepts
response = requests.get("https://api.europeana.eu/entity/suggest", params={"wskey": europeana_api_key, "text": "Literature", "type": "concept"})
print()
print('literature', response.json())

# Entity API - search for places
response = requests.get("https://api.europeana.eu/entity/suggest", params={"wskey": europeana_api_key, "text": "London", "type": "place"})
print()
print('london', response.json())
