def get_words_from_file(filename):
    with open(filename) as file:
        text = file.read()

    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()

    words = text.split(" ")
    words.sort()
    return words

def get_unique_words(words):
    unique_words = []
    unique_words.append(words[0])

    for i in range(1, len(words)):
        if(words[i] == words[i - 1]):
            continue
        else:
            unique_words.append(words[i])
    return unique_words

def main():
    filename = "address.txt"
    print("The Word Counter Program\n")
    words = get_words_from_file(filename)
    unique_words = get_unique_words(words)

    print("Number of words =", len(words))
    print("Number of uniquen words =", len(unique_words))

    print("Unique word occurences: ")
    for word in unique_words:
        print(" ", word, "=", words.count(word))

if __name__ == "__main__":
    main()
