import time, os, sys, pprint

os.system("clear")

print("Welcome To The Movie Tracker!")

entries = int(input("How many movies do you want to enter? : "))

movieList = []

for i in range(entries):
    print()
    title = input(f"Enter movie {i + 1} title : ")
    genre = input(f"Enter the genre : ")
    rating = float(input(f"Enter your rating out of 10 : "))

    movie = {"Title" : title,
             "Genre" : genre,
             "Rating" : rating
             }
    
    movieList.append(movie)


os.system("clear")
print()
print("Your Movie List")
print("-"*60)
print()

for i in movieList:
    print(f"{i["Title"]:<20} {i["Genre"]:<20} - {i["Rating"]:>10}/10")

print()
print()
time.sleep(5)
sys.exit()