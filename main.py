import api
'''The API has an undetermine timeout'''
movie_list = api.MovieList(limit=50, page=2, quality="2160p", minimum_rating="8")

response = movie_list.list_movies()
print(response.json())
