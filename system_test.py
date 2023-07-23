# Import the Movie and MovieList class
from bi28qv_system_source_code import Movie, MovieList
# Import the Actor and ActorsList class
from bi28qv_system_source_code import Actor, ActorsList

# Create a new movie object
movie_007 = Movie()

movie_007.set_title('007')
movie_007.set_year(2020)
movie_007.set_genre('Action')
movie_007.set_release_date('2023-02-01')

# Create a new movie list object
actions = MovieList()
actions.add_movie(movie_007)

# Create a new actor object
james_bond = Actor('James', 'Bond', 'Male', '1920-01-01')

# Create a new actors list object
all_actors = ActorsList()
all_actors.add_actor(james_bond)

# Get the details of the movie object '007'
print(movie_007.get_title())  # Output: 007
print(movie_007.get_year())   # Output: 2020
print(movie_007.get_genre())  # Output: Action
print(movie_007.get_release_date())  # Output: 2023-02-01

# Get the number of objects in the actors list
print(all_actors.get_actor_count())  # Output: 1

# Get the details of the actor James Bond
print(all_actors.get_actor_details('James'))  # Output: actor object with details of James Bond

# Remove the details of the actor James Bond from the collection
all_actors.remove_actor('James')

