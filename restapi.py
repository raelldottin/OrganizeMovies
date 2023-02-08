import api
'''The API has an undetermine timeout'''

yts_mx = api.MovieEndpoint()

response = yts_mx.list_movies(limit=50, page=2, quality="2160p", minimum_rating="8")
if response:
    response.json()
