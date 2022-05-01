
from unicodedata import name
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
            source_object = Source(name,description,url,country,category)
            source_results.append(source_object)
    return source_results


