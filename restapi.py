import api
'''The API has an undetermine timeout'''

response = api.list_movies(limit=50, page=2, quality="2160p", minimum_rating="8")
print(response.json())
