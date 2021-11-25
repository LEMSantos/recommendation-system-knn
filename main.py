import pandas as pd
from scipy.sparse import csr_matrix
from fuzzywuzzy import process, fuzz
from sklearn.neighbors import NearestNeighbors


def recommender(movie_name, data, k):
    idx = process.extractOne(
        movie_name,
        movies['title'],
        scorer=fuzz.partial_token_set_ratio,
    )[2]

    print('Movie Selected:', movies['title'][idx], '- Index:', idx)
    print('Searching recommendation...\n')

    _, indices = model.kneighbors(data.iloc[[idx]], n_neighbors=k)

    for i in indices[0]:
        if i != idx:
            print(movies['title'][i])


movies = pd.read_csv('data/prepared_data.csv')

training_data = movies.drop(['movieId', 'title', 'users_count'], axis=1)

model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20)
model.fit(training_data)


if __name__ == '__main__':
    movie = input('Enter the movie to get recommendations: ')
    print('\n')

    recommender(movie, training_data, 10)
