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


## Claude Code Prompts
⏺ 1. I need to get this API from the website. explain step by step what I should do
  2. from here https://swapi.dev/documentation                                                                
  3. how to make a request? whats the code for it?                                                            
  4. for step 3 - do I need to find a specific query or what do you mean by request?                          
  5. is this about the right code that I need to get?? (showing terminal output)                              
  6. check this instructions and tell me what i missed (pasting full assignment)                              
  7. can you make sure that Europeana API is in the same style as the code I wrote for SWAPI?                 
  8. explain to me this part (about apikey/os.environ code)                                                   
  9. like how it wont appear? can you tell me                                                                 
  10. i ran this code in my getting_culture file... what should I do to hide my key?                          
  11. lets get back to the assignment - what should I do next?                                                
  12. how to combine them in one script?                                                                      
  13. what is swapi data =?                                                                                   
  14. can I already there in the dictionary name it inside?                                                   
  15. i mean like this character_name = swapi_data['name=luke']                                               
  16. look now (showing updated code)                                                                         
  17. this is all of my code (pasting full script)                                                            
  18. sorry how can I manage this??? (overwhelmed by raw JSON output)                                         
  19. use Rich library to make it more beautiful                                                              
  20. extract this rich code to json file. walk me through the process                                        
  21. should it be separate python file                                                                       
  22. how to open json file                                                                                   
  23. yes (confirming fixes to JSON saving)                                                                   
  24. yes, push it to github here... and in readme say that its SWAPI... 
