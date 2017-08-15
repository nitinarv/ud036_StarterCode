import webbrowser


class Video():
    """ This is the class that will
    hold the video information. It will also
    contain the code the play the video"""

    """Constructor for class Video. Accepts <br/>" +
    "@param: trailer_youtube_url which is the url of the youtube vide"""
    def __init__(self, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url

    """Universal method for showing trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
