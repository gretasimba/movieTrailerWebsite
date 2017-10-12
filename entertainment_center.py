import media  # class Movie initates in media.py
import fresh_tomatoes  # class generates fresh_tomatoes.html

""" creates 6 instances of class Movies to create "my favore movies" website.
Each instance pass 4 attributes to class Movie: movie_title as string,
movie_storyline as string, poster_url as string, youtube_trailer as string.
Then creates list with all 6 instances included.
Last it calls fresh_tomatoes.open_movies_page, which creates HTML page that
displays movies with title, and poster images. Movie trailer from YouTube
shows whem poster omage is clicked.
Method takes movies (list) as argument"""


# initialises movie "It"
it = media.Movie("It",
                 "A group of young kids are faced with their biggest fears",
                 "http://cdn6.ihorror.com/app/uploads/17632177_1388557637831190_3930730815628374813_o-2.jpg",
                 "https://www.youtube.com/watch?v=FnCdOQsX5kc")
# initialises movie "Amadeus"
amadeus = media.Movie("Amadeus",
                      "Antonio Salieri believes that Wolfgang Amadeus"
                      "Mozart's music is divine and miraculous",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcRszKttX-DHHFm8ZRtTqUCrUYGS34C5clU2Shgw2nlEEle7heDN",
                      "https://www.youtube.com/watch?v=yIzhAKtEzY0")
# initialises movie "The Big Lebowski"
lebowski = media.Movie("The Big Lebowski",
                       "Jeff Bridges plays Jeff Lebowski who insists on being"
                       "called ""the Dude,"" a laid-back, easygoing burnout"
                       "who happens to have the same name as a millionaire"
                       "whose wife owes a lot of dangerous people"
                       "a whole bunch of money -- resulting in "
                       "the Dude having his rug soiled,sending him"
                       "spiraling into the Los Angeles underworld.",
                       "http://t3.gstatic.com/images?q=tbn:ANd9GcRBYp315X-0pNvI-Dvqj8FR0AGdF39VCprXpurd0cQel__e17CP",
                       "https://www.youtube.com/watch?v=cd-go0oBF4Y")
# initialises movie "The Icredibles"
incredibles = media.Movie("The Icredibles",
                          "In this lauded Pixar animated film,"
                          " married superheroes Mr. Incredible"
                          "(Craig T. Nelson) and Elastigirl (Holly Hunter)"
                          "are forced to assume mundane lives as Bob and"
                          "Helen Parr after all super-powered activities"
                          "have been banned by the government."
                          "While Mr. Incredible  loves his "
                          "wife and kids, he longs to return to"
                          " a life of adventure, and he gets a"
                          "chance when summoned to an island "
                          "to battle an out-of-control robot."
                          "Soon, Mr. Incredible is in trouble, and it's"
                          "up to his family to save him",
                          "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                          "https://www.youtube.com/watch?v=eZbzbC9285I")
# initialises movie "Apocalypse Now"
apocalypse = media.Movie("Apocalypse Now",
                         "In Vietnam in 1970, Captain Willard"
                         " (Martin Sheen) takes a perilous and"
                         " increasingly hallucinatory journey "
                         "upriver to find and terminate Colonel Kurtz"
                         "(Marlon Brando), a once-promising officer"
                         " who has reportedly gone completely mad."
                         "In the company of a Navy patrol boat filled"
                         "with street-smart kids",
                         "https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
                         "https://www.youtube.com/watch?v=IkrhkUeDCdQ")
# initialises movie "Fight Club"
fight_club = media.Movie("Fight Club",
                         "A depressed man (Edward Norton) suffering"
                         "from insomnia meets a strange"
                         "soap salesman named Tyler Durden"
                         "(Brad Pitt) and soon finds himself"
                         "living in his squalid house"
                         "after his perfect apartment is destroyed...",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=J8FRBYOFu2w")
# creates list movies
movies = [it, amadeus, lebowski, incredibles, apocalypse, fight_club]
# calls method from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
