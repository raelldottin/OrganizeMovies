import bs4 
import api
import os
import time
import random

global endpoint, list_of_movies, movies_indexes, params, download_links

endpoint='/browse-movies/0/2160p/all/8/year/0/en'
list_of_movies = list()
movies_indexes = [endpoint,]
params = dict()

def get_indexes() -> None:
    global endpoint, movies_indexes

    html = api.list_movies(endpoint=endpoint, params=dict())
    time.sleep(random.uniform(5.0, 10.0))
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    for link in soup('a', href=True):
        if endpoint in link['href']:
            if link['href'] not in movies_indexes:
                movies_indexes.append(link['href'])

def get_download_links() -> None:
    global endpoint, list_of_movies, download_links

    print(f'{endpoint=}\t{params=}')
    if params:
        html = api.list_movies(endpoint=endpoint, params=params)
    else:
        html = api.list_movies(endpoint=endpoint, params=dict())
    time.sleep(random.uniform(5.0, 10.0))
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    for link in soup('a', href=True):
        if 'https://yts.mx/movies/' in link['href']:
            if link['href'] not in list_of_movies:
                list_of_movies.append(link['href'])
    for movie_link in list_of_movies:
        endpoint = ''.join(['/', '/'.join(movie_link.split('/')[-2:])])
        download_link = str()
        html = api.movie_details(endpoint=endpoint)
        time.sleep(random.uniform(5.0, 10.0))
        soup = bs4.BeautifulSoup(html.text, 'html.parser')
        for keyword in ['2160p.WEB Torrent', '2160p Torrent', ]:
            if not download_link:
                for link in soup('a', href=True):
                    if 'https://yts.mx/torrent/' in link['href']:
                        if keyword in link['title']:
                            download_link = link['href']
                            torrent_file=f"{download_link.split('/')[-1:][0]}.torrent"
                            os.popen(f'curl -fsSL {download_link} -o {torrent_file}')
                            time.sleep(random.uniform(5.0, 10.0))
                            print(f'curl -fsSL {download_link} -o {torrent_file}')
                            break

get_indexes()
for index in movies_indexes:
    if '?' in index:
        endpoint, page = index.split('?')
        params[page.split('=')[0]] = page.split('=')[1]
    else:
        params = dict()
    get_download_links()
