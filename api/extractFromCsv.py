import json
import numpy as np
import pandas as pd
from getMovieInfoFromTMDB import getMovieData

def getGeneralList(count=100):
    """
    Get general list of top movies
    
    Params: count - number of movies to fetch

    Returns: list of movie with data
    """

    df = pd.read_pickle('C:/mydev/recommender/data/movieData.pkl')
    topMovies = df.nlargest(count, 'popularity')
    tmdbIds = topMovies['tmdbId'].to_list()
    movieData = [getMovieData(i) for i in tmdbIds]

    # return json.dumps({"movies": movieData})
    return {"movies": movieData}



def getSelections(count=100, genres=[], strictGenres=False, earliest=0, latest=10000):
    """Get selections from df
    
    Params: count - number of movies to retrieve
            genres - list of genres preferred
            strictGenres - bool to limit choosing movies without the desired genre
            earliest - earliest year of movie release
            latest - latest year of movie release 

    Returns: list of movie ids
    """

    raise NotImplementedError
    # df = pd.read_pickle('C:/mydev/recommender/data/movieData.pkl')

    # # Remove movies outside of the date range
    # df = df[df['year'].map(lambda x: (earliest <= x) and (x <= latest))]


def countGenreOverlaps(df_row, genres):
    raise NotImplementedError
    # movie_genres = 


def getGenres(df_row):
    """Get all genres from a row in the dataframe
    
    Params: df_row: the dataframe to extract from

    Returns: list of genres found
    """
    genresStr = df_row['genres']

    # Handle case where no genres listed
    if genresStr.strip() == "(no genres listed)":
        return []


    genresLst = [g.strip() for g in genresStr.split('|')]
    return genresLst


def calculatePopularity(df_row):
    mean = df_row['average rating']
    count = df_row['rating count']
    totalPopularity = mean * count
    return totalPopularity


def getMovieYearFromTitle(title):
    try:
        year = int(title.strip()[-5:-1])
    except:
        year = 0
    
    return year


def toInt(num):
    if type(num) is np.float64:
        return int(num)
    
    return num


def moviesWithInfo():
    """
    Get movies and related information from processing .csv files

    Saves the resulting dataframe to pickle for quick accsess

    Params: No Params

    Returns: 
    """

    # Get movies, ratings and links from .csv file
    movies = pd.read_csv('C:/mydev/recommender/data/movies.csv')
    ratings = pd.read_csv('C:/mydev/recommender/data/ratings.csv')
    links = pd.read_csv('C:/mydev/recommender/data/links.csv')

    # Format the IDs in links
    links = links.fillna(0.0)
    links.astype(np.int64)
    links = links.apply(np.vectorize(toInt))

    # Remove unused information
    del ratings["timestamp"]
    del ratings["userId"]

    # Merge the two dataframes and calculate additional information for the movies
    merged = pd.merge(movies, ratings)
    grouped = merged.groupby(['movieId', 'title', 'genres'], as_index=False)
    df = grouped.first()
    del df['rating']
    df['rating count'] = grouped.count()['rating']
    df['average rating'] = grouped.mean()['rating']
    df['year'] = [getMovieYearFromTitle(x) for x in df['title']]
    df['popularity'] = df.apply(calculatePopularity, axis=1)

    # Add TMDB and IMDB id
    df = pd.merge(df, links, on='movieId')
    df.to_pickle('C:/mydev/recommender/data/movieData.pkl')



if __name__ == "__main__":
    print(getGeneralList())
