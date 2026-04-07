import requests
import apikey
import os
import json
from rich.console import Console
from rich.table import Table

console = Console()

# --- SWAPI ---
console.print("\n[bold cyan]===== SWAPI (Star Wars API) =====[/bold cyan]\n")

response = requests.get("https://swapi.dev/api/people/1/")
name_swapi_data = response.json()

table = Table(title="SWAPI Character Info")
table.add_column("Field", style="bold magenta")
table.add_column("Value", style="green")
for key, value in name_swapi_data.items():
    table.add_row(key, str(value))
console.print(table)

# --- Europeana API ---
console.print("\n[bold cyan]===== Europeana API =====[/bold cyan]\n")

europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

response = requests.get("https://api.europeana.eu/record/v2/search.json", params={"wskey": europeana_api_key, "query": "Star Wars", "rows": 10})
europeana_data = response.json()

table = Table(title="Europeana Search: 'Star Wars'")
table.add_column("#", style="bold")
table.add_column("Title", style="green")
table.add_column("Type", style="cyan")
table.add_column("Country", style="yellow")
for i, item in enumerate(europeana_data['items'], 1):
    title = item.get('title', ['Unknown'])[0]
    item_type = item.get('type', 'Unknown')
    country = item.get('country', ['Unknown'])[0]
    table.add_row(str(i), title, item_type, country)
console.print(table)

# --- Searching for a specific name from SWAPI in Europeana ---
character_name = name_swapi_data['name']
console.print(f"\n[bold cyan]===== Europeana Search: '{character_name}' =====[/bold cyan]\n")

response = requests.get("https://api.europeana.eu/record/v2/search.json", params={"wskey": europeana_api_key, "query": character_name, "rows": 10})
europeana_character_data = response.json()

table = Table(title=f"Europeana Search: '{character_name}'")
table.add_column("#", style="bold")
table.add_column("Title", style="green")
table.add_column("Type", style="cyan")
table.add_column("Country", style="yellow")
for i, item in enumerate(europeana_character_data['items'], 1):
    title = item.get('title', ['Unknown'])[0]
    item_type = item.get('type', 'Unknown')
    country = item.get('country', ['Unknown'])[0]
    table.add_row(str(i), title, item_type, country)
console.print(table)

# --- Saving JSON file ---
console.print(f"\n[bold cyan]===== Saving JSON file =====[/bold cyan]\n")

# Combine both API results into one dictionary
combined_data = {
    "swapi_character": name_swapi_data,
    "europeana_star_wars": europeana_data['items'],
    "europeana_character_search": europeana_character_data['items']
}

# Filter out API key from the data before saving
combined_json = json.dumps(combined_data, indent=2)
combined_json = combined_json.replace(europeana_api_key, "HIDDEN_API_KEY")
combined_data = json.loads(combined_json)

with open("swapi_europeana_data.json", "w") as f:
    json.dump(combined_data, f, indent=2)

console.print("[green]Saved to swapi_europeana_data.json[/green]")