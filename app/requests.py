
from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
apiKey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(sources,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['results']:
            new_results_list = get_news_response['results']
            new_results = process_results(new_results_list)


    return new_results

def process_results(new_list):
    '''
    Function  that processes the new result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain new details

    Returns :
        news_results: A list of news objects
    '''
    new_results = []
  
    for new_item in new_list:
        id = new_item.get('id')
        name = new_item.get('name')
        description = new_item.get('description')
        url = new_item.get('url')
        country = new_item.get('country')
        poster = new_item.get('poster_path')
               
        if poster:
             new_object = News(id,name,description,url,country)
             new_results.append(new_object)
           

    return new_results