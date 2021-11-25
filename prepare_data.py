import pandas as pd


movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv', usecols=['movieId', 'userId', 'rating'])

movies_dummies = movies['genres'].str.get_dummies(sep='|')
movies = movies.join(movies_dummies)

ratings_mean = ratings.groupby('movieId').agg({
    'userId': 'sum',
    'rating': 'mean',
})

ratings_mean['ratings_normalized'] = (
    (ratings_mean['rating'] - ratings_mean['rating'].min()) / (
        ratings_mean['rating'].max() - ratings_mean['rating'].min()
    )
)

ratings_mean['users_count'] = ratings_mean['userId']

del ratings_mean['userId']
del ratings_mean['rating']
del movies['genres']

prepared_data = movies.join(ratings_mean)
prepared_data = prepared_data.fillna(0)

prepared_data.to_csv('data/prepared_data.csv', index=False)
