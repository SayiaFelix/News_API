class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,overview,poster,time):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_count = time

