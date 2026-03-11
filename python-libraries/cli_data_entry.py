from rich.console import Console
from rich.table import Table
import csv

console = Console()

console.print("Here's a table of U.S. Immigration Laws:")

table = Table(title="U.S. Immigration Laws", show_lines=True)

table.add_column("Law Name", style="cyan")
table.add_column("Year", style="magenta")
table.add_column("Key Change", style="green")

table.add_row("Immigration Act", "1924", "Banned Chinese laborers")
table.add_row("Hart-Celler Act", "1965", "Removed national origin quotas")
table.add_row("Chinese Exclusion Act", "1882", "set national origin quotas")

console.print(table)

console.print("Now, do some research and add a new law to the table:", style="bold green")

while True:
    input_law_name = input("Enter the law name: ")
    input_year = input("Enter the year: ")
    input_key_change = input("Enter a brief description of what the law changed: ")
    input_confirm = input("Does it look correct? (y/n): ")
    if input_confirm == "y":                                                                                                       
      table.add_row(input_law_name, input_year, input_key_change)                                                                
      with open("/Users/dariam/Desktop/IS310/python-libraries/immigration_laws.csv", "w", newline="") as file:                   
          writer = csv.writer(file)                                                                                              
          writer.writerow(["Law Name", "Year", "Key Change"])                                                                    
          for i in range(len(table.rows)):
              writer.writerow([col._cells[i] for col in table.columns])
      console.print(table)
      console.print("Congratulations! You've added a new law to the table:", style="bold green")
      console.print("Data saved to: /Users/dariam/Desktop/IS310/python-libraries/immigration_laws.csv", style="bold green")
      break
    else:
        console.print("Sorry, can you try again?", style="bold red")

