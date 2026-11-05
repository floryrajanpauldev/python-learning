import requests
import json

url = "https://itunes.apple.com/search?entity=song&limit=2&term=weezer"

response = requests.get(url)
print(response.status_code) # this will print the status code of the response
#print(response.json())

data = response.json()

#print(json.dumps(data, indent=2)) # this will print the json data in a pretty format 
#indent=2 will indent the json data by 2 spaces for better readability

for result in data["results"]:
    print(result["trackName"]) # this will print the track name of the first result
    print(result["artistName"]) # this will print the artist name of the first result
    print(result["collectionName"]) # this will print the collection name of the first result
    print(result["releaseDate"]) # this will print the release date of the first result
    print(result["primaryGenreName"]) # this will print the primary genre name of the first result