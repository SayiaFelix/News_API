class Source:
    '''
    News class to define News Objects
    '''

    def __init__(self,name,description,url,category,country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

class TopHeadlines:
    '''
    Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,title,description,url,content,urlToImage,publishedAt):
        self.author = author
        self.description = description
        self.content = content
        self.url = url
        self.urlToImage = urlToImage
        self.title = title
        self.publishedAt = publishedAt