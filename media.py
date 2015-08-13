import webbrowser

class Movie():
    """ This class provides a way to store moview related information """
        
# Here I'll define what parameters will Movie need to work
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
# Here we'll use webbrowser to be able to show the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
