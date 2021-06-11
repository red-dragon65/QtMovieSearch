'''
3580: Recommendation Engine
Author: Mujtaba Ashfaq
Date: 3/23/21

This is a content based movie search engine.
'''
# Used to run the movie search engine in a GUI
import MovieGui as mg

# Used to run the movie search engine in the console
import MovieTextUI as mtu



# Menu to ask user what version of movie search engine they want to run

print("Welcome to the movie search engine!")
print()
print("Enter 1 for console version")
print("Enter 2 for GUI version")

print()
print("Your input: ", end="")

input = input()

if input == "1":
    mtu.textMenu()

if input == "2":
    mg.runGUI()


