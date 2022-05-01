class Source:
    '''
    News class to define News Objects
    '''

    def __init__(self,name,description,url,category,country):
        self.name = name
        self.description = description
        self.url = url
        self.content = category
        self.country = country

