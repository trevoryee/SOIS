#h07_movie.py

x= "yes"

file= open('h07_movies.txt',"a")

while x.casefold() == 'yes':
    movie= input("Favorite movie? ")
    directors= input("Name of director: ")
    why= input("Why do you like this movie? ")
    x= input("Would you like to let someone else respond? ")
    print(x)
    file.write("Movie: ")
    file.write(movie)
    file.write("\n")
    file.write("Directors: ")
    file.write(directors)
    file.write("\n")
    file.write("Why user liked it: ")
    file.write(why)
    file.write("\n")

file.close()