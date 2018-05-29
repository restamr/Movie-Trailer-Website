"""interfaces for creating list of movies and genrate Html Page to display the list of movies ."""
# Maintained by Amr Ismail.

import media
import fresh_tomatoes

#create Captain Marvel Movie Object
MARVEL =media.Movie("CAPTAIN MARVEL",
                          "Captain Marvel is a 2019 superhero film based on the Marvel Comics superheroine Carol Danvers/Captain Marvel.",
                          "https://www.youtube.com/watch?v=lokJkv32EUA",
                          "https://ia.media-imdb.com/images/M/MV5BMTQ3MjIyMDQxOF5BMl5BanBnXkFtZTgwNDIxNTM2OTE@._V1_.jpg")

#create FRIENDS Movie Object
FRIENDS=media.Movie("FRIENDS",
                          "Friends The Movie is both, a continuation and finale to the hit TV series Friends.",
                          "https://www.youtube.com/watch?v=Gpa5S8DgPzs",
                          "https://i.ytimg.com/vi/Gpa5S8DgPzs/hqdefault.jpg")

#create Avengers Movie Object
Avengers=media.Movie("Avengers: Infinity War",
                          "The Avengers will have to team up with the Guardians of the Galaxy to have any hope of taking down Thanos and his Black Order.",
                          "https://www.youtube.com/watch?v=4ZxDEPJGgDg",
                          "https://i.ytimg.com/vi/6ZfuNTqbHE8/maxresdefault.jpg")

#create VENOM Movie Object
VENOM=media.Movie("VENOM",
                          "When Eddie Brock acquires the powers of a symbiote, he will have to release his alter-ego Venom to save his life.",
                          "https://www.youtube.com/watch?v=u9Mv98Gr5pY",
                          "https://ia.media-imdb.com/images/M/MV5BMTU3MTQyNjQwM15BMl5BanBnXkFtZTgwNDgxNDczNTM@._V1_SY1000_CR0,0,675,1000_AL_.jpg")

#create Annihilation Movie Object
Annihilation=media.Movie("Annihilation",
                          "When Eddie Brock acquires the powers of a symbiote, he will have to release his alter-ego Venom to save his life.",
                          "https://www.youtube.com/watch?v=u9Mv98Gr5pY",
                          "https://ia.media-imdb.com/images/M/MV5BMTk2Mjc2NzYxNl5BMl5BanBnXkFtZTgwMTA2OTA1NDM@._V1_SY1000_CR0,0,640,1000_AL_.jpg")

#create Skyscraper Movie Object
Skyscraper=media.Movie("Skyscraper",
                          "FBI Hostage Rescue Team leader and U.S. war veteran Will Sawyer, who now assesses security for skyscrapers.",
                          "https://www.youtube.com/watch?v=_pIEzZVqwFs",
                          "https://ia.media-imdb.com/images/M/MV5BOGM3MzQwYzItNDA1Ny00MzIyLTg5Y2QtYTAwMzNmMDU2ZDgxXkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_SY1000_SX632_AL_.jpg")

#creat list of movies
Movies=[MARVEL,FRIENDS,Avengers,VENOM,Annihilation,Skyscraper]

#use freshtomatoes class to generate html page with movie list
freshtomatoes=fresh_tomatoes.open_movies_page(Movies)
