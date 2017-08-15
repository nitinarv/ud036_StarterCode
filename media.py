import video


class Movie(video.Video):
    """Movie class contains the details of the movie.
    It will extend the Video class that is used to hold
    video information like Youtube video link """

    """Constructor for the movie class, <br/>
    accepts the following variables, <br/>
    @param: title is the title of the movie,<br/>
    @param: movie_storyline is the storyline of the movie, <br/>
    @param: poster_image_url is the url of the poster image of the movie<br/>
    @param: trailer_youtube_url is the url of the youtube trailer video"""
    def __init__(
        self,
        title,
        movie_storyline,
        poster_image_url,
        trailer_youtube_url
            ):
            video.Video.__init__(self, trailer_youtube_url)
            self.title = title
            self.movie_storyline = movie_storyline
            self.poster_image_url = poster_image_url
