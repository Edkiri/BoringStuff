#! python3

tableData = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bob', 'Carol', 'David'],
  ['dogs', 'cats', 'moose', 'goose']
]

def printTable(tableData):
  """Print table assume that all the string have the same numbers of characters and justify-self to rigth."""
  colWidths = []
  for col in tableData:
    for string in col:
      print(string.rjust(get_longest_string(col)))



def get_longest_string(col):
  strings_len = []
  for string in col:
    strings_len.append(len(string))
  return max(strings_len)

printTable(tableData)