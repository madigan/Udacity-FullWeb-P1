# Demos the use of the Movie data structure
# Author: John Lynn

import fresh_tomatoes
from movie import Movie

# Create movie list
movies = []
movies.append(Movie("Star Wars: Episode I", "http://skywalkingthroughneverland.com/wp-content/uploads/2014/05/star-wars-episode-1-poster.jpg", "https://www.youtube.com/watch?v=bD7bpG-zDJQ"))
movies.append(Movie("Star Wars: Episode II", "http://brushfirecreative.com/wp-content/uploads/2015/05/sw2.jpg", "https://www.youtube.com/watch?v=gYbW1F_c9eM"))
movies.append(Movie("Star Wars: Episode III", "http://cdn.buzznet.com/assets/users7/macpro/default/star-wars-episode-iii-poster--large-msg-1115006319-2.jpg", "https://www.youtube.com/watch?v=5UnjrG_N8hU"))
movies.append(Movie("Star Wars: Episode IV", "http://simonz.web.elte.hu/poster/classic-poster1-movie.jpg", "https://www.youtube.com/watch?v=xioILbwDlEg"))
movies.append(Movie("Star Wars: Episode V", "http://i.newsarama.com/images/i/000/138/527/original/star-wars-empire-strikes-back-poster.jpg?1415977989", "https://www.youtube.com/watch?v=JNwNXF9Y6kY"))
movies.append(Movie("Star Wars: Episode VI", "http://img1.wikia.nocookie.net/__cb20050925102019/starwars/images/4/44/Return_of_the_jedi_old.jpg", "https://www.youtube.com/watch?v=CsDwpF3uiZI"))
movies.append(Movie("Star Wars: Episode VII", "http://www.moviecricket.com/wp-content/uploads/2014/05/Star-Wars-Episode-VII-Fan-Made-Poster-Falcon.jpg", "https://www.youtube.com/watch?v=OMOVFvcNfvE"))

# Render movie list
fresh_tomatoes.open_movies_page(movies)
