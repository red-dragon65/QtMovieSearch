# QtMovieSearch
This is a machine learning movie recommendation engine built with a Qt GUI.

This app uses a k-means algorithm for the year, and a jaccard algorithm for genre and title. In addition,
the app applies weights to each score of the year, genre, and title. This way, the genre is preferred over
the year and title for a more sensible recommendation set.

### How to use
- Run the python app in a command line. From there, you can select a CLI menu, or a GUI menu.
- Once the app is running, search for movies that you like and add it to your list.
- Once you movie selection is created, you can have the app generate a list of top movies that you might like.

### Notes
- Please use the CLI menu as it is more stable than the GUI menu. The GUI menu has bugs that have not been worked out.
- Try not to be picky about the minimum movie rating for recommended movies is. This is because the app has to pull
ratings data from IMDB which is not cached and is rate limited. This means a rating above a 7 - 7.5 will lead to a long
wait time as many ratings pulled will get discarded.

### Future considerations
- Adding a list for disliked movies can create a more accurate set of genre tags and years that will create a more
accurate recommendation set.
