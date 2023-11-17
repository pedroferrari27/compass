import requests

# start a session id
api_key ="f195fd8c9afef0db2bf8136e5452b574"

url = "https://api.themoviedb.org/3/authentication/token/new"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTk1ZmQ4YzlhZmVmMGRiMmJmODEzNmU1NDUyYjU3NCIsInN1YiI6IjY1NDkyODI5NmJlYWVhMDBjOWZkNzI5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TK_o1CliJTUqQ9x_q353CkHopwkxrxb_eGK9b-ZiaEc"
}

response = requests.get(url, headers=headers)

response_data = response.json()
request_token = response_data.get("request_token")



#get list
import requests

url = "https://api.themoviedb.org/4/account/654928296beaea00c9fd7297/lists?page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTk1ZmQ4YzlhZmVmMGRiMmJmODEzNmU1NDUyYjU3NCIsInN1YiI6IjY1NDkyODI5NmJlYWVhMDBjOWZkNzI5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TK_o1CliJTUqQ9x_q353CkHopwkxrxb_eGK9b-ZiaEc"
}

response = requests.get(url, headers=headers)

print(response.text)

response_data = response.json()
list = response_data['results'][0]['account_object_id']

#adding our movies to the list

print("\n")


list_id = '8277611'


movie_id = 'tt0000591'

api_key = "f195fd8c9afef0db2bf8136e5452b574"


url = f'https://api.themoviedb.org/3/list/{list_id}/add_item'

params = {
    'api_key': api_key,
}

payload = {
    'media_id': movie_id,
}

# Make the POST request to add the movie to the list
response = requests.post(url, params=params, json=payload)

# Check if the request was successful (HTTP status code 20X)
if response.status_code // 100 == 2:
    print(f"Movie with ID {movie_id} added to list with ID {list_id}")
else:
    print(f"Failed to add the movie to the list. Status Code: {response.status_code}")
    print(response.text)
#

