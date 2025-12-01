movies = {
    "Inception": [5, 4, 5, 5, 4],
    "Avatar": [3, 4, 4, 3],
    "Interstellar": [5, 5, 5, 4, 5],
    "Frozen": [4, 3, 4]
}

averages = {}

for title, ratings in movies.items():
    avg = sum(ratings) / len(ratings)
    averages[title] = avg

for title, avg in averages.items():
    print(f"{title} has an average of {avg}")

top_movie = max(averages, key=averages.get)
print(f"The top movie is {top_movie} with an average of {averages[top_movie]}")

highly_rated = []

for title in averages:
    avg = averages[title]
    if avg > 4.0:
        highly_rated.append(title)
print(f"Highly rated movies are : {highly_rated}")
