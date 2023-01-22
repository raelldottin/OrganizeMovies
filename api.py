import session

def list_movies(url: str, endpoint: str, params: dict):
    session.get(url, endpoint, params)
