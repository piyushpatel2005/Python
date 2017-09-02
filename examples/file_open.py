with open("test.txt", "w") as outfile:
    sample_text = input("Write to file: ")
    outfile.write(sample_text)

with open("test.txt", "r") as infile:
    print("test.txt file content:")
    print()
    print(infile.readline())
