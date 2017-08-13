import webbrowser

class Video():
    """ This is the class that will hold the video information. It will also contain the code the play the video"""

    def __init__(self, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
