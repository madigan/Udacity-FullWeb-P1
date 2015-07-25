# Basic movie data structure
# Author: John Lynn


class Movie:
        """
        Basic movie data structure. Includes a title,
        a url for the movie poster, and a url to the trailer.
        """
        # Constructor
        def __init__(self, title, poster_image_url, trailer_youtube_url, rating):
                self.title = title
                self.poster_image_url = poster_image_url
                self.trailer_youtube_url = trailer_youtube_url
                self.rating = rating
