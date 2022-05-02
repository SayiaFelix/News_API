
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import  get_sources,get_headlines,article_source


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
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    headline=get_headlines()

    title = 'Sir Felix News Hub'
    
    return render_template('index.html', title = title, general = general_sources, entertainment = entertainment_sources, technology = technology_sources,science = science_sources, health = health_sources, sports = sport_sources, business = business_sources,headlines=headline)

    
@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    articles = article_source(id)
    return render_template('news.html',articles = articles, id=id )





