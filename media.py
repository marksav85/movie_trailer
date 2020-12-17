import webbrowser
import fresh_tomatoes

class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


import media

spongebob = media.Movie("The SpongeBob Movie: Sponge on the Run", "Spongebob and Patrick are on the run", "https://upload.wikimedia.org/wikipedia/en/3/38/The_SpongeBob_Movie_Sponge_on_the_Run.jpg", "https://www.youtube.com/watch?v=HfiH_526qhY&ab_channel=ParamountPictures")

print(spongebob.storyline)

spongebob.show_trailer()

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy","A group of misfits band together to defend the galaxy","https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg","https://www.youtube.com/watch?v=d96cjJhvlMA&ab_channel=MarvelEntertainment")

print(guardians_of_the_galaxy.storyline)

guardians_of_the_galaxy.show_trailer()

dredd = media.Movie("Dredd","A lone enforcer takes on a drug gang in a dystopian future","https://upload.wikimedia.org/wikipedia/en/1/16/Dredd2012Poster.jpg","https://www.youtube.com/watch?v=qVIba2N6MTA")

print(dredd.title, dredd.storyline)

dredd.show_trailer()

movies = [spongebob, guardians_of_the_galaxy, dredd]

fresh_tomatoes.open_movies_page(movies)


