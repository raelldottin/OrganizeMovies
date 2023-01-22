import session

class MovieList(object):
    def __init__(self, limit=20, page=1, quality="All", minimum_rating="0", query_term="", genre="All", sort_by="year", order_by="desc", with_rt_ratings="false"):
        self.endpoint_params = {
            "limit": limit,
            "page":  page,
            "quality": quality,
            "minimum_rating": minimum_rating,
            "query_term": query_term,
            "genre": genre,
            "sort_by": sort_by,
            "order_by": order_by,
            "with_rt_ratings": with_rt_ratings,
        }

    def list_movies(self) -> session.requests.Response:
        return session.query(url="https://yts.mx", endpoint="/api/v2/list_movies.json", params=self.endpoint_params)
