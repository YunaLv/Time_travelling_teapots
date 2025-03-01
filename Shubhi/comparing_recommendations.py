import random
liked_movies = {
    "Aisha": {"Everything Everywhere All at Once", "Dune", "Spider-Man: Across the Spider-Verse", "The Matrix", "Black Panther"},
    "Carlos": {"The Dark Knight", "Interstellar", "Inception", "Dune", "John Wick"},
    "Mia": {"Barbie", "La La Land", "Pride & Prejudice", "Spider-Man: Across the Spider-Verse", "Everything Everywhere All at Once"},
    "Jin": {"Parasite", "Dune", "Everything Everywhere All at Once", "Inception", "Train to Busan"},
    "Liam": {"The Lord of the Rings: The Fellowship of the Ring", "Star Wars: The Empire Strikes Back", "The Matrix", "Interstellar", "John Wick"},
}

user_likes = set()
movie = input ("Enter a movie you like (or press Enter to finish): ")
while movie != "":
    user_likes.add(movie)
    movie = input ("Enter a movie you like (or press Enter to finish): ")
else:
    user_likes_join = ", ".join(user_likes)
    print (f"Movies liked by user: {user_likes_join}")
best_match = None
highest_jaccard = 0

names = list(liked_movies.keys())
for name in names:
    both = []
    for movie in liked_movies[name]:
        for movie2 in user_likes:
            if movie2 == movie:
                both.append(movie)
    both_join = ", ".join(both)

    either = set()
    for movie in liked_movies[name]:
        either.add(movie)
    for movie2 in user_likes:
        either.add(movie2)  
    either_join =  ", ".join(either)
    jaccard = len(both)/len(either)
    if jaccard !=1:
        if jaccard > highest_jaccard:
            highest_jaccard = jaccard
            best_match = name
            #not the best method, reevaluate
            for item in either:
                if item not in both:
                    if item not in user_likes:
                        movie_recco = item
print (f" Best match: {best_match} (Jaccard score: {highest_jaccard})")
print (f"Reccomended Movie: {movie_recco}")

