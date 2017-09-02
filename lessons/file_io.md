# File Input/Output in Python

There can be two types of files: text and binary files.
Files are persistent data storage.

File IO is a process of three steps:
1. Open a file in correct mode
2. Operate on file object
3. Close the file object to release resources of the system

## Working with Text Files

| Function | Description |
-----------|:-----------:|
|open(file, mode) | returns file object for specified file with given mode |
|close() | closes the file, frees all resources |

**Modes of open() function**

When opened in read mode, it will throw an exception if file doesn't exist. In write and append mode, if file doesn't exist, it will create one.

r - Read - open file for reading.
w - Write - write mode.
a - append - append mode.
b - binary - use this mode with 'r' or 'w'.

The default mode is 'r' with open() function.


```python
outfile = open("test.txt", "w")
outfile.write("Test")
outfile.close()
```

If during operation with file object, exception occurs, then the file resource is never released. This can cause problems. To avoid this open files with `with` statement as below. You don't need to close file object in this case, it will be closed automatically in any case.

```python
with open(file, mode) as file_object:
  statement...
```

```python
with open("test.txt", "w") as outfile:
  outfile.write("Test")
```

```python
with open("test.txt", "r") as infile:
  print(infile.readline())
```

[File Open example with text file](../examples/file_open.py)

When writing to a file, you can convert int and float to str using str() function as write() method takes string.

- file.write(str) : writes the specified string to the file.
- read() : reads the entire file and returns its contents as a string
- readlines(): reads the entire file and returns it as a list.
- readline() : reads the next line in the file and returns as a string.

```python
with open("members.txt") as file:
  for line in file:   # the loop automatically calls readline() function.
    print(line, end="")
  print()
```

```python
with open("members.txt") as file:
  contents = file.read()
  print(contents)
```

```python
with open("members.txt") as file:
  members = file.readlines()
  print(members[0], end="")
  print(members[1])
```

**Write items in a list to file**

```python
members = ["Piyush Patel", "Ishit Patel"]
with open("members.txt", "w") as file:
  for m in members:
    file.write(m + "\n")

years = [1975, 1978, 1981]
with open("years.txt", "w") as years_file:
  for year in years:
    years_file.write(str(year) + "\n")
```

**How to read lines in a file to a list**

```python
members = []
with open("members.txt", "r") as file:
  for line in file:
    line = line.replace("\n", "")
    members.append(line)
print(members)

years = []
with open("years.txt") as file:
  for line in file:
    line = line.replace("\n", "")
    years.append(int(line))
print(years)
```

### Working with CSV files

When working with CSV, you can use csv module and use its functions to work with csv files. CSV(comma separated values) files stores tabular data in text file separated by comma and each row ends with a new line character. Rows and columns can also be referred to as records and fields.

To write to a file, you can get writer object from csv using `csv.writer(file_object)` function. To open a csv file, you use open() function with extra third argument `newline=""`. This enables universal newlines mode, so it will read and write correctly for all operating systems.

- csv.writer(file) : returns a CSV writer object for the file. The writer object converts the data into comma-separated values.
- writer.writerows(rows) : writes all specified rows to the file specified by the writer object using the CSV format specified by the writer object.

```python
import csv
movies = [['Titanic', 1997], ['Pearl Harbor', 2003]]
with open("movies.csv", "w", newline="") as file:
  writer = csv.write(file)
  writer.writerows(movies)
```

CSV format causes problems when comma is used in one of the fields. For example, in address. To handle such issues CSV module provides optional arguments to change the CSV format.

- reader(file_object) : returns a CSV reader object for the file to get data from the CSV file.

```python
with open("movies.txt", newline="") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row[0] + " (" + str(row[1]) +")")
```

[CSV file reading writing example](../examples/csv_reader.py)

**Optional arguments for writer/reader function**

- quoting=csv.QUOTE_MINIMAL : specifies when quotes are written and read. It can be set to any of the QUOTE constants(default: QUOTE_MINIMAL)
- quotechar='"' : specifies the character that's used to quote columns.
- delimiter="," : specifies one-character string used to separate fields.(default: comma)

```python
writer = csv.writer(file, delimiter='\t')
reader = csv.reader(file, delimiter='\t')
```

[Movie List program using CSV](../example/movie_list_csv.py)

## Working with Binary Files

For working with binary files, use 'pickle' module. To work in binary mode, you need to add 'b' to mode argument in open() function.

Pickle module provides dump() to store object and load() to get objects. Storing is also called serializing or pickling an object and loading is also known as deserializing or unpickling

- dump (object, bfile) : writes the specified object to the binary file
- load (bfile) : reads an object from the specified binary file

```python
import pickle
movies = [['Star Wars',  2016], ['Running Cats', 2010]]
with open("movies.bin", "wb") as file:
  pickle.dump(movies, file)
with open("movies.bin", "rb") as file:
  movie_list = pickle.load(file)
  print(movie_list)
```

[Binary file reading writing example](../examples/binary_file.py)
