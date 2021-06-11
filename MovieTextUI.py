'''
3580: Recommendation Engine
Author: Mujtaba Ashfaq
Date: 3/23/21

This is a content based movie search engine.
'''

# Used for movie search engine
import MovieRecommendationEngine as mre

# Allow console commands
import os



'''
Manage console main menu branching for the user
'''
def textMenu():

    # Hold user input
    user_input = ''
    formatted_user_input = 1

    # Loop through menu options
    while formatted_user_input > 0:

        print("\n\n")

        #Show menu
        print("Main menu")
        print("----------")
        print("1. Search by title")
        print("2. Search by year")
        print("3. Search by genre")
        print("---")
        print("4. Show your selected movie list")
        print("5. Show recommended movies")
        print("--")
        print("6. Recommendation Filter: Set minimum year")
        print("7. Recommendation Filter: Set minimum rating")
        print()
        print("(Enter -1 to exit)")
        print("Enter selection (1-5): ", end="")


        # Get input
        user_input = input()

        # Verify input
        try:
            formatted_user_input = int(user_input)
        except:
            print("Invalid input! Try again!")
            continue

        # Process input
        if 0 < formatted_user_input <= 3:
            searchTextUI(formatted_user_input)

        elif formatted_user_input == 4:
            print("\n\nSelected movies")
            print("----------------------")
            print("Loading movies (this may take a while due to ratings data)")
            print("Please wait for main menu...\n")
            showSelectedMovies()

        elif formatted_user_input == 5:
            print("\n\nRecommended movies")
            print("----------------------")
            print("Note:")
            print("- Title weighting is set to " + str(mre.title_weighting) + " decimal percentage")
            print("- Genre weighting is set to " + str(mre.genre_weighting) + " decimal percentage")
            print()
            print("Loading movies (this may take a while due to ratings API call)")
            print("Please wait for main menu...\n")
            displayMovies(mre.calculateRecommendations(), True)
            print("\n\n")

        elif formatted_user_input == 6:
            print("\n\nEnter min year: ", end="")
            global user_min_year
            try:
                user_min_year = int(input())
            except:
                print("Invalid input! Try again!")
                continue
            print("\n\n")

        elif formatted_user_input == 7:
            print("\n\nNote: Do not choose a rating above 7 as results may take a long time to load!")
            print("Enter min rating: ", end="")
            global user_min_rating
            try:
                user_min_rating = float(input())
            except:
                print("Invalid input! Try again!")
                continue
            print("\n\n")

        else:
            print("Input out of range!")

        if formatted_user_input == -1:
            return



'''
Menu for allowing user to search for movies using the console
'''
def searchTextUI(menu_id):

    user_input = ''

    # For searching
    while user_input != "-1":

        print("\n\n")

        # Clear console
        cls()

        # Print menu info
        print("(Enter -1 to return to main menu)")

        if menu_id == 1:
            print("Enter the movie NAME you want to search: ", end="")
        elif menu_id == 2:
            print("Enter the movie YEAR you want to search: ", end="")
        elif menu_id == 3:
            print("Enter the movie GENRES you want to search: ", end="")

        # Get user input
        user_input = input()

        # Go back to main menu
        if user_input == "-1":
            return

        # Show search results
        print("\n\nResults")
        print("------------")
        print()

        results_df = ''

        # Do the correct search
        if menu_id == 1:
            results_df = mre.searchMovieByTitle(user_input)
            printTopResults(results_df)
        elif menu_id == 2:
            results_df = mre.searchMovieByYear(user_input)
            printTopResults(results_df)
        elif menu_id == 3:
            results_df = mre.searchMovieByGenre(user_input)
            printTopResults(results_df)


        # Show menu
        print()
        print("Enter the index of the movie you want to add to your movie list")
        print("(Enter -1 to return to main menu)")
        print("(Enter out of bounds value to skip)")
        print("Your input: ", end="")

        # Get user input
        user_input = input()

        # Verify input
        try:
            user_input = int(user_input)
        except:
            print("Invalid input! Try again!")
            continue

        # Go to main menu
        if user_input == "-1":
            return

        # Save users selection
        mre.selectMovie(results_df, user_input)

        if user_input < 1 or user_input > mre.number_of_results:
            print("Out of bounds index! Selection not saved :(")
        else:
            print("Selection saved!")

        print("\nEnter 1 to search again")
        print("Enter -1 to return to main menu")
        print("Your input: ", end="")

        # Get user input
        user_input = input()



'''
Allows clearing the console (doesn't work in pycharm!)
'''
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



'''
Display the users selected movies in a clean way
'''
def showSelectedMovies():


    displayMovies(getSelectedMovies(), False)


def getSelectedMovies():

    # Retrieve movies
    user_movies_df = mre.df.loc[(mre.df['movieId'].isin(mre.user_selection))]

    return user_movies_df


'''
Display the movie search results in a clean way
'''
def printTopResults(results_df):

    # Pull out the movie ids
    movie_ids = results_df['movieId'].to_list()

    row_num = 0

    # Get movies from original dataframe
    for i in movie_ids:

        # Get row
        movie_item = mre.og_df.loc[(mre.df['movieId'] == i)]

        year = movie_item['year'].to_list()[0]

        # Format for displaying

        print()

        print("Index: ", end="")
        print(1 + row_num)

        print(movie_item['title'].to_list()[0])

        print("    - Year: ", end="")
        print(year)

        print("    - Genres: ", end="")
        genres = movie_item['genre_array'].to_list()[0]
        for i in range(len(genres)):
            print(genres[i], end="")
            if i != len(genres) - 1:
                print(", ", end="")
        print()

        # Count number of results
        row_num += 1

        # End method if number of results has been reached
        if row_num == mre.number_of_results:
            return

    print()



'''
Display the recommended movies in a clean way
'''
def displayMovies(recommend_df, limit_rows):

    # Pull out the movie ids
    movie_ids = recommend_df['movieId'].to_list()

    row_num = 0

    # Get movies from original dataframe
    for i in movie_ids:

        # Get row
        movie_item = mre.og_df.loc[(mre.df['movieId'] == i)]

        # Get more movie data from imdb
        movie = mre.ia.get_movie(movie_item['imdbId'].to_list()[0])
        rating = movie.get('rating')
        year = movie_item['year'].to_list()[0]

        # Apply user restrictions
        if rating < mre.user_min_rating:
            continue

        if int(year) < mre.user_min_year:
            continue


        # Format for displaying
        print(movie_item['title'].to_list()[0])

        print("    - Rating: ", end="")
        print(rating)

        print("    - Year: ", end="")
        print(year)

        print("    - Genres: ", end="")
        genres = movie_item['genre_array'].to_list()[0]
        for i in range(len(genres)):
            print(genres[i], end="")
            if i != len(genres) - 1:
                print(", ", end="")
        print()

        print("    - Plot: ", end="")

        # Get the first plot and remove the author signature
        print(movie.get('plot')[0].split(':')[0])

        print()

        # Count number of results
        if limit_rows:
            row_num += 1

        # End method if number of results has been reached
        if row_num == mre.number_of_results:
            return



# Actually run menu
#textMenu()