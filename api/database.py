import os
import pandas as pd
from getMovieInfoFromTMDB import getMovieData
from api import db, Movie, User

def uploadMovieData():
    """ Find and upload movie data to database"""

    df = pd.read_pickle('C:/mydev/recommender/data/movieData.pkl')
    tmdbIds = df['tmdbId'].to_list()
    with open("uploadErrors.txt", "w") as f:
        f.truncate(0)
        for mId in tmdbIds:
            try:
                data = getMovieData(mId)
                title = data['title']
                poster = f"http://image.tmdb.org/t/p/w185{data['poster_path']}"
                overview = data['overview']
                date = data['release_date']
                duration = data['runtime']
                genres = '|'.join([g['name'] for g in data['genres']])
                rating = round(data['vote_average']/2, 1)

                movie = Movie(id=mId,
                              title=title,
                              poster=poster,
                              overview=overview,
                              date=date,
                              duration=duration,
                              genres=genres,
                              rating=rating)

                db.session.add(movie)
                db.session.commit()
            except:
                f.write(f"Can't upload data for {mId}")


if __name__ == "__main__":
    db.create_all()
    # uploadMovieData()
            