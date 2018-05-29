"""class for ecapsulat movie detailes and open movie in webbrowser."""
# Maintained by Amr Ismail.
import webbrowser

class Movie(object):
    """class for ecapsulat movie detailes contains movie title ,movie storyline ,movie trailer url ,movie posterimage url."""

    #instance variable intialization
    def __init__(self,movie_title,movie_storyline,movie_trailer, movie_posterimage):
        self.title=movie_title
        self.storyline=movie_storyline
        self.trailer_youtube_url=movie_trailer
        self.poster_image_url=movie_posterimage

    #function to open the movie trailer on webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailerurl)
