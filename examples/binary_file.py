import pickle
movies = [['Titanic', 1997], ['Vinnaithandi Varuvaayaa', 2012], ['Kem Chho', 2015]]
with open("movies.dat", "wb") as file:
    pickle.dump(movies, file)
with open("movies.dat", "rb") as file:
    movies_list = pickle.load(file)
    print(movies_list)
