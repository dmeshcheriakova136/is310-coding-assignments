# GETting Culture Across APIs

## API Selected: SWAPI - Star Wars API

I chose SWAPI (https://swapi.dev/) because it is one of the only APIs that has different categories of data to scrape from (people, planets, films, species, vehicles, and starships) and it is the one that is familiar to me.

## How It Works

The `getting_culture.py` script:
1. Fetches character data from SWAPI (Star Wars API)
2. Searches the Europeana API for "Star Wars" related cultural heritage items
3. Uses the character name from SWAPI to find related items in the Europeana collection
4. Displays results using Rich tables
5. Saves combined data to `swapi_europeana_data.json` (with API keys filtered out)
