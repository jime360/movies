# First I need to import what I'll use in this app, from other files

import fresh_tomatoes
import media

############################################################################################################
#                                                                                                          #
# Here you can find all instance from Movie class. Each instance will need to send 4 parameters to Movie.  #
# You can add as many instances as you want.                                                               #
#                                                                                                          #
# Since the story line of the movie can be long, you can either send it as a parameter or add it in a txt  #
# file, in the same path of the rest of the files.                                                         #
#                                                                                                          #
# This is an example on how to add a new instance (with the storyline in a txt):                           #
#                                                                                                          #
# text = open("example_storyline_text.txt")                                                                #
# example_storyline = text.read()                                                                          #
#                                                                                                          #
# example_name_of_the_movie = media.Movie("name of the movie",                                             #
#                                         example_storyline,                                               #
#                                         "url to some jpg or image with the poster of the movie",         #
#                                         "url of youtube with the trailer of the movie")                  #
#                                                                                                          #
############################################################################################################


# Here I go to the txt that contains the storyline of this movie and I save it in a variable to use it later

text = open("fast.txt")
fast_storyline = text.read()

# Here I send the parameters to Movie

fast = media.Movie("The Fast and the Furious",
                   fast_storyline,
                   "http://goo.gl/5Z38VZ",
                   "https://www.youtube.com/watch?v=ZsJz2TJAPjw")


# Here I go to the txt that contains the storyline of this movie and I save it in a variable to use it later

text = open("four_weddings.txt")
four_weddings_storyline = text.read()

# Here I send the parameters to Movie

four_weddings = media.Movie("Four weddings and a funeral",
                            four_weddings_storyline,
                            "http://goo.gl/Qq10GD",
                            "https://www.youtube.com/watch?v=ZHyCtw6BB20")


# Here I go to the txt that contains the storyline of this movie and I save it in a variable to use it later

text = open("harry_sally.txt")
harry_sally_storyline = text.read()

# Here I send the parameters to Movie

harry_sally = media.Movie("when harry met sally",
                          harry_sally_storyline,
                          "http://goo.gl/2tdFdi",
                          "https://www.youtube.com/watch?v=V8DgDmUHVto")


# Here I go to the txt that contains the storyline of this movie and I save it in a variable to use it later
                          
text = open("carroza.txt")
carroza_storyline = text.read()

# Here I send the parameters to Movie

carroza = media.Movie("Esperando la carroza",
                      carroza_storyline,
                      "https://goo.gl/a4b4SR",
                      "https://www.youtube.com/watch?v=KIgOuEPQZsU")


# Here I go to the txt that contains the storyline of this movie and I save it in a variable to use it later

text = open("fifty_first.txt")
fifty_first_storyline = text.read()

# Here I send the parameters to Movie
                          
fifty_first = media.Movie("Fifty first dates",
                          fifty_first_storyline,
                          "https://goo.gl/k2dVob",
                          "https://www.youtube.com/watch?v=ErjP5xMTc8I")


# Here I go to the txt that contains the storyline of this movie and I save it in a variable to use it later
                          
text = open("matrix.txt")
matrix_storyline = text.read()

# Here I send the parameters to Movie

matrix = media.Movie("Matrix",
                     matrix_storyline,
                     "http://goo.gl/dqXYqo",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")




# This is the list of movies that I'll send to fresh_tomatoes to show in the web
# If you add a new instance/movie, you will need to add it to this list:

movies =[carroza,fast, four_weddings, harry_sally, fifty_first, matrix]

# Finally, I send the list of movies to fresh_tomatoes

fresh_tomatoes.open_movies_page(movies)
