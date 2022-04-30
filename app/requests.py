
import urllib.request,json
from .news import News
# from .sources import Sources

# Getting api key
apiKey = None

# Getting the news base url
base_url = None

def configure_request(app):
    global apiKey,base_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

# News
def get_everything():

    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['articles']:
            new_results_list = get_news_response['articles']
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
        title= new_item.get('title')
        description = new_item.get('description')
        urlToImage = new_item.get('urlToImage')
        content = new_item.get('content')
        publishedAt = new_item.get('publishedAt')
               
        new_object = News(title,description,urlToImage,content,publishedAt)
        new_results.append(new_object)
           

    return new_results

#sources
# def get_sources():
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_source_url = base_url.format(apiKey)

#     with urllib.request.urlopen(get_source_url) as url:
#         get_source_data = url.read()
#         get_source_response = json.loads(get_source_data)

#         source_object = None

#         if get_source_response:
#             name = get_source_response.get('name')
#             description = get_source_response.get('description')
#             url = get_source_response.get('url')
         
#             movie_object = Sources(name,description,url)

#     return source_object
         
# def process_results(new_list):
#     '''
#     Function  that processes the new result and transform them to a list of Objects

#     Args:
#         news_list: A list of dictionaries that contain new details

#     Returns :
#         news_results: A list of news objects
#     '''
#     new_results = []
  
#     for new_item in new_list: 
#         title= new_item.get('title')
#         description = new_item.get('description')
#         urlToImage = new_item.get('urlToImage')
#         content = new_item.get('content')
#         publishedAt = new_item.get('publishedAt')
               
#         new_object = News(title,description,urlToImage,content,publishedAt)
#         new_results.append(new_object)
           

#     return new_results