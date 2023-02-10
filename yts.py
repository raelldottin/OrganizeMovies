'''YTS module for downloading movies'''
import os
import time
import random
import bs4
import api


class YTS(object):
    endpoint = "/browse-movies/0/2160p/all/8/year/0/en"
    list_of_movies = list()
    movies_indexes = [
        endpoint,
    ]
    params = dict()
    download_link = str()

    def get_indexes(self) -> None:
        yts_mx = api.NewMovieEndpoint()
        html = yts_mx.list_movies(endpoint=self.endpoint, params=dict())
        time.sleep(random.uniform(5.0, 10.0))
        soup = bs4.BeautifulSoup(html.text, "html.parser")
        for link in soup("a", href=True):
            if self.endpoint in link["href"]:
                if link["href"] not in self.movies_indexes:
                    self.movies_indexes.append(link["href"])

    def get_download_links(self) -> None:
        yts_mx = api.NewMovieEndpoint()

        print(f"{self.endpoint=}\t{self.params=}")
        if self.params:
            html = yts_mx.list_movies(endpoint=self.endpoint, params=self.params)
        else:
            html = yts_mx.list_movies(endpoint=self.endpoint, params=dict())
        time.sleep(random.uniform(5.0, 10.0))
        soup = bs4.BeautifulSoup(html.text, "html.parser")
        for link in soup("a", href=True):
            if "https://yts.mx/movies/" in link["href"]:
                if link["href"] not in self.list_of_movies:
                    self.list_of_movies.append(link["href"])
        for movie_link in self.list_of_movies:
            endpoint = "".join(["/", "/".join(movie_link.split("/")[-2:])])
            self.download_link = str()
            html = yts_mx.movie_details(endpoint=endpoint)
            time.sleep(random.uniform(5.0, 10.0))
            soup = bs4.BeautifulSoup(html.text, "html.parser")
            for keyword in [
                "2160p.WEB Torrent",
                "2160p Torrent",
            ]:
                if not self.download_link:
                    for link in soup("a", href=True):
                        if ("https://yts.mx/torrent/" in link["href"]) and (
                            keyword in link["title"]
                        ):
                            self.download_link = link["href"]
                            torrent_file = (
                                f"{self.download_link.split('/')[-1:][0]}.torrent"
                            )
                            os.popen(
                                f"curl -fsSL {self.download_link} -o {torrent_file}"
                            )
                            time.sleep(random.uniform(5.0, 10.0))
                            print(f"curl -fsSL {self.download_link} -o {torrent_file}")
                            break

    def run(self):
        self.get_indexes()
        for index in self.movies_indexes:
            if "?" in index:
                self.endpoint, page = index.split("?")
                self.params[page.split("=")[0]] = page.split("=")[1]
            else:
                self.params = dict()
            self.get_download_links()
