
from flask import render_template,request,redirect,url_for
from . import main

from ..requests import  get_sources


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting news
    general_sources = get_sources('general')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')
    sport_sources = get_sources('sports')
    business_sources = get_sources('business')
    
    


    title = 'Sir Felix News Hub'
    
    return render_template('index.html', title = title, general = general_sources, entertainment = entertainment_sources, technology = technology_sources, sports = sport_sources, business = business_sources)

    
# @main.route('/Article')
# def news():

#     '''
#     View movie page function that returns the article details page and its data
#     '''
#     News = get_everything()
      
#     return render_template('news.html', Articles = News)


