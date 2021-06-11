'''
3580: Recommendation Engine
Author: Mujtaba Ashfaq
Date: 3/23/21

This is a content based movie search engine.
'''

# Use this for qt applications
from PyQt5 import QtCore, QtGui, QtWidgets

# Use this to access the movie recommendation engine
from PyQt5.QtGui import QImage, QPixmap

# Used for movie search engine
import MovieRecommendationEngine as mre

# Used to retrieve image data
import requests

# Use this to get the movies poster
import movieposters as mp

result_df = ''




class Ui_Dialog(object):



    """
    Button handlers
    """
    def genreSearch(self):

        # Get the users search term
        keyword = self.textboxSearch.text().lower()

        # Update the title
        self.label_6.setText("Search Results: Genre - " + keyword)

        # Get the df for the search term
        global result_df
        result_df = mre.searchMovieByGenre(keyword)

        # Pass the df to update the result list
        self.showResults(result_df)

    def yearSearch(self):

        # Get the users search term
        keyword = self.textboxSearch.text()

        # Update the title
        self.label_6.setText("Search Results: Year - " + keyword)

        # Get the df for the search term
        global result_df
        result_df = mre.searchMovieByYear(keyword)

        # Pass the df to update the result list
        self.showResults(result_df)

    def titleSearch(self):

        # Get the users search term
        keyword = self.textboxSearch.text().lower()

        # Update the title
        self.label_6.setText("Search Results: Title - " + keyword)

        # Get the df for the search term
        global result_df
        result_df = mre.searchMovieByTitle(keyword)

        # Pass the df to update the result list
        self.showResults(result_df)



    def getSelection(self):

        global result_df

        result_df = mre.getSelectedMovies()
        self.showResults(result_df)


    def calculateRecommendation(self):

        recc_df = mre.calculateRecommendations()
        self.showRecc(recc_df)



    def resetFilter(self):

        # Reset filter to default values
        self.textboxMinYear.setText("0")
        self.textboxMinRating.setText("0")

        mre.user_min_year = 0
        mre.user_min_rating = 0.0

    def applyFilter(self):

        try:
            # Update the filter values
            mre.user_min_year = int(self.textboxMinYear.text())
            mre.user_min_rating = float(self.textboxMinRating.text())

        except:
            self.textboxMinYear.setText("Invalid input!")
            self.textboxMinRating.setText("Invalid input!")
            mre.user_min_year = 0
            mre.user_min_rating = 0







    def addSelection1(self):
        mre.selectMovie(result_df, 1)
    def addSelection2(self):
        mre.selectMovie(result_df, 2)
    def addSelection3(self):
        mre.selectMovie(result_df, 3)
    def addSelection4(self):
        mre.selectMovie(result_df, 4)
    def addSelection5(self):
        mre.selectMovie(result_df, 5)
    def addSelection6(self):
        mre.selectMovie(result_df, 6)
    def addSelection7(self):
        mre.selectMovie(result_df, 7)
    def addSelection8(self):
        mre.selectMovie(result_df, 8)
    def addSelection9(self):
        mre.selectMovie(result_df, 9)
    def addSelection10(self):
        mre.selectMovie(result_df, 10)

    """
    Update UI
    """
    def showResults(self, df):

        # Clear the results UI
        self.resetResultsUI()

        # Pull out the movie ids
        movie_ids = df['movieId'].to_list()

        row_num = 0

        # Get movies from original dataframe
        for i in movie_ids:

            # Get row
            movie_item = mre.og_df.loc[(mre.df['movieId'] == i)]

            # Format for displaying
            self.updateResultsList(movie_item, row_num)

            # Count number of results
            row_num += 1

            # End method if number of results has been reached
            if row_num == mre.number_of_results:
                return



    def updateResultsList(self, movie_item, row_num):
        _translate = QtCore.QCoreApplication.translate

        # Get movie info
        title = "Title: " + movie_item['title'].to_list()[0]
        year = "Year: " + movie_item['year'].to_list()[0]

        genres_list = movie_item['genre_array'].to_list()[0]
        genre_string = ""

        for i in range(len(genres_list)):

            genre_string += genres_list[i]

            if i != len(genres_list) - 1:
                genre_string += ", "

        # Update results UI
        if row_num == 0:
            self.lbl_Result_Movie_1.setText(_translate("Dialog", title))
            self.lbl_Results_Year_1.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_1.setText(_translate("Dialog", genre_string))
        elif row_num == 1:
            self.lbl_Result_Movie_2.setText(_translate("Dialog", title))
            self.lbl_Results_Year_2.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_2.setText(_translate("Dialog", genre_string))
        elif row_num == 2:
            self.lbl_Result_Movie_3.setText(_translate("Dialog", title))
            self.lbl_Results_Year_3.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_3.setText(_translate("Dialog", genre_string))
        elif row_num == 3:
            self.lbl_Result_Movie_4.setText(_translate("Dialog", title))
            self.lbl_Results_Year_4.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_4.setText(_translate("Dialog", genre_string))
        elif row_num == 4:
            self.lbl_Result_Movie_5.setText(_translate("Dialog", title))
            self.lbl_Results_Year_5.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_5.setText(_translate("Dialog", genre_string))
        elif row_num == 5:
            self.lbl_Result_Movie_6.setText(_translate("Dialog", title))
            self.lbl_Results_Year_6.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_6.setText(_translate("Dialog", genre_string))
        elif row_num == 6:
            self.lbl_Result_Movie_7.setText(_translate("Dialog", title))
            self.lbl_Results_Year_7.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_7.setText(_translate("Dialog", genre_string))
        elif row_num == 7:
            self.lbl_Result_Movie_8.setText(_translate("Dialog", title))
            self.lbl_Results_Year_8.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_8.setText(_translate("Dialog", genre_string))
        elif row_num == 8:
            self.lbl_Result_Movie_9.setText(_translate("Dialog", title))
            self.lbl_Results_Year_9.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_9.setText(_translate("Dialog", genre_string))
        elif row_num == 9:
            self.lbl_Result_Movie_10.setText(_translate("Dialog", title))
            self.lbl_Results_Year_10.setText(_translate("Dialog", year))
            self.lbl_Results_Genres_10.setText(_translate("Dialog", genre_string))




    def resetResultsUI(self):

        _translate = QtCore.QCoreApplication.translate
        title = "N/A"
        year = "N/A"
        genre_string = "N/A"

        self.lbl_Result_Movie_1.setText(_translate("Dialog", title))
        self.lbl_Results_Year_1.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_1.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_2.setText(_translate("Dialog", title))
        self.lbl_Results_Year_2.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_2.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_3.setText(_translate("Dialog", title))
        self.lbl_Results_Year_3.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_3.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_4.setText(_translate("Dialog", title))
        self.lbl_Results_Year_4.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_4.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_5.setText(_translate("Dialog", title))
        self.lbl_Results_Year_5.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_5.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_6.setText(_translate("Dialog", title))
        self.lbl_Results_Year_6.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_6.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_7.setText(_translate("Dialog", title))
        self.lbl_Results_Year_7.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_7.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_8.setText(_translate("Dialog", title))
        self.lbl_Results_Year_8.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_8.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_9.setText(_translate("Dialog", title))
        self.lbl_Results_Year_9.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_9.setText(_translate("Dialog", genre_string))

        self.lbl_Result_Movie_10.setText(_translate("Dialog", title))
        self.lbl_Results_Year_10.setText(_translate("Dialog", year))
        self.lbl_Results_Genres_10.setText(_translate("Dialog", genre_string))





    def showRecc(self, df):

        # Pull out the movie ids
        movie_ids = df['movieId'].to_list()

        row_num = 0

        # Get movies from original dataframe
        for i in movie_ids:

            # Get row
            movie_item = mre.og_df.loc[(mre.df['movieId'] == i)]

            # Get more movie data from imdb
            movie = mre.ia.get_movie(movie_item['imdbId'].to_list()[0])
            rating = movie.get('rating')
            year = movie_item['year'].to_list()[0]
            plot = movie.get('plot')[0].split(':')[0]

            # Apply user restrictions
            if rating < mre.user_min_rating:
                continue

            if int(year) < mre.user_min_year:
                continue

            # Format for displaying
            self.updateReccList(movie_item, row_num, year, str(rating), plot)

            # Count number of results
            row_num += 1

            # End method if number of results has been reached
            if row_num == mre.number_of_results:
                return



    def updateReccList(self, movie_item, row_num, year, rating, plot):
        _translate = QtCore.QCoreApplication.translate

        # Get movie info
        title = "Title: " + movie_item['title'].to_list()[0]

        # Get genre data
        genres_list = movie_item['genre_array'].to_list()[0]
        genre_string = ""

        for i in range(len(genres_list)):

            genre_string += genres_list[i]

            if i != len(genres_list) - 1:
                genre_string += ", "

        # Get poster for movie if possible
        try:
            url = mp.get_poster(title=title)

            image = QImage()
            image.loadFromData(requests.get(url).content)
        except:
            image = ''


        # Update results UI
        if row_num == 0:
            self.lbl_Recc_Movie_1.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_1.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_1.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_1.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_1.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_1.setPixmap(QPixmap(image))
        elif row_num == 1:
            self.lbl_Recc_Movie_2.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_2.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_2.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_2.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_2.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_2.setPixmap(QPixmap(image))
        elif row_num == 2:
            self.lbl_Recc_Movie_3.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_3.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_3.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_3.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_3.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_3.setPixmap(QPixmap(image))
        elif row_num == 3:
            self.lbl_Recc_Movie_4.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_4.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_4.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_4.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_4.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_4.setPixmap(QPixmap(image))
        elif row_num == 4:
            self.lbl_Recc_Movie_5.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_5.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_5.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_5.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_5.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_5.setPixmap(QPixmap(image))
        elif row_num == 5:
            self.lbl_Recc_Movie_6.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_6.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_6.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_6.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_6.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_6.setPixmap(QPixmap(image))
        elif row_num == 6:
            self.lbl_Recc_Movie_7.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_7.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_7.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_7.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_7.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_7.setPixmap(QPixmap(image))
        elif row_num == 7:
            self.lbl_Recc_Movie_8.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_8.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_8.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_8.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_8.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_8.setPixmap(QPixmap(image))
        elif row_num == 8:
            self.lbl_Recc_Movie_9.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_9.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_9.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_9.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_9.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_9.setPixmap(QPixmap(image))
        elif row_num == 9:
            self.lbl_Recc_Movie_10.setText(_translate("Dialog", title))
            self.lbl_Recc_Year_10.setText(_translate("Dialog", year))
            self.lbl_Recc_Rating_10.setText(_translate("Dialog", rating))
            self.lbl_Recc_Genres_10.setText(_translate("Dialog", genre_string))
            self.lbl_Recc_Plot_10.setText(_translate("Dialog", plot))

            self.lbl_Recc_Image_10.setPixmap(QPixmap(image))






    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1516, 771)

        self.btnGetSelection = QtWidgets.QPushButton(Dialog)
        self.btnGetSelection.setGeometry(QtCore.QRect(680, 290, 201, 60))
        self.btnGetSelection.setObjectName("btnGetSelection")
        self.btnGetSelection.clicked.connect(self.getSelection)

        self.btnGetRecommendations = QtWidgets.QPushButton(Dialog)
        self.btnGetRecommendations.setGeometry(QtCore.QRect(680, 380, 201, 60))
        self.btnGetRecommendations.setObjectName("btnGetRecommendations")
        self.btnGetRecommendations.clicked.connect(self.calculateRecommendation)

        self.groupBoxSearch = QtWidgets.QGroupBox(Dialog)
        self.groupBoxSearch.setGeometry(QtCore.QRect(590, 30, 371, 230))
        self.groupBoxSearch.setObjectName("groupBoxSearch")

        self.btnTitleSearch = QtWidgets.QPushButton(self.groupBoxSearch)
        self.btnTitleSearch.setGeometry(QtCore.QRect(250, 160, 88, 40))
        self.btnTitleSearch.setObjectName("btnTitleSearch")
        self.btnTitleSearch.clicked.connect(self.titleSearch)

        self.btnYearSearch = QtWidgets.QPushButton(self.groupBoxSearch)
        self.btnYearSearch.setGeometry(QtCore.QRect(140, 160, 88, 40))
        self.btnYearSearch.setObjectName("btnYearSearch")
        self.btnYearSearch.setObjectName("btnYearSearch")

        self.btnGenreSearch = QtWidgets.QPushButton(self.groupBoxSearch)
        self.btnGenreSearch.setGeometry(QtCore.QRect(40, 160, 88, 40))
        self.btnGenreSearch.setObjectName("btnGenreSearch")
        self.btnGenreSearch.clicked.connect(self.genreSearch)

        self.lblSearchTitle = QtWidgets.QLabel(self.groupBoxSearch)
        self.lblSearchTitle.setGeometry(QtCore.QRect(60, 60, 120, 18))
        self.lblSearchTitle.setObjectName("lblSearchTitle")

        self.lblSearchTypeTitle = QtWidgets.QLabel(self.groupBoxSearch)
        self.lblSearchTypeTitle.setGeometry(QtCore.QRect(140, 120, 90, 20))
        self.lblSearchTypeTitle.setObjectName("lblSearchTypeTitle")
        self.textboxSearch = QtWidgets.QLineEdit(self.groupBoxSearch)
        self.textboxSearch.setGeometry(QtCore.QRect(200, 50, 113, 32))
        self.textboxSearch.setObjectName("textboxSearch")
        self.groupBoxFilters = QtWidgets.QGroupBox(Dialog)
        self.groupBoxFilters.setGeometry(QtCore.QRect(600, 480, 341, 240))
        self.groupBoxFilters.setObjectName("groupBoxFilters")

        self.btnApplyFilter = QtWidgets.QPushButton(self.groupBoxFilters)
        self.btnApplyFilter.setGeometry(QtCore.QRect(210, 180, 88, 34))
        self.btnApplyFilter.setObjectName("btnApplyFilter")
        self.btnApplyFilter.clicked.connect(self.applyFilter)

        self.btnResetFilter = QtWidgets.QPushButton(self.groupBoxFilters)
        self.btnResetFilter.setGeometry(QtCore.QRect(50, 180, 88, 34))
        self.btnResetFilter.setObjectName("btnResetFilter")
        self.btnResetFilter.clicked.connect(self.resetFilter)

        self.textboxMinYear = QtWidgets.QLineEdit(self.groupBoxFilters)
        self.textboxMinYear.setGeometry(QtCore.QRect(160, 50, 140, 32))
        self.textboxMinYear.setObjectName("textboxMinYear")
        self.textboxMinRating = QtWidgets.QLineEdit(self.groupBoxFilters)
        self.textboxMinRating.setGeometry(QtCore.QRect(160, 110, 140, 32))
        self.textboxMinRating.setObjectName("textboxMinRating")
        self.labelYearTitle = QtWidgets.QLabel(self.groupBoxFilters)
        self.labelYearTitle.setGeometry(QtCore.QRect(60, 60, 60, 18))
        self.labelYearTitle.setObjectName("labelYearTitle")
        self.lblRatingTitle = QtWidgets.QLabel(self.groupBoxFilters)
        self.lblRatingTitle.setGeometry(QtCore.QRect(60, 120, 80, 18))
        self.lblRatingTitle.setObjectName("lblRatingTitle")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(40, 60, 471, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setSizeIncrement(QtCore.QSize(0, 0))
        self.scrollArea.setBaseSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 446, 2500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.groupBox_Results_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_1.setTitle("")
        self.groupBox_Results_1.setObjectName("groupBox_Results_1")
        self.lbl_Results_Year_1 = QtWidgets.QLabel(self.groupBox_Results_1)
        self.lbl_Results_Year_1.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_1.setObjectName("lbl_Results_Year_1")
        self.lbl_Results_Genres_1 = QtWidgets.QLabel(self.groupBox_Results_1)
        self.lbl_Results_Genres_1.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_1.setWordWrap(True)
        self.lbl_Results_Genres_1.setObjectName("lbl_Results_Genres_1")
        self.lblGenres = QtWidgets.QLabel(self.groupBox_Results_1)
        self.lblGenres.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres.setObjectName("lblGenres")
        self.btn_Results_Add_1 = QtWidgets.QPushButton(self.groupBox_Results_1)
        self.btn_Results_Add_1.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_1.setObjectName("btn_Results_Add_1")
        self.lbl_Result_Movie_1 = QtWidgets.QLabel(self.groupBox_Results_1)
        self.lbl_Result_Movie_1.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_1.setObjectName("lbl_Result_Movie_1")
        self.verticalLayout.addWidget(self.groupBox_Results_1)
        self.btn_Results_Add_1.clicked.connect(self.addSelection1)

        self.groupBox_Results_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_2.setTitle("")
        self.groupBox_Results_2.setObjectName("groupBox_Results_2")
        self.lbl_Results_Year_2 = QtWidgets.QLabel(self.groupBox_Results_2)
        self.lbl_Results_Year_2.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_2.setObjectName("lbl_Results_Year_2")
        self.lbl_Results_Genres_2 = QtWidgets.QLabel(self.groupBox_Results_2)
        self.lbl_Results_Genres_2.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_2.setWordWrap(True)
        self.lbl_Results_Genres_2.setObjectName("lbl_Results_Genres_2")
        self.lblGenres_2 = QtWidgets.QLabel(self.groupBox_Results_2)
        self.lblGenres_2.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_2.setObjectName("lblGenres_2")
        self.btn_Results_Add_2 = QtWidgets.QPushButton(self.groupBox_Results_2)
        self.btn_Results_Add_2.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_2.setObjectName("btn_Results_Add_2")
        self.lbl_Result_Movie_2 = QtWidgets.QLabel(self.groupBox_Results_2)
        self.lbl_Result_Movie_2.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_2.setObjectName("lbl_Result_Movie_2")
        self.verticalLayout.addWidget(self.groupBox_Results_2)
        self.btn_Results_Add_2.clicked.connect(self.addSelection2)

        self.groupBox_Results_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_3.setTitle("")
        self.groupBox_Results_3.setObjectName("groupBox_Results_3")
        self.lbl_Results_Year_3 = QtWidgets.QLabel(self.groupBox_Results_3)
        self.lbl_Results_Year_3.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_3.setObjectName("lbl_Results_Year_3")
        self.lbl_Results_Genres_3 = QtWidgets.QLabel(self.groupBox_Results_3)
        self.lbl_Results_Genres_3.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_3.setWordWrap(True)
        self.lbl_Results_Genres_3.setObjectName("lbl_Results_Genres_3")
        self.lblGenres_3 = QtWidgets.QLabel(self.groupBox_Results_3)
        self.lblGenres_3.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_3.setObjectName("lblGenres_3")
        self.btn_Results_Add_3 = QtWidgets.QPushButton(self.groupBox_Results_3)
        self.btn_Results_Add_3.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_3.setObjectName("btn_Results_Add_3")
        self.lbl_Result_Movie_3 = QtWidgets.QLabel(self.groupBox_Results_3)
        self.lbl_Result_Movie_3.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_3.setObjectName("lbl_Result_Movie_3")
        self.verticalLayout.addWidget(self.groupBox_Results_3)
        self.btn_Results_Add_3.clicked.connect(self.addSelection3)

        self.groupBox_Results_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_4.setTitle("")
        self.groupBox_Results_4.setObjectName("groupBox_Results_4")
        self.lbl_Results_Year_4 = QtWidgets.QLabel(self.groupBox_Results_4)
        self.lbl_Results_Year_4.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_4.setObjectName("lbl_Results_Year_4")
        self.lbl_Results_Genres_4 = QtWidgets.QLabel(self.groupBox_Results_4)
        self.lbl_Results_Genres_4.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_4.setWordWrap(True)
        self.lbl_Results_Genres_4.setObjectName("lbl_Results_Genres_4")
        self.lblGenres_4 = QtWidgets.QLabel(self.groupBox_Results_4)
        self.lblGenres_4.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_4.setObjectName("lblGenres_4")
        self.btn_Results_Add_4 = QtWidgets.QPushButton(self.groupBox_Results_4)
        self.btn_Results_Add_4.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_4.setObjectName("btn_Results_Add_4")
        self.lbl_Result_Movie_4 = QtWidgets.QLabel(self.groupBox_Results_4)
        self.lbl_Result_Movie_4.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_4.setObjectName("lbl_Result_Movie_4")
        self.verticalLayout.addWidget(self.groupBox_Results_4)
        self.btn_Results_Add_4.clicked.connect(self.addSelection4)

        self.groupBox_Results_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_5.setTitle("")
        self.groupBox_Results_5.setObjectName("groupBox_Results_5")
        self.lbl_Results_Year_5 = QtWidgets.QLabel(self.groupBox_Results_5)
        self.lbl_Results_Year_5.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_5.setObjectName("lbl_Results_Year_5")
        self.lbl_Results_Genres_5 = QtWidgets.QLabel(self.groupBox_Results_5)
        self.lbl_Results_Genres_5.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_5.setWordWrap(True)
        self.lbl_Results_Genres_5.setObjectName("lbl_Results_Genres_5")
        self.lblGenres_5 = QtWidgets.QLabel(self.groupBox_Results_5)
        self.lblGenres_5.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_5.setObjectName("lblGenres_5")
        self.btn_Results_Add_5 = QtWidgets.QPushButton(self.groupBox_Results_5)
        self.btn_Results_Add_5.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_5.setObjectName("btn_Results_Add_5")
        self.lbl_Result_Movie_5 = QtWidgets.QLabel(self.groupBox_Results_5)
        self.lbl_Result_Movie_5.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_5.setObjectName("lbl_Result_Movie_5")
        self.verticalLayout.addWidget(self.groupBox_Results_5)
        self.btn_Results_Add_5.clicked.connect(self.addSelection5)

        self.groupBox_Results_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_6.setTitle("")
        self.groupBox_Results_6.setObjectName("groupBox_Results_6")
        self.lbl_Results_Year_6 = QtWidgets.QLabel(self.groupBox_Results_6)
        self.lbl_Results_Year_6.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_6.setObjectName("lbl_Results_Year_6")
        self.lbl_Results_Genres_6 = QtWidgets.QLabel(self.groupBox_Results_6)
        self.lbl_Results_Genres_6.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_6.setWordWrap(True)
        self.lbl_Results_Genres_6.setObjectName("lbl_Results_Genres_6")
        self.lblGenres_6 = QtWidgets.QLabel(self.groupBox_Results_6)
        self.lblGenres_6.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_6.setObjectName("lblGenres_6")
        self.btn_Results_Add_6 = QtWidgets.QPushButton(self.groupBox_Results_6)
        self.btn_Results_Add_6.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_6.setObjectName("btn_Results_Add_6")
        self.lbl_Result_Movie_6 = QtWidgets.QLabel(self.groupBox_Results_6)
        self.lbl_Result_Movie_6.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_6.setObjectName("lbl_Result_Movie_6")
        self.verticalLayout.addWidget(self.groupBox_Results_6)
        self.btn_Results_Add_6.clicked.connect(self.addSelection6)

        self.groupBox_Results_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_7.setTitle("")
        self.groupBox_Results_7.setObjectName("groupBox_Results_7")
        self.lbl_Results_Year_7 = QtWidgets.QLabel(self.groupBox_Results_7)
        self.lbl_Results_Year_7.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_7.setObjectName("lbl_Results_Year_7")
        self.lbl_Results_Genres_7 = QtWidgets.QLabel(self.groupBox_Results_7)
        self.lbl_Results_Genres_7.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_7.setWordWrap(True)
        self.lbl_Results_Genres_7.setObjectName("lbl_Results_Genres_7")
        self.lblGenres_7 = QtWidgets.QLabel(self.groupBox_Results_7)
        self.lblGenres_7.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_7.setObjectName("lblGenres_7")
        self.btn_Results_Add_7 = QtWidgets.QPushButton(self.groupBox_Results_7)
        self.btn_Results_Add_7.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_7.setObjectName("btn_Results_Add_7")
        self.lbl_Result_Movie_7 = QtWidgets.QLabel(self.groupBox_Results_7)
        self.lbl_Result_Movie_7.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_7.setObjectName("lbl_Result_Movie_7")
        self.verticalLayout.addWidget(self.groupBox_Results_7)
        self.btn_Results_Add_7.clicked.connect(self.addSelection7)

        self.groupBox_Results_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_8.setTitle("")
        self.groupBox_Results_8.setObjectName("groupBox_Results_8")
        self.lbl_Results_Year_8 = QtWidgets.QLabel(self.groupBox_Results_8)
        self.lbl_Results_Year_8.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_8.setObjectName("lbl_Results_Year_8")
        self.lbl_Results_Genres_8 = QtWidgets.QLabel(self.groupBox_Results_8)
        self.lbl_Results_Genres_8.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_8.setWordWrap(True)
        self.lbl_Results_Genres_8.setObjectName("lbl_Results_Genres_8")
        self.lblGenres_8 = QtWidgets.QLabel(self.groupBox_Results_8)
        self.lblGenres_8.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_8.setObjectName("lblGenres_8")
        self.btn_Results_Add_8 = QtWidgets.QPushButton(self.groupBox_Results_8)
        self.btn_Results_Add_8.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_8.setObjectName("btn_Results_Add_8")
        self.lbl_Result_Movie_8 = QtWidgets.QLabel(self.groupBox_Results_8)
        self.lbl_Result_Movie_8.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_8.setObjectName("lbl_Result_Movie_8")
        self.verticalLayout.addWidget(self.groupBox_Results_8)
        self.btn_Results_Add_8.clicked.connect(self.addSelection8)

        self.groupBox_Results_9 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_9.setTitle("")
        self.groupBox_Results_9.setObjectName("groupBox_Results_9")
        self.lbl_Results_Year_9 = QtWidgets.QLabel(self.groupBox_Results_9)
        self.lbl_Results_Year_9.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_9.setObjectName("lbl_Results_Year_9")
        self.lbl_Results_Genres_9 = QtWidgets.QLabel(self.groupBox_Results_9)
        self.lbl_Results_Genres_9.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_9.setWordWrap(True)
        self.lbl_Results_Genres_9.setObjectName("lbl_Results_Genres_9")
        self.lblGenres_9 = QtWidgets.QLabel(self.groupBox_Results_9)
        self.lblGenres_9.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_9.setObjectName("lblGenres_9")
        self.btn_Results_Add_9 = QtWidgets.QPushButton(self.groupBox_Results_9)
        self.btn_Results_Add_9.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_9.setObjectName("btn_Results_Add_9")
        self.lbl_Result_Movie_9 = QtWidgets.QLabel(self.groupBox_Results_9)
        self.lbl_Result_Movie_9.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_9.setObjectName("lbl_Result_Movie_9")
        self.verticalLayout.addWidget(self.groupBox_Results_9)
        self.btn_Results_Add_9.clicked.connect(self.addSelection9)

        self.groupBox_Results_10 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Results_10.setTitle("")
        self.groupBox_Results_10.setObjectName("groupBox_Results_10")
        self.lbl_Results_Year_10 = QtWidgets.QLabel(self.groupBox_Results_10)
        self.lbl_Results_Year_10.setGeometry(QtCore.QRect(60, 70, 151, 18))
        self.lbl_Results_Year_10.setObjectName("lbl_Results_Year_10")
        self.lbl_Results_Genres_10 = QtWidgets.QLabel(self.groupBox_Results_10)
        self.lbl_Results_Genres_10.setGeometry(QtCore.QRect(70, 130, 221, 51))
        self.lbl_Results_Genres_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Results_Genres_10.setWordWrap(True)
        self.lbl_Results_Genres_10.setObjectName("lbl_Results_Genres_10")
        self.lblGenres_10 = QtWidgets.QLabel(self.groupBox_Results_10)
        self.lblGenres_10.setGeometry(QtCore.QRect(60, 110, 58, 18))
        self.lblGenres_10.setObjectName("lblGenres_10")
        self.btn_Results_Add_10 = QtWidgets.QPushButton(self.groupBox_Results_10)
        self.btn_Results_Add_10.setGeometry(QtCore.QRect(60, 180, 171, 34))
        self.btn_Results_Add_10.setObjectName("btn_Results_Add_10")
        self.lbl_Result_Movie_10 = QtWidgets.QLabel(self.groupBox_Results_10)
        self.lbl_Result_Movie_10.setGeometry(QtCore.QRect(60, 30, 301, 18))
        self.lbl_Result_Movie_10.setObjectName("lbl_Result_Movie_10")
        self.verticalLayout.addWidget(self.groupBox_Results_10)
        self.btn_Results_Add_10.clicked.connect(self.addSelection10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 30, 434, 18))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(1020, 50, 471, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.scrollArea_2.setBaseSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -3853, 446, 4500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.groupBox_Recc_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_1.setTitle("")
        self.groupBox_Recc_1.setObjectName("groupBox_Recc_1")
        self.lbl_Recc_Image_1 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lbl_Recc_Image_1.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_1.setAutoFillBackground(False)
        self.lbl_Recc_Image_1.setText("")
        self.lbl_Recc_Image_1.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_1.setScaledContents(True)
        self.lbl_Recc_Image_1.setObjectName("lbl_Recc_Image_1")
        self.lbl_Recc_Rating_1 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lbl_Recc_Rating_1.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_1.setObjectName("lbl_Recc_Rating_1")
        self.lbl_Recc_Plot_1 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lbl_Recc_Plot_1.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_1.setWordWrap(True)
        self.lbl_Recc_Plot_1.setObjectName("lbl_Recc_Plot_1")
        self.lbl_Recc_Year_1 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lbl_Recc_Year_1.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_1.setObjectName("lbl_Recc_Year_1")
        self.lbl_Recc_Genres_1 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lbl_Recc_Genres_1.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_1.setWordWrap(True)
        self.lbl_Recc_Genres_1.setObjectName("lbl_Recc_Genres_1")
        self.lblPlot_20 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lblPlot_20.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_20.setObjectName("lblPlot_20")
        self.lblGenres_20 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lblGenres_20.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_20.setObjectName("lblGenres_20")
        self.btn_Recc_Add_1 = QtWidgets.QPushButton(self.groupBox_Recc_1)
        self.btn_Recc_Add_1.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_1.setObjectName("btn_Recc_Add_1")
        self.lbl_Recc_Movie_1 = QtWidgets.QLabel(self.groupBox_Recc_1)
        self.lbl_Recc_Movie_1.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_1.setObjectName("lbl_Recc_Movie_1")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_1)
        self.btn_Recc_Add_1.clicked.connect(self.addSelection1)

        self.groupBox_Recc_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_2.setTitle("")
        self.groupBox_Recc_2.setObjectName("groupBox_Recc_2")
        self.lbl_Recc_Image_2 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lbl_Recc_Image_2.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_2.setAutoFillBackground(False)
        self.lbl_Recc_Image_2.setText("")
        self.lbl_Recc_Image_2.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_2.setScaledContents(True)
        self.lbl_Recc_Image_2.setObjectName("lbl_Recc_Image_2")
        self.lbl_Recc_Rating_2 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lbl_Recc_Rating_2.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_2.setObjectName("lbl_Recc_Rating_2")
        self.lbl_Recc_Plot_2 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lbl_Recc_Plot_2.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_2.setWordWrap(True)
        self.lbl_Recc_Plot_2.setObjectName("lbl_Recc_Plot_2")
        self.lbl_Recc_Year_2 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lbl_Recc_Year_2.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_2.setObjectName("lbl_Recc_Year_2")
        self.lbl_Recc_Genres_2 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lbl_Recc_Genres_2.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_2.setWordWrap(True)
        self.lbl_Recc_Genres_2.setObjectName("lbl_Recc_Genres_2")
        self.lblPlot_21 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lblPlot_21.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_21.setObjectName("lblPlot_21")
        self.lblGenres_21 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lblGenres_21.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_21.setObjectName("lblGenres_21")
        self.btn_Recc_Add_2 = QtWidgets.QPushButton(self.groupBox_Recc_2)
        self.btn_Recc_Add_2.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_2.setObjectName("btn_Recc_Add_2")
        self.lbl_Recc_Movie_2 = QtWidgets.QLabel(self.groupBox_Recc_2)
        self.lbl_Recc_Movie_2.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_2.setObjectName("lbl_Recc_Movie_2")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_2)
        self.btn_Recc_Add_2.clicked.connect(self.addSelection2)

        self.groupBox_Recc_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_3.setTitle("")
        self.groupBox_Recc_3.setObjectName("groupBox_Recc_3")
        self.lbl_Recc_Image_3 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lbl_Recc_Image_3.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_3.setAutoFillBackground(False)
        self.lbl_Recc_Image_3.setText("")
        self.lbl_Recc_Image_3.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_3.setScaledContents(True)
        self.lbl_Recc_Image_3.setObjectName("lbl_Recc_Image_3")
        self.lbl_Recc_Rating_3 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lbl_Recc_Rating_3.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_3.setObjectName("lbl_Recc_Rating_3")
        self.lbl_Recc_Plot_3 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lbl_Recc_Plot_3.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_3.setWordWrap(True)
        self.lbl_Recc_Plot_3.setObjectName("lbl_Recc_Plot_3")
        self.lbl_Recc_Year_3 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lbl_Recc_Year_3.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_3.setObjectName("lbl_Recc_Year_3")
        self.lbl_Recc_Genres_3 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lbl_Recc_Genres_3.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_3.setWordWrap(True)
        self.lbl_Recc_Genres_3.setObjectName("lbl_Recc_Genres_3")
        self.lblPlot_22 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lblPlot_22.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_22.setObjectName("lblPlot_22")
        self.lblGenres_22 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lblGenres_22.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_22.setObjectName("lblGenres_22")
        self.btn_Recc_Add_3 = QtWidgets.QPushButton(self.groupBox_Recc_3)
        self.btn_Recc_Add_3.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_3.setObjectName("btn_Recc_Add_3")
        self.lbl_Recc_Movie_3 = QtWidgets.QLabel(self.groupBox_Recc_3)
        self.lbl_Recc_Movie_3.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_3.setObjectName("lbl_Recc_Movie_3")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_3)
        self.btn_Recc_Add_3.clicked.connect(self.addSelection3)

        self.groupBox_Recc_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_4.setTitle("")
        self.groupBox_Recc_4.setObjectName("groupBox_Recc_4")
        self.lbl_Recc_Image_4 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lbl_Recc_Image_4.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_4.setAutoFillBackground(False)
        self.lbl_Recc_Image_4.setText("")
        self.lbl_Recc_Image_4.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_4.setScaledContents(True)
        self.lbl_Recc_Image_4.setObjectName("lbl_Recc_Image_4")
        self.lbl_Recc_Rating_4 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lbl_Recc_Rating_4.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_4.setObjectName("lbl_Recc_Rating_4")
        self.lbl_Recc_Plot_4 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lbl_Recc_Plot_4.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_4.setWordWrap(True)
        self.lbl_Recc_Plot_4.setObjectName("lbl_Recc_Plot_4")
        self.lbl_Recc_Year_4 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lbl_Recc_Year_4.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_4.setObjectName("lbl_Recc_Year_4")
        self.lbl_Recc_Genres_4 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lbl_Recc_Genres_4.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_4.setWordWrap(True)
        self.lbl_Recc_Genres_4.setObjectName("lbl_Recc_Genres_4")
        self.lblPlot_23 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lblPlot_23.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_23.setObjectName("lblPlot_23")
        self.lblGenres_23 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lblGenres_23.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_23.setObjectName("lblGenres_23")
        self.btn_Recc_Add_4 = QtWidgets.QPushButton(self.groupBox_Recc_4)
        self.btn_Recc_Add_4.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_4.setObjectName("btn_Recc_Add_4")
        self.lbl_Recc_Movie_4 = QtWidgets.QLabel(self.groupBox_Recc_4)
        self.lbl_Recc_Movie_4.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_4.setObjectName("lbl_Recc_Movie_4")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_4)
        self.btn_Recc_Add_4.clicked.connect(self.addSelection4)

        self.groupBox_Recc_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_5.setTitle("")
        self.groupBox_Recc_5.setObjectName("groupBox_Recc_5")
        self.lbl_Recc_Image_5 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lbl_Recc_Image_5.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_5.setAutoFillBackground(False)
        self.lbl_Recc_Image_5.setText("")
        self.lbl_Recc_Image_5.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_5.setScaledContents(True)
        self.lbl_Recc_Image_5.setObjectName("lbl_Recc_Image_5")
        self.lbl_Recc_Rating_5 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lbl_Recc_Rating_5.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_5.setObjectName("lbl_Recc_Rating_5")
        self.lbl_Recc_Plot_5 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lbl_Recc_Plot_5.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_5.setWordWrap(True)
        self.lbl_Recc_Plot_5.setObjectName("lbl_Recc_Plot_5")
        self.lbl_Recc_Year_5 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lbl_Recc_Year_5.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_5.setObjectName("lbl_Recc_Year_5")
        self.lbl_Recc_Genres_5 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lbl_Recc_Genres_5.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_5.setWordWrap(True)
        self.lbl_Recc_Genres_5.setObjectName("lbl_Recc_Genres_5")
        self.lblPlot_24 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lblPlot_24.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_24.setObjectName("lblPlot_24")
        self.lblGenres_24 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lblGenres_24.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_24.setObjectName("lblGenres_24")
        self.btn_Recc_Add_5 = QtWidgets.QPushButton(self.groupBox_Recc_5)
        self.btn_Recc_Add_5.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_5.setObjectName("btn_Recc_Add_5")
        self.lbl_Recc_Movie_5 = QtWidgets.QLabel(self.groupBox_Recc_5)
        self.lbl_Recc_Movie_5.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_5.setObjectName("lbl_Recc_Movie_5")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_5)
        self.btn_Recc_Add_5.clicked.connect(self.addSelection5)

        self.groupBox_Recc_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_6.setTitle("")
        self.groupBox_Recc_6.setObjectName("groupBox_Recc_6")
        self.lbl_Recc_Image_6 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lbl_Recc_Image_6.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_6.setAutoFillBackground(False)
        self.lbl_Recc_Image_6.setText("")
        self.lbl_Recc_Image_6.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_6.setScaledContents(True)
        self.lbl_Recc_Image_6.setObjectName("lbl_Recc_Image_6")
        self.lbl_Recc_Rating_6 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lbl_Recc_Rating_6.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_6.setObjectName("lbl_Recc_Rating_6")
        self.lbl_Recc_Plot_6 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lbl_Recc_Plot_6.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_6.setWordWrap(True)
        self.lbl_Recc_Plot_6.setObjectName("lbl_Recc_Plot_6")
        self.lbl_Recc_Year_6 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lbl_Recc_Year_6.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_6.setObjectName("lbl_Recc_Year_6")
        self.lbl_Recc_Genres_6 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lbl_Recc_Genres_6.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_6.setWordWrap(True)
        self.lbl_Recc_Genres_6.setObjectName("lbl_Recc_Genres_6")
        self.lblPlot_25 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lblPlot_25.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_25.setObjectName("lblPlot_25")
        self.lblGenres_25 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lblGenres_25.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_25.setObjectName("lblGenres_25")
        self.btn_Recc_Add_6 = QtWidgets.QPushButton(self.groupBox_Recc_6)
        self.btn_Recc_Add_6.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_6.setObjectName("btn_Recc_Add_6")
        self.lbl_Recc_Movie_6 = QtWidgets.QLabel(self.groupBox_Recc_6)
        self.lbl_Recc_Movie_6.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_6.setObjectName("lbl_Recc_Movie_6")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_6)
        self.btn_Recc_Add_6.clicked.connect(self.addSelection6)

        self.groupBox_Recc_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_7.setTitle("")
        self.groupBox_Recc_7.setObjectName("groupBox_Recc_7")
        self.lbl_Recc_Image_7 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lbl_Recc_Image_7.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_7.setAutoFillBackground(False)
        self.lbl_Recc_Image_7.setText("")
        self.lbl_Recc_Image_7.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_7.setScaledContents(True)
        self.lbl_Recc_Image_7.setObjectName("lbl_Recc_Image_7")
        self.lbl_Recc_Rating_7 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lbl_Recc_Rating_7.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_7.setObjectName("lbl_Recc_Rating_7")
        self.lbl_Recc_Plot_7 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lbl_Recc_Plot_7.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_7.setWordWrap(True)
        self.lbl_Recc_Plot_7.setObjectName("lbl_Recc_Plot_7")
        self.lbl_Recc_Year_7 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lbl_Recc_Year_7.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_7.setObjectName("lbl_Recc_Year_7")
        self.lbl_Recc_Genres_7 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lbl_Recc_Genres_7.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_7.setWordWrap(True)
        self.lbl_Recc_Genres_7.setObjectName("lbl_Recc_Genres_7")
        self.lblPlot_26 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lblPlot_26.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_26.setObjectName("lblPlot_26")
        self.lblGenres_26 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lblGenres_26.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_26.setObjectName("lblGenres_26")
        self.btn_Recc_Add_7 = QtWidgets.QPushButton(self.groupBox_Recc_7)
        self.btn_Recc_Add_7.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_7.setObjectName("btn_Recc_Add_7")
        self.lbl_Recc_Movie_7 = QtWidgets.QLabel(self.groupBox_Recc_7)
        self.lbl_Recc_Movie_7.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_7.setObjectName("lbl_Recc_Movie_7")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_7)
        self.btn_Recc_Add_7.clicked.connect(self.addSelection7)

        self.groupBox_Recc_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_8.setTitle("")
        self.groupBox_Recc_8.setObjectName("groupBox_Recc_8")
        self.lbl_Recc_Image_8 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lbl_Recc_Image_8.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_8.setAutoFillBackground(False)
        self.lbl_Recc_Image_8.setText("")
        self.lbl_Recc_Image_8.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_8.setScaledContents(True)
        self.lbl_Recc_Image_8.setObjectName("lbl_Recc_Image_8")
        self.lbl_Recc_Rating_8 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lbl_Recc_Rating_8.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_8.setObjectName("lbl_Recc_Rating_8")
        self.lbl_Recc_Plot_8 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lbl_Recc_Plot_8.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_8.setWordWrap(True)
        self.lbl_Recc_Plot_8.setObjectName("lbl_Recc_Plot_8")
        self.lbl_Recc_Year_8 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lbl_Recc_Year_8.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_8.setObjectName("lbl_Recc_Year_8")
        self.lbl_Recc_Genres_8 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lbl_Recc_Genres_8.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_8.setWordWrap(True)
        self.lbl_Recc_Genres_8.setObjectName("lbl_Recc_Genres_8")
        self.lblPlot_27 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lblPlot_27.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_27.setObjectName("lblPlot_27")
        self.lblGenres_27 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lblGenres_27.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_27.setObjectName("lblGenres_27")
        self.btn_Recc_Add_8 = QtWidgets.QPushButton(self.groupBox_Recc_8)
        self.btn_Recc_Add_8.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_8.setObjectName("btn_Recc_Add_8")
        self.lbl_Recc_Movie_8 = QtWidgets.QLabel(self.groupBox_Recc_8)
        self.lbl_Recc_Movie_8.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_8.setObjectName("lbl_Recc_Movie_8")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_8)
        self.btn_Recc_Add_8.clicked.connect(self.addSelection8)

        self.groupBox_Recc_9 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_9.setTitle("")
        self.groupBox_Recc_9.setObjectName("groupBox_Recc_9")
        self.lbl_Recc_Image_9 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lbl_Recc_Image_9.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_9.setAutoFillBackground(False)
        self.lbl_Recc_Image_9.setText("")
        self.lbl_Recc_Image_9.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_9.setScaledContents(True)
        self.lbl_Recc_Image_9.setObjectName("lbl_Recc_Image_9")
        self.lbl_Recc_Rating_9 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lbl_Recc_Rating_9.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_9.setObjectName("lbl_Recc_Rating_9")
        self.lbl_Recc_Plot_9 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lbl_Recc_Plot_9.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_9.setWordWrap(True)
        self.lbl_Recc_Plot_9.setObjectName("lbl_Recc_Plot_9")
        self.lbl_Recc_Year_9 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lbl_Recc_Year_9.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_9.setObjectName("lbl_Recc_Year_9")
        self.lbl_Recc_Genres_9 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lbl_Recc_Genres_9.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_9.setWordWrap(True)
        self.lbl_Recc_Genres_9.setObjectName("lbl_Recc_Genres_9")
        self.lblPlot_28 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lblPlot_28.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_28.setObjectName("lblPlot_28")
        self.lblGenres_28 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lblGenres_28.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_28.setObjectName("lblGenres_28")
        self.btn_Recc_Add_9 = QtWidgets.QPushButton(self.groupBox_Recc_9)
        self.btn_Recc_Add_9.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_9.setObjectName("btn_Recc_Add_9")
        self.lbl_Recc_Movie_9 = QtWidgets.QLabel(self.groupBox_Recc_9)
        self.lbl_Recc_Movie_9.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_9.setObjectName("lbl_Recc_Movie_9")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_9)
        self.btn_Recc_Add_9.clicked.connect(self.addSelection9)

        self.groupBox_Recc_10 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Recc_10.setTitle("")
        self.groupBox_Recc_10.setObjectName("groupBox_Recc_10")
        self.lbl_Recc_Image_10 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lbl_Recc_Image_10.setGeometry(QtCore.QRect(20, 20, 171, 220))
        self.lbl_Recc_Image_10.setAutoFillBackground(False)
        self.lbl_Recc_Image_10.setText("")
        self.lbl_Recc_Image_10.setPixmap(QtGui.QPixmap("../../../../../Pictures/GIF/tumblr_p69334HRQC1qze3hdo1_500.gif"))
        self.lbl_Recc_Image_10.setScaledContents(True)
        self.lbl_Recc_Image_10.setObjectName("lbl_Recc_Image_10")
        self.lbl_Recc_Rating_10 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lbl_Recc_Rating_10.setGeometry(QtCore.QRect(210, 90, 151, 18))
        self.lbl_Recc_Rating_10.setObjectName("lbl_Recc_Rating_10")
        self.lbl_Recc_Plot_10 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lbl_Recc_Plot_10.setGeometry(QtCore.QRect(30, 280, 391, 121))
        self.lbl_Recc_Plot_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Plot_10.setWordWrap(True)
        self.lbl_Recc_Plot_10.setObjectName("lbl_Recc_Plot_10")
        self.lbl_Recc_Year_10 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lbl_Recc_Year_10.setGeometry(QtCore.QRect(210, 60, 151, 18))
        self.lbl_Recc_Year_10.setObjectName("lbl_Recc_Year_10")
        self.lbl_Recc_Genres_10 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lbl_Recc_Genres_10.setGeometry(QtCore.QRect(220, 150, 191, 51))
        self.lbl_Recc_Genres_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Recc_Genres_10.setWordWrap(True)
        self.lbl_Recc_Genres_10.setObjectName("lbl_Recc_Genres_10")
        self.lblPlot_29 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lblPlot_29.setGeometry(QtCore.QRect(20, 260, 58, 18))
        self.lblPlot_29.setObjectName("lblPlot_29")
        self.lblGenres_29 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lblGenres_29.setGeometry(QtCore.QRect(210, 130, 58, 18))
        self.lblGenres_29.setObjectName("lblGenres_29")
        self.btn_Recc_Add_10 = QtWidgets.QPushButton(self.groupBox_Recc_10)
        self.btn_Recc_Add_10.setGeometry(QtCore.QRect(220, 210, 171, 34))
        self.btn_Recc_Add_10.setObjectName("btn_Recc_Add_10")
        self.lbl_Recc_Movie_10 = QtWidgets.QLabel(self.groupBox_Recc_10)
        self.lbl_Recc_Movie_10.setGeometry(QtCore.QRect(210, 30, 150, 18))
        self.lbl_Recc_Movie_10.setObjectName("lbl_Recc_Movie_10")
        self.verticalLayout_2.addWidget(self.groupBox_Recc_10)
        self.btn_Recc_Add_10.clicked.connect(self.addSelection10)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(1030, 20, 434, 18))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnGetSelection.setText(_translate("Dialog", "Show Your Selected Movies"))
        self.btnGetRecommendations.setText(_translate("Dialog", "Show Recommended Movies"))
        self.groupBoxSearch.setTitle(_translate("Dialog", "Search"))
        self.btnTitleSearch.setText(_translate("Dialog", "By Title"))
        self.btnYearSearch.setText(_translate("Dialog", "By Year"))
        self.btnGenreSearch.setText(_translate("Dialog", "By Genre"))
        self.lblSearchTitle.setText(_translate("Dialog", "Enter Search Term:"))
        self.lblSearchTypeTitle.setText(_translate("Dialog", "Search by type"))
        self.groupBoxFilters.setTitle(_translate("Dialog", "Recommendation Filters"))
        self.btnApplyFilter.setText(_translate("Dialog", "Apply Filter"))
        self.btnResetFilter.setText(_translate("Dialog", "Reset Filter"))
        self.labelYearTitle.setText(_translate("Dialog", "Min Year:"))
        self.lblRatingTitle.setText(_translate("Dialog", "Min Rating:"))
        self.lbl_Results_Year_1.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_1.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_1.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_1.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_2.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_2.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_2.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_2.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_2.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_3.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_3.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_3.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_3.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_3.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_4.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_4.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_4.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_4.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_4.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_5.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_5.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_5.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_5.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_5.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_6.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_6.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_6.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_6.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_6.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_7.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_7.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_7.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_7.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_7.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_8.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_8.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_8.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_8.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_8.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_9.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_9.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_9.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_9.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_9.setText(_translate("Dialog", "Title:"))
        self.lbl_Results_Year_10.setText(_translate("Dialog", "Year:"))
        self.lbl_Results_Genres_10.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblGenres_10.setText(_translate("Dialog", "Genres:"))
        self.btn_Results_Add_10.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Result_Movie_10.setText(_translate("Dialog", "Title:"))
        self.label_6.setText(_translate("Dialog", "Search Results: Title - \"keyword\""))
        self.lbl_Recc_Rating_1.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_1.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_1.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_1.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_20.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_20.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_1.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_1.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_2.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_2.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_2.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_2.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_21.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_21.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_2.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_2.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_3.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_3.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_3.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_3.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_22.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_22.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_3.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_3.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_4.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_4.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_4.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_4.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_23.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_23.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_4.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_4.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_5.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_5.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_5.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_5.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_24.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_24.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_5.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_5.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_6.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_6.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_6.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_6.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_25.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_25.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_6.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_6.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_7.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_7.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_7.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_7.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_26.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_26.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_7.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_7.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_8.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_8.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_8.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_8.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_27.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_27.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_8.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_8.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_9.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_9.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_9.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_9.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_28.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_28.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_9.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_9.setText(_translate("Dialog", "Title:"))
        self.lbl_Recc_Rating_10.setText(_translate("Dialog", "Rating:"))
        self.lbl_Recc_Plot_10.setText(_translate("Dialog", "A young man walks into a circus only to find out his long lost brother is the main performonce."))
        self.lbl_Recc_Year_10.setText(_translate("Dialog", "Year:"))
        self.lbl_Recc_Genres_10.setText(_translate("Dialog", "Action, Adventure, Comedy, Horror, Thriller, Sci-Fi, Romance"))
        self.lblPlot_29.setText(_translate("Dialog", "Plot:"))
        self.lblGenres_29.setText(_translate("Dialog", "Genres:"))
        self.btn_Recc_Add_10.setText(_translate("Dialog", "Add movie to selection"))
        self.lbl_Recc_Movie_10.setText(_translate("Dialog", "Title:"))
        self.label_7.setText(_translate("Dialog", "Recommendations List"))

def runGUI():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    runGUI()

