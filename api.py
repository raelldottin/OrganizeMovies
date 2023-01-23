import session

def list_movies(limit=20, page=1, quality="All", minimum_rating="0",
                 query_term="", genre="All", sort_by="year", order_by="desc",
                 with_rt_ratings="false", endpoint="/api/v2/list_movies.json",
                 params=dict()) -> session.requests.Response:
    endpoint_params = {
        "limit": limit, "page":  page, "quality": quality,
        "minimum_rating": minimum_rating, "query_term": query_term,
        "genre": genre, "sort_by": sort_by, "order_by": order_by,
        "with_rt_ratings": with_rt_ratings,
    }

    if endpoint != "/api/v2/list_movies.json":
        if params:
            return session.query(url="https://yts.mx", endpoint=endpoint, params=params)
        else:
            return session.query(url="https://yts.mx", endpoint=endpoint, params=dict())
    else:
        return session.query(url="https://yts.mx", endpoint=endpoint, params=endpoint_params)

def movie_details(imdb_id=str(), with_images=str(), with_cast=str(),
                  endpoint="/v2/movie_details.json"
                  ) -> session.requests.Response:
    endpoint_params = {
        "imdb_id": imdb_id, "with_images": with_images, "with_cast": with_cast,
    }

    if endpoint != "/api/v2/movie_details.json":
        return session.query(url="https://yts.mx", endpoint=endpoint, params=dict())
    else:
        return session.query(url="https://yts.mx", endpoint=endpoint, params=endpoint_params)
