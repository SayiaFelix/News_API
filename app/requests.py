
import urllib.request,json
from .news import Source
# from .sources import Sources

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
       
        # language = source_item.get('language')
        if name:    
            source_object = Source(name,description,url,category,)
            source_results.append(source_object)
    return source_results




# News
# def get_everything(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_news_url = base_url.format(category,apiKey)

#     with urllib.request.urlopen(get_news_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)

#         new_results = None

#         if get_news_response['sources']:
#             new_results_list = get_news_response['sources']
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
#         urlToImage = new_item.get('urlToImage')
#         content = new_item.get('content')
#         publishedAt = new_item.get('publishedAt')
               
#         new_object = News(title,description,urlToImage,content,publishedAt)
#         new_results.append(new_object)
           

#     return new_results







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