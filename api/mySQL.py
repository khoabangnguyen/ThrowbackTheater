# import mysql.connector
# from datetime import datetime
# import json
# import pandas as pd
# import os
# from sqlalchemy import create_engine, insert, MetaData, Table, Column, String, Date, Integer, Float
# from sqlalchemy.orm import sessionmaker
# from getMovieInfoFromTMDB import getMovieData

# class mySQLEditor():
#     def __init__(self, host="localhost", user="root", password="root", database="recommender"):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.connection = self.connectToDB()

#     def connectToDB(self):
#         mydb = mysql.connector.connect(
#                                         host=self.host,
#                                         user=self.user,
#                                         password=self.password,
#                                         database=self.database
#                                     )
#         return mydb

#     def createDB(self, dbname):
#         cursor = self.connection.cursor()
#         try: 
#             cursor.execute(f"CREATE DATABASE {dbname}")
#         except Exception as e: 
#             print(f"Can't create database {dbname} \n Exception: {e}")

#     def uploadStarterData(self, dir="C:/mydev/recommender/data"):
#         engine = create_engine('mysql://root:@localhost/test?charset=utf8')
#         for filename in os.listdir(dir):
#             if filename.endswith(".csv"):
#                 tableName = filename[:-4]
#                 filePath = os.path.join(dir, filename)
#                 dfs = pd.read_csv(filePath, chunksize=50000, index_col=False, delimiter = ',', encoding='utf-8')
#                 res_dfs = []
#                 for chunk in dfs:
#                     res_dfs.append(chunk)

#                 data = pd.concat(res_dfs)
#                 data.to_sql(tableName, con=engine,index=False,if_exists='replace', method='multi')
#             else:
#                 continue
    

#     def checkTableExists(self, tableName):
#         cursor = self.connection.cursor()
#         cursor.execute("""
#             SELECT COUNT(*)
#             FROM information_schema.tables
#             WHERE table_name = '{0}'
#             """.format(tableName.replace('\'', '\'\'')))
#         if cursor.fetchone()[0] == 1:
#             return True

#         return False


#     def uploadMovieData(self, tableName='movies'):
#         """ Find and upload movie data to database"""

#         engine = create_engine('mysql://root:root@localhost/recommender?charset=utf8')
#         Session = sessionmaker(bind=engine)
#         session = Session()

#         # Create table if doesn't exist:
#         if not self.checkTableExists(tableName):
#             meta = MetaData()
#             movies = Table(
#                 tableName,
#                 meta,
#                 Column('id', Integer, primary_key = True), 
#                 Column('title', String(255)),
#                 Column('poster', String(255)),
#                 Column('overview', String(255)),
#                 Column('date', Date),
#                 Column('duration', Integer),
#                 Column('genres', String(255)),
#                 Column('rating', Float(precision=1))
#             )
#             meta.create_all(engine)


#         df = pd.read_pickle('C:/mydev/recommender/data/movieData.pkl')
#         tmdbIds = df['tmdbId'].to_list()
#         for mId in tmdbIds:
#             try:
#                 data = getMovieData(mId)
#                 title = data['title']
#                 poster = f"http://image.tmdb.org/t/p/w185{data['poster_path']}"
#                 overview = data['overview']
#                 date = data['release_date']
#                 duration = data['runtime']
#                 genres = ''.join([g['name'] for g in data['genres']])
#                 rating = round(data['vote_average']/2, 1)
#                 users.insert().values(

#                 )

#             except:
#                 json.dumps('test.json')


# if __name__=="__main__":
#     editor = mySQLEditor()
#     # editor.uploadMovieData()
#     # print(editor.checkTableExists('movies'))
#     # editor.uploadMovieData()
#     db.create_all()

