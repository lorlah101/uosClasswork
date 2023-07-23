import random
import string

class Movie:
    def __init__(self):
        # Generate a random ID for the movie record
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        self.title = ''
        self.year = 0
        self.genre = ''
        self.release_date = ''

    def set_title(self, title):
        """Set the title of the movie record."""
        self.title = title

    def set_year(self, year):
        """Set the year of the movie record."""
        # Make sure the year is an integer
        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError('Year must be an integer')

    def set_genre(self, genre):
        """Set the genre of the movie record."""
        self.genre = genre

    def set_release_date(self, release_date):
        """Set the release date of the movie record."""
        self.release_date = release_date

    def get_title(self):
        """Get the title of the movie record."""
        return self.title

    def get_year(self):
        """Get the year of the movie record."""
        return self.year

    def get_genre(self):
        """Get the genre of the movie record."""
        return self.genre

    def get_release_date(self):
        """Get the release date of the movie record."""
        return self.release_date

class MovieList:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie):
        """Add a movie to the movie list."""
        # Make sure the movie is an instance of the Movie class
        if isinstance(movie, Movie):
            self.movies[movie.id] = movie
        else:
            raise ValueError('Movie must be an instance of the Movie class')

    def search(self, title=None, genre=None, release_date=None):
        """Search for movies in the movie list by title, genre, or release date."""
        # Initialize an empty list to store the search results
        results = []

        # Iterate through the movies in the movie list
        for id, movie in self.movies.items():
            # Check if the movie matches the search criteria
            if (title is None or movie.title == title) and (genre is None or movie.genre == genre) and (release_date is None or movie.release_date == release_date):
                results.append(movie)
            else: 
                print("Movie not found")
        return results

    def remove_movie(self, title):
        """Remove a movie from the movie list by title."""
        # Iterate through the movies in the movie list
        for id, movie in self.movies.items():
            # Check if the movie title matches the title to be removed
            if movie.title == title:
                # Remove the movie from the movie list
                self.movies.pop(id)
                break
            else:
                print(f"Movie with title '{title}' not found")

    def get_movie_count(self):
        """Get the total number of movies in the movie list."""
        return len(self.movies)

class Actor:
    # initialize a constructor to create the actor object
    def __init__(self, first_name, surname, gender, date_of_birth):
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
    
    def __str__(self):
        return f'First name: {self.first_name}\nSurname: {self.surname}\nGender: {self.gender}\nDate of Birth: {self.date_of_birth} '

    def set_first_name(self, first_name):
        """Set the first name of the actor."""
        self.first_name = first_name

    def set_surname(self, surname):
        """Set the surname of the actor."""
        self.surname = surname

    def set_gender(self, gender):
        """Set the gender of the actor."""
        self.gender = gender

    def set_date_of_birth(self, date_of_birth):
        """Set the date of birth of the actor."""
        self.date_of_birth = date_of_birth

    def get_first_name(self):
        """Get the first name of the actor."""

        return self.first_name

    def get_surname(self):
        """Get the surname of the actor."""
        return self.surname

    def get_gender(self):
        """Get the gender of the actor."""
        return self.gender

    def get_date_of_birth(self):
        """Get the date of birth of the actor."""
        return self.date_of_birth


class ActorsList:
    def __init__(self):
        self.actors = {}

    def add_actor(self, actor):
        """Add an actor to the actors list."""
        # Make sure the actor is an instance of the Actor class
        if isinstance(actor, Actor):
            self.actors[actor.first_name] = actor
        else:
            raise ValueError('Actor must be an instance of the actor class')

    def remove_actor(self, first_name):
        """Remove an actor from the actors list by first name."""
        if first_name in self.actors:
            # Remove the actor from the actors list
            self.actors.pop(first_name) 
            print(f"Actor {first_name} has been removed successfully")
        else:
            print(f"Actor {first_name} not in the list of actors")

    def get_actor_count(self):
        """Get the total number of actors in the actors list."""
        return len(self.actors)

    def get_actor_details(self, first_name):
        """Get the details of an actor by first name."""
        if first_name in self.actors:
            return self.actors[first_name]
        else:
            return None

