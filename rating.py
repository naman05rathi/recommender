import pandas as pd
import numpy as np
from scipy import spatial
import operator

rating_column = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/home/naman/Downloads/ml-100k/u.data', sep='\t', names=rating_column, usecols=range(3))
properties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genre_dist = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularity_dist = abs(popularityA - popularityB)
    return genre_dist + popularity_dist

def getNeighbors(movieID, K):
    distances = []
    for movie in dictionary:
        if (movie != movieID):
            dist = ComputeDistance(dictionary[movieID], dictionary[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

movie_rate = pd.DataFrame(properties['rating']['size'])
movie_rate_normal = movie_rate.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

dictionary = {}
with open(r'/home/naman/Downloads/ml-100k/u.item') as f:
    temp = ''
    for line in f:
        field = line.rstrip('\n').split('|')
        movieID = int(field[0])
        name = field[1]
        genres = field[5:25]
        genres = map(int, genres)
        dictionary[movieID] = (name, genres, movie_rate_normal.loc[movieID].get('size'), properties.loc[movieID].rating.get('mean'))

print ComputeDistance(dictionary[1], dictionary[2])

K = 10
rate_average = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    rate_average += dictionary[neighbor][3]
    print dictionary[neighbor][0] + " " + str(dictionary[neighbor][3])
    
rate_average /= float(K)

print rate_average