import csv
import json
import pandas as pd
import requests

# TMDB Credentials
API_key = '8c2362eacfae33b9a7e317356c237a90'
    


def getMovieData(Movie_ID):
    query = f'https://api.themoviedb.org/3/movie/{Movie_ID}?api_key={API_key}&language=en-US'
    response =  requests.get(query)
    if response.status_code==200: 
        data = response.json()
        return data
    else:
        return ("error")

def save_movie_data(csv_path):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        with open("failed.txt", "a") as log_file:
            log_file.truncate(0)
            for row in csv_reader:
                movie_id = row[0]
                tmdb_id = row[-1]
                data = getMovieData(tmdb_id)
                json.dump(data, f"C:/mydev/recommender/movieInfo/{tmdb_id}_info.json")

def download_poster(Movie_ID):
    data = getMovieData(Movie_ID)
    if data == "error":
        return f"ERROR: Movie ID not found: {Movie_ID}"
    else:
        try:
            poster_path_rel = data["poster_path"]
            poster_path_full = f"https://image.tmdb.org/t/p/original/{poster_path_rel}"
            response = requests.get(poster_path_full)
            with open(f"C://mydev//recommender//posters{Movie_ID}.jpg", "wb") as f:
                f.write(response.content)
                f.close()
            return f"DONE: Poster found for {Movie_ID}"
        except Exception as e:
            return f"ERROR: Can't fetch poster for {Movie_ID}, exception: {e}"


def download_posters_from_csv(csv_path):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        with open("download_log.txt", "a") as log_file:
            log_file.truncate(0)
            for row in csv_reader:
                tmdb_id = row[-1]
                log_file.write(download_poster(tmdb_id))




if __name__ == "__main__":
    # print(get_data(862))
    # download_posters_from_csv('data/links.csv')
    print(getMovieData(862))
