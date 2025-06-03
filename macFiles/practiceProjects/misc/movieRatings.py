import time, sys, os

os.system("clear")

movieList = []

for i in range(3):
    title = input("Please enter title : ")
    title = title.capitalize()
    rating = int(input("Please enter rating : "))

    movie = {"title": title, "rating": rating}

    movieList.append(movie)

for movie in movieList:
    print(f"{movie["title"]} {movie["rating"]}")
