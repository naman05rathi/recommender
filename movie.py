import pandas as pd
import numpy as np

rating_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/home/naman/Downloads/ml-100k/u.data', sep='\t', names=rating_columns, usecols=range(3))
movie_columns = ['movie_id', 'title']
movies = pd.read_csv('/home/naman/Downloads/ml-100k/u.item', sep='|', names=movie_columns, usecols=range(2))

ratings = pd.merge(movies, ratings)
rate_movie = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

star_wars = rate_movie['Star Wars (1977)']
similar = rate_movie.corrwith(star_wars)
similar = similar.dropna()
df = pd.DataFrame(similar)
#print similar.sort_values(ascending=False)

stats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
popular = stats['rating']['size'] >= 100
#print stats[popular].sort_values([('rating', 'mean')], ascending=False)[:15]

df1 = stats[popular].join(pd.DataFrame(similar, columns=['similarity']))
print df1.sort_values(['similarity'], ascending=False)[:15]
print ("")
print ("")
print ("")

user = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
correlation_matrix = user.corr()
correlation_matrix = user.corr(method='pearson', min_periods=100)
rate = user.loc[0].dropna()

similar_candidate = pd.Series()
for i in range(0, len(rate.index)):
	print rate.index[i]
	simi = correlation_matrix[rate.index[i]].dropna()
	simi = simi.map(lambda x: x * rate[i])
	similar_candidate = similar_candidate.append(simi)
    
similar_candidate.sort_values(inplace = True, ascending = False)
similar_candidate = similar_candidate.groupby(similar_candidate.index).sum()
similar_candidate.sort_values(inplace = True, ascending = False)

filter_movie = similar_candidate.drop(rate.index)
print filter_movie.head(10)