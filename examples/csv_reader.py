import csv
movies = [["Titanic", 1997], ["Pearl Harbor", 2003], ["X-Men", 2002]]
with open("movies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(movies)

with open("movies.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0] + "(" + str(row[1]) + ")") # Titanic(1997)
        print(row)  # ['Titanic', 1997]
