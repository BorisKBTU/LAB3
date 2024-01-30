# Dictionary of movies
from random import randint

movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]
random_movie = randint(0, len(movies))
print(
    f'Movie with name "{movies[random_movie]["name"]}"{" do" if movies[random_movie]["imdb"] >= 5.5 else " do not"} have a rating above 5.5, its rating is {movies[random_movie]["imdb"]}')
print(
    f'List of movies which rating is more 5.5: {[i["name"] for i in list(filter(lambda x: x["imdb"] >= 5.5, movies))]}')
category = input('Input category ')
print(
    f'List of movies with category {category}: {[i["name"] for i in list(filter(lambda x: x["category"] == category, movies))]}')
print(f'Average imdb score: {sum([i["imdb"] for i in movies]) / len(movies)}')
category_ = input('Input category ')
print(print(
    f'Average imdb score with category {category_}: {sum([i["imdb"] for i in movies if i["category"] == category_]) / len([i["imdb"] for i in movies if i["category"] == category_])}'))
