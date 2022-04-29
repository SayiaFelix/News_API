# from flask import render_template,request,redirect,url_for
# from .main import main
# from .requests import get_news,get_movie,search_news
# from .main.forms import ReviewForm
# from .news_source import News

# # Views
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#      # Getting popular movie
#     popular_movies = get_news('popular')
#     print(popular_movies)
#     title ='Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title,popular = popular_movies)



#     # # Getting News Source
#     # popular_movies = get_news('popular')
#     # upcoming_movie = get_news('upcoming')
#     # now_showing_movie = get_news('now_playing')

#     # title = 'Home - Welcome to The World News HUB'

#     # search_news = request.args.get('movie_query')

#     # if search_news:
#     #     return redirect(url_for('.search',new_name=search_news))
#     # else:
#     #     return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )

from flask import render_template
from app import app


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The Best Online News Hub'
    return render_template('index.html', title=title)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',id = news_id,title = title)