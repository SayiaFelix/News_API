import urllib.request,json
from .news_article import Movie
from .news_source import Movie


# Getting api key
api_key = None

# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['results']:
            movie_news_list = get_news_response['results']
            new_results = process_results(movie_news_list)


    return new_results

def process_results(new_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    new_results = []
    for new_item in new_list:
        id = new_item.get('id')
        title = new_item.get('original_title')
        overview = new_item.get('overview')
        poster = new_item.get('poster_path')
        vote_average = new_item.get('vote_average')
        vote_count = new_item.get('vote_count')

        if poster:
            new_object = Movie(id,title,overview,poster,vote_average,vote_count)
            new_results.append(new_object)

    return new_results