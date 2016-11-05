
class Movie:
    """
    The movie object reads in the attributes of a movie to create a data
    structure for accessing these attributes of the movie.

    """

    def __init__(self, title, summary, poster, trailer_youtube_url):
        """
        Initializes the object with the following attributes:

        :param title: Title of the movie
        :param summary: a brief summary of the movie
        :param poster: a link to an image of the movie's poster
        :param trailer_youtube_url: a link to the movie's trail on youtube
        """
        self.title = title
        self.summary = summary
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube_url


