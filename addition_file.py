import csv
import requests
import datetime
import pytz


class Addition:
    def __init__(self, title=None):
        self.title = title

    def movie_id_search(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"title": self.title}

        headers = {
            "Type": "get-movies-by-title",
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['movie_results'][0]['imdb_id']

    def movie_year(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"title": self.title}

        headers = {
            "Type": "get-movies-by-title",
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['movie_results'][0]['year']

    def popularity(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"movieid": new_obj.movie_id_search()}

        headers = {
            "Type": "get-movie-details",
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['popularity']

    def description(self):
        url = f"https://imdb207.p.rapidapi.com/storyline/{new_obj.movie_id_search()}"

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "imdb207.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        return response.json()['result']['storyline'][0]

    def content_rating(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"movieid": new_obj.movie_id_search()}

        headers = {
            "Type": "get-movie-details",
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['rated']

    def movie_length(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"movieid": new_obj.movie_id_search()}

        headers = {
            "Type": "get-movie-details",
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['runtime']

    def rating(self):
        url = "https://mdblist.p.rapidapi.com/"

        querystring = {"i": new_obj.movie_id_search()}

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "mdblist.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['ratings'][0]['value']

    def created(self):
        date = datetime.datetime.now()
        tz = pytz.timezone('Europe/Kiev')
        new_date = tz.localize(date)

        return new_date.isoformat()

    def trailer(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"movieid": new_obj.movie_id_search()}

        headers = {
            "Type": "get-movie-details",
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return 'https://www.youtube.com/watch?v=' + response.json()['youtube_trailer_key']

    def image_url(self):
        url = f"https://imdb207.p.rapidapi.com/id/{new_obj.movie_id_search()}"

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "imdb207.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        return response.json()['result']['poster'][:-15] + 'UX182_CR0,0,182,268_AL_.jpg'

    def release_date(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"movieid": new_obj.movie_id_search()}

        headers = {
            "Type": "get-movie-details",
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['release_date']

    def plot_summary(self):
        url = "https://imdb146.p.rapidapi.com/v1/title/"

        querystring = {"id": new_obj.movie_id_search()}

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "imdb146.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['plot']['plotText']['plainText']

    def image_banner(self):
        url = f"https://imdb207.p.rapidapi.com/id/{new_obj.movie_id_search()}"

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "imdb207.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        return response.json()['result']['poster']

    def title_type(self):
        url = "https://imdb146.p.rapidapi.com/v1/title/"

        querystring = {"id": new_obj.movie_id_search()}

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "imdb146.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()['titleType']['id']

    def more_like_this(self):
        url = "https://imdb-com.p.rapidapi.com/title/details"

        querystring = {"tconst": new_obj.movie_id_search()}

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "imdb-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        more_like_list = []
        for i in response.json()['data']['mainColumnData']['moreLikeThisTitles']['edges']:
            more_like_list.append(i['node']['originalTitleText']['text'])
        return more_like_list

    def genres(self):
        url = "https://imdb146.p.rapidapi.com/v1/title/"

        querystring = {"id": new_obj.movie_id_search()}

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "imdb146.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        genres_list = []
        for i in response.json()['titleGenres']['genres']:
            genres_list.append(i['genre']['text'])
        genre_dict = dict.fromkeys(genres_list, 'genre')
        res_list = [{val: key} for key, val in genre_dict.items()]
        return res_list

    def movie_keywords(self):
        url = "https://mdblist.p.rapidapi.com/"

        querystring = {"i": new_obj.movie_id_search()}

        headers = {
            "X-RapidAPI-Key": "4f6ac20324msh40d2c8d0f01119dp1600a3jsn409f6c7d7ca4",
            "X-RapidAPI-Host": "mdblist.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        keyw_list = []
        for i in response.json()['keywords']:
            keyw_list.append(i['name'])
        keyw_dict = dict.fromkeys(keyw_list, 'keyword')
        res_keyw_list = [{val: key} for key, val in keyw_dict.items()]
        return res_keyw_list

    def extend_csv_file(self):
        file_name = "films.csv"
        with open(file_name, "a", newline="") as file:
            data_list = [new_obj.movie_id_search(), self.title, new_obj.movie_year(), new_obj.popularity(),
                         new_obj.description(), new_obj.content_rating(), new_obj.movie_length(), new_obj.rating(),
                         new_obj.created(), new_obj.trailer(), new_obj.image_url(), new_obj.release_date(),
                         new_obj.plot_summary(), new_obj.image_banner(), new_obj.title_type(), new_obj.more_like_this(),
                         new_obj.genres(), new_obj.movie_keywords()]
            writer = csv.writer(file)
            writer.writerow(data_list)


new_obj = Addition('Class of 1999')
