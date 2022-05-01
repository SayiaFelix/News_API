
import urllib.request,json
from .news import Source
# from .article import Everything

# Getting api key
apiKey = None

# Getting the news base url
base_url = None

def configure_request(app):
    global apiKey,base_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the sources for a given category
    '''
    get_sources_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results_sources(source_results_list)

        return source_results
    
def process_results_sources(source_list):
    source_results = []
    for source_item in source_list:
       
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if name:    
            source_object = Source(name,description,url,category,country)
            source_results.append(source_object)
    return source_results


# # Articles list
# def get_everything():
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_news_url = base_url.format(apiKey)

#     with urllib.request.urlopen(get_news_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)

#         new_results = None

#         if get_news_response['articles']:
#             new_results_list = get_news_response['articles']
#             new_results = process_results(new_results_list)


#     return new_results

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
#         url= new_item.get('url')
#         urlToImage = new_item.get('urlToImage')
#         content = new_item.get('content')
#         publishedAt = new_item.get('publishedAt')
               
#         new_object = Everything(title,description,url,urlToImage,content,publishedAt)
#         new_results.append(new_object)
           

#     return new_results

