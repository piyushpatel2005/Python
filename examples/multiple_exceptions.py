import sys

filename = input('Enter filename: ')
movies = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
except FileNotFoundError as e:
    print("FileNotFoundError", e)
    sys.exit()
except OSError as e:
    print("OSError:", e)
except Execption as e:
    print(type(e), e)
    sys.exit()
