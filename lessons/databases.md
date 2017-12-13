# Working with Databases

A relational database consists of tables. Tables consists of rows and columns, which can also be referred to as records and fields.

Tables in Database can have one to one, one to many or many to many relationship.Typically, relationship exists between the primary key in one table and foreign key in another table.

To work with SQLite database, we can use sqlite3 module.
To open a connection, you call `connect()` method from sqlite3 module to create connection object.

```python
import sqlite3
conn = sqlite3.connect("movies.sqlite")
```

For working with different OS, you can use following code:

```python
import sys
import os

if sys.platform == "win32":
  DB_FILE = "/python/_db/movies.sqlite"
else:
  HOME = os.environ["HOME"]
  DB_FILE = HOME + "/Documents/python/_db/movies.sqlite"
conn = sqlite3.connect(DB_FILE)
```

To execute SQL statement on a database, you need to get a cursor object for the database. You can use `cursor()` method. Then execute a SQL statement, you call the `execute()` method from the cursor object.

- `cursor()` : returns a cursor object that you can use to execute SQL statements.
- `execute(sql [params_tuple])` : execute SQL statement. You supply values for placeholders in tuple parameters.

```python
c = conn.cursor()
query = '''SELECT * FROM Movie'''
c.execute(query)
```

```python
query = '''SELECT * FROM Movie
           WHERE minutes < ?'''
c.execute(query, (90,))
```

**How to close cursor object automatically**

```python
from contextlib import closing
with closing(conn.cursor()) as c:
  query = '''SELECT * FROM Movie'''
  c.execute(query)
```

After executing a query, the cursor object contains a result set with the rows returned by the query. To access row or rows, you can use `fetchone()` or `fetchall()` methods of crusor.

- `fetchone()` : returns a tuple containing the next row from the result set. If there is no next row, it returns None
- `fetchall()` : returns a list containing all of the rows in the result set.

```python
with closing(conn.cursor()) as c:
  query = '''SELECT * FROM Movie WHERE movieID = ?'''
  c.execute(query, (5,))
  movie = c.fetchone()
print("Name:", movie[2])
print("Year:", str(movie[3]))
```

**How to access columns by name**

To acces them with name, you need to set `conn.row_factory` to `sqlite3.Row`.

```python
conn.row_factory = sqlite3.Row
print("Name:", movie['name'])
print("Year:", movie['year'])
```

To get all rows, you can use `fetchall`

```python
with closing(conn.cursor()) as c:
  query = '''SELECT * FROM Movie
              WHERE minutes < ?'''
  c.execute(query, (90,))
  movies = c.fetchall()

for movie in movies:
  print(movie['name'], "|", movie['year'], "|", movie['minutes'])
```

### Executing INSERT, UPDATE, DELETE

These operations don't return a result set. They modify data in the database.
To save changes after executing these queries, you use `commit()` method on connection object.

- `commit()` : commits the changes to the database.

**INSERT query**

```python
name = "Hero"
year = 2016
minutes = 96
categoryID = 2

with closing(conn.cursor()) as c:
  sql = '''INSERT INTO Movie (name, year, minutes, categoryID) VALUES (?, ?, ?, ?)'''
  c.execute(sql, (name, year, minutes, categoryID))
  conn.commit()
```

**UPDATE query**

```python
id = 4
minutes = 90

with closing(conn.cursor()) as c:
  sql = '''UPDATE Movie SET minutes = ? WHERE movieID = ?'''
  c.execute(sql, (minutes, id))
  conn.commit()
```

**DELETE query**

```python
id = 12

with closing(conn.cursor()) as c:
  sql = '''DELETE FROM Movie WHERE movieID = ?'''
  c.execute(query, (id,))
  conn.commit()
```

If the specified database is not found, the connect() method may raise `OperationalError`.

```python
import sqlite3
from contextlib import closing

conn = sqlite3.connect('movies.sqlite')
conn.row_factory = sqlite3.Row

# SELECT statement with exception handling
try:
  with closing(conn.cursor()) as c:
    query = '''SELECT * FROM Movie WHERE minutes < ?'''
    c.execute(query, (90,))
    movies = c.fetchall()
except sqlite3.OperationalError as e:
  print("Error reading database -", e)
  movies = None

if movies != None:
  for movie in movies:
    print(movie['name'] + "|" + movie['year'])
  print()

# INSERT statement
name = "The Day After Tomorrow"
year = 1988
minutes = 108
categoryID = 1
with closing(conn.cursor()) as c:
  sql = '''INSERT INTO Movie(name, year, minutes, categoryID) VALUES(?, ?, ?, ?)'''
  c.execute(sql, (name, year, minutes, categoryID))
  conn.commit()
print(name, "inserted")

# DELETE statement
with closing (conn.cursor()) as c:
  sql = '''DELETE FROM Movie WHERE name = ?'''
  c.execute(sql, (name, ))
  conn.commit()
print(name, "deleted")
