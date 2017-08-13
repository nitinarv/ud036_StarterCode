import video
class Movie(video.Video):
    """Movie class contains the details of the movie. It will extend the Video class that is used to hold video information like Youtube video link """

    def __init__(self, title, movie_storyline, poster_image_url, trailer_youtube_url):
        video.Video.__init__(self, trailer_youtube_url)
        self.title = title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url

        
    