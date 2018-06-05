"""class for ecapsulat movie detailes and open movie in webbrowser."""
# Maintained by Amr Ismail.
import webbrowser


class Movie(object):
    """class for ecapsulat movie detailes contains movie title ,movie storyline ,
    movie trailer url ,movie posterimage url."""

    # instance variable intialization
    def __init__(self, title, storyline, trailer, posterimage):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer
        self.poster_image_url = posterimage

    # function to open the movie trailer on webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailerurl)
