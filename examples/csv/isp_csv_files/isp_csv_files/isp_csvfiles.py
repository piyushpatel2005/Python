"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding ton the field names in
      the given CSV file.
    """
    with open(filename) as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=separator, quoting=0, quotechar=quote)
        for row in csv_reader:
            csv_table.append(row)
    # print(csv_table)
    return csv_table[0]

# read_csv_fieldnames("table1.csv", ',', '"')

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote,
                                   quoting=csv.QUOTE_MINIMAL)
        for row in csvreader:
            row_dict = dict()
            for key,value in row.items():
                row_dict[key] = value
            table.append(row_dict)
    # print(table)
    return table

    # return table, csvreader.fieldnames

# read_csv_as_list_dict('table1.csv', ',', '"')
# read_csv_as_list_dict('table4.csv', ',', '"') 


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """

    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote,
                                   quoting=csv.QUOTE_MINIMAL)
        for row in csvreader:
            row_dict = {}
            for key,value in row.items():
                row_dict[key] = value
            table[row[keyfield]] = row_dict
            # table[row[keyfield]] = {key: value} for key, value in row.items()
    # print(table)
    return table

# read_csv_as_nested_dict('table1.csv', 'Field1', ',', '"')

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, "wt", newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames,
                                   delimiter=separator,
                                   quotechar=quote,
                                   quoting=csv.QUOTE_NONNUMERIC)

        csvwriter.writeheader()
        for row in table:    
            csvwriter.writerow(row)

# write_csv_from_list_dict('output1.csv', 
# [
#   {'b': 11, 'e': 14, 'a': 10, 'c': 12, 'd': 13}, 
#   {'b': 21, 'e': 24, 'a': 20, 'c': 22, 'd': 23}, 
#   {'b': 31, 'e': 34, 'a': 30, 'c': 32, 'd': 33}, 
#   {'b': 41, 'e': 44, 'a': 40, 'c': 42, 'd': 43}
# ], ['a', 'b', 'c', 'd', 'e'], ',', '"')
