
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_everything


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting news
    News = get_everything()

    title = 'Sir Felix News Hub'
    return render_template('index.html', title = title, article = News)
    # search_movie = request.args.get('movie_query')

    # if search_movie:
    #     return redirect(url_for('.search',movie_name=search_movie))
    # else:
    #     return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )


# @main.route('/Sources')
# def sources():

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     News= get_sources()
      
#     return render_template('news.html', Sources= News)


# # @main.route('/search/<movie_name>')
# # def search(movie_name):
# #     '''
# #     View function to display the search results
# #     '''
# #     movie_name_list = movie_name.split(" ")
# #     movie_name_format = "+".join(movie_name_list)
# #     searched_movies = search_movie(movie_name_format)
# #     title = f'search results for {movie_name}'
# #     return render_template('search.html',movies = searched_movies)
