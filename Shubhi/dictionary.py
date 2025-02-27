liked_movies = {
    "Aisha": {"Everything Everywhere All at Once", "Dune", "Spider-Man: Across the Spider-Verse", "The Matrix", "Black Panther"},
    "Carlos": {"The Dark Knight", "Interstellar", "Inception", "Dune", "John Wick"},
    "Mia": {"Barbie", "La La Land", "Pride & Prejudice", "Spider-Man: Across the Spider-Verse", "Everything Everywhere All at Once"},
    "Jin": {"Parasite", "Dune", "Everything Everywhere All at Once", "Inception", "Train to Busan"},
    "Liam": {"The Lord of the Rings: The Fellowship of the Ring", "Star Wars: The Empire Strikes Back", "The Matrix", "Interstellar", "John Wick"},
}

names_options = ", ".join(list(liked_movies.keys()))
print (f"Available people: {names_options}")
name = input("Enter a name: ")
movie_list = ", ".join(liked_movies[name])
print (f"Movies liked by {name}: {movie_list}")
name2 = input("Enter another name: ")
movie_list = ", ".join(liked_movies[name2])
print (f"Movies liked by {name2}: {movie_list}")

both = []
for movie in liked_movies[name]:
    for movie2 in liked_movies[name2]:
        if movie2 == movie:
            both.append(movie)
both_join = ", ".join(both)
print (f"Movies liked by both {name} or {name2}: {both}")

either = set()
for movie in liked_movies[name]:
    either.add(movie)
for movie2 in liked_movies[name2]:
    either.add(movie2)  
either_join =  ", ".join(either)
print (f"Movies liked by either {name} or {name2}: {either}")

print (len(either))
print (len(both))
jaccard = len(both)/len(either)
print (f"Jaccard similarity between {name} and {name2}: {jaccard}")


