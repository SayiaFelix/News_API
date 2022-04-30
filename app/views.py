

from flask import render_template
from app import app
from app.requests import get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
       # Getting popular movie
    source_news = get_news('source')
    # print(popular_movies) 
    title = 'Home - Welcome to The Best Online News Hub'
    return render_template('index.html', title = title, source = source_news)


   
  
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',id = news_id,title = title)