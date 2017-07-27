# Movie Recommender System
This project is a mini movie recommender system which recommends movies based on user ratings.


## Dataset
Dataset used is MovieLens 100K Dataset. This data set consists of: 100,000 ratings (1-5) from 943 users on 1682 movies. Each user has rated at least 20 movies.


## Model
The whole model used correlation matrix to find the relation between various movies and then uses k-Nearest Neighbour to find the similar movies.


## Result Screenshot
![movie1](https://user-images.githubusercontent.com/25280843/28689208-7562c074-7332-11e7-89b4-a85979e7ca00.png)

Correlation of movies with 'Star Wars'

![movie2](https://user-images.githubusercontent.com/25280843/28689257-ab7853ea-7332-11e7-87d4-7ed41e4143fc.png)

Movies similar with Star Wars

![rate](https://user-images.githubusercontent.com/25280843/28689448-4914b850-7333-11e7-9803-47ec2d5b0a0e.png)

Recommended movies


### File Description
movie.py - This output similar movies w.r.t. a given movie.
rating.py - This output the recommended movies.
