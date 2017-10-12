import webbrowser


class Movie ():
    """class to store my favorite movie
       4 attributes:
       movie_title - string; movie title
       movie_storyline - string; short description of movie story;
       poster_image - string, URL to poster gif
       trailer_youtube - string; URL to trailer on youtube.com site"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Inits Movie with 4 attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens trailer in youtube.com in browser window"""
    webbrowser.open(self.trailer_youtube_url)
