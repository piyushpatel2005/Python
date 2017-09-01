def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()


def list(movie_list):
    i = 1
    for movie in movie_list:
        print(str(i) + ". " + movie)
        i += 1
    print()

def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(movie + " was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(movie + " was deleted.\n")

def main():
    movie_list = ["Titanic", "Pearl Harbor", "Yeh Jawaani Hai Deewani"]
    display_menu()

    while True:
        command = input("Command: ")
        print(command.lower())
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print ("Bye!\n")

if __name__ == "__main__":
    main()
