'''
3580: Recommendation Engine
Author: Mujtaba Ashfaq
Date: 3/23/21

This is a content based movie search engine.
'''

# Library for processing data frames
import pandas as pd

# IMDB API library
from imdb import IMDb

# Random number generator
from random import randint

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans






# Initialize imdb object
ia = IMDb()

# Read in the csv file
og_df = pd.read_csv('movies.csv')

# Make data readable during testing
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#print(og_df)




'''
Pre process data
'''
# Extract year and title into separate columns
og_df['year'] = og_df['title'].str.extract(r'([0-9]{4})')
og_df['title'] = og_df['title'].replace(r'(\s\([0-9]{4}\))', '', regex=True)

# Extract genre as an array
og_df['genre_array'] = og_df['genres'].str.split('|')

# Remove rows with missing data
og_df.dropna(inplace=True)

# Hold additional data separate from original dataframe
df = og_df.copy()

# Extract title as an array
df['title_array'] = df['title'].str.split(' ')

# Lower case genres and title
df['title'] = df['title'].str.lower()
df['genres'] = df['genres'].str.lower()


#print(df)


# Number of results to return
number_of_results = 10

# Movie ids selected by user
user_selection = []

# Recommendation filter
user_min_rating = float(0.0)
user_min_year = 0

# Feature weighting importance
genre_weighting = 0.80
title_weighting = 0.20






'''
Return a list of ten random movies
'''
def randomMovies():

    # Hold random indices
    indices = []

    # Generate 10 random indices
    for i in range(number_of_results):
        indices.append(randint(0, len(df)))

    # Hold ten movies
    random_movies = []

    # Retrieve movie from list using indices
    for i in range(number_of_results):
        random_movies.append(df.iloc[indices[i]])

    # Return list of movies
    return random_movies




'''
Allow user search
- Based on year
- Based on movie title
- Based on genre

Do straight string matching at minimum
'''
def searchMovieByTitle(title):

    movies_df = df[df['title'].str.contains(title)]
    return movies_df


def searchMovieByYear(year):

    movies_df = df[df['year'].str.contains(year, na=False)]
    return movies_df


def searchMovieByGenre(genre):

    movies_df = df[df['genres'].str.contains(genre, na=False)]
    return movies_df




'''
# Return only the top results from the df
def getTopResults(movieList):

    top_results_df = movieList[:number_of_results]

    return top_results_df
'''





'''
Allow user to select movies
(via recommended or search)
- Track all the selected movies
- Show the user what they have selected
'''
def selectMovie(movie_list, index):

    # Offset index to account for array starting at 0
    index -= 1

    # Access the movie id column
    column = 0

    # Verify index is not bullshit
    if 0 <= index < len(movie_list):

        # Add movie selection
        user_selection.append(movie_list.iloc[index, column])






'''
Calculate recommendations based on:
- Year
- Title
- Genre

Use k nearest neighbor at minimum
'''
def calculateRecommendations():

    # Calculate cluster labels for year
    kmeans()

    # Hold the final weighted df
    weighted_df = df.copy()



    # Get the users_movies
    user_movies = df.loc[(df['movieId'].isin(user_selection))]

    # Users movie year cluster
    user_cluster = user_movies['cluster'].to_list()

    # Only get movies in the same cluster as the users movies
    weighted_df = weighted_df.loc[(weighted_df['cluster'].isin(user_cluster))]



    # Drop movies the user has already seen
    weighted_df = weighted_df.loc[(weighted_df['movieId'].isin(user_selection)==False)]


    # Calculate weighting for genre using jaccard
    weighted_df = jaccard_df_genre_calc(weighted_df)

    # Calculate weighting for title
    weighted_df = jaccard_df_title_calc(weighted_df)

    # Calculate final weighting
    weighted_df['final_weighting'] = ((weighted_df['genre_weights'] * genre_weighting) + (weighted_df['title_weights'] * title_weighting)) / 2

    # Sort movie by final weight
    weighted_df = weighted_df.sort_values(by='final_weighting', ascending=False)



    # Return top ten movies
    return weighted_df




'''
Calculate k means for years
'''
def kmeans():

    # Add dummy to df
    dummy_df = df.copy()

    # Convert categorical data to numerical data
    #genre_dummy = pd.get_dummies(df['genres_array'])

    # Drop all data but year data
    del dummy_df['movieId']
    del dummy_df['title']
    del dummy_df['genres']
    del dummy_df['imdbId']
    del dummy_df['genre_array']
    del dummy_df['title_array']

    # Reset index so it actually works with sklearn
    dummy_df.reset_index()


    # Setup k means with 10 clusters
    kmeans = KMeans(n_clusters=10, random_state=0)

    # Fit kmeans
    kmeans.fit(dummy_df)

    # Get clusters
    clusters = kmeans.predict(dummy_df)

    # Label movies with respective cluster
    df['cluster'] = clusters



'''
Weighted jaccard for genre
'''
def jaccard_df_genre_calc(weighted_df):

    # Hold all genres based on user selection
    user_genres = []

    print(df)
    # Get only user movies from df
    user_movies_df = df.loc[(df['movieId'].isin(user_selection))]

    # Get the genres for the users movies
    user_genres = user_movies_df['genre_array'].to_list()

    # Calculate movie weights
    weighted_df['genre_weights'] = df['genre_array'].apply(lambda x: weighted_jaccard_similarity(user_genres, x))

    # Return the df with the added weights
    return weighted_df



'''
weighted jaccard for title
'''
def jaccard_df_title_calc(weighted_df):

    # Hold all movie titles based on user selection
    user_movie_titles = []

    # Get only user movies from df
    user_movies_df = df.loc[(df['movieId'].isin(user_selection))]

    # Get the titles for the users movies
    user_movie_titles = user_movies_df['title_array'].to_list()

    # Calculate movie weights
    weighted_df['title_weights'] = df['title_array'].apply(lambda x: weighted_jaccard_similarity(user_movie_titles, x))

    # Return the df with the added weights
    return weighted_df



'''
Weighted jaccard algorithm definition
'''
def weighted_jaccard_similarity(a, b):

    # in this case, 'a' is all the selections that the user has made so far
    # build the weighted dictionary:
    c = {'total': 0}
    for el in a:
        for genre in el:
            if genre in c: c[genre] += 1
            else: c[genre] = 1
            c['total'] += 1

    numerator = 0
    denomenator = c['total']
    for genre in b:
        if genre in c:
            numerator += c[genre]

    return numerator / denomenator



