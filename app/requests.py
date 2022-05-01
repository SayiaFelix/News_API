
from unicodedata import name
import urllib.request,json
from .news import Source
from .article import Article

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


def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(apiKey)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)

    return get_headlines_results   
     
def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,apiKey)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        title = article.get ('title')
        url = article.get('url')
        content = article.get('content')
        description = article.get('description')
        publishedAt = article.get('publishedAt')
        urlToImage = article.get('urlToImage')
       
        if url:
            article_objects = Article(content,description,publishedAt,urlToImage,url,title)
            article_source_results.append(article_objects)

    return article_source_results