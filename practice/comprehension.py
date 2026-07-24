# list comprehension 
numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print(squares)
# Output: [1, 4, 9, 16, 25]


scores = [45, 82, 94, 58, 71]

passing_scores = [s for s in scores if s >= 60]

print(passing_scores)
# Output: [82, 94, 71]


oxford_scores = [55, 72, 40, 90]

# Label each score as Pass or Fail
status = ["Pass" if s >= 60 else "Fail" for s in oxford_scores]

print(status)
# Output: ['Fail', 'Pass', 'Fail', 'Pass']



matrix = [[1, 2, 3], [4, 5, 6]]

# For each row in the matrix, take each item in that row
flat = [item for row in matrix for item in row]

print(flat)
# Output: [1, 2, 3, 4, 5, 6]






















# dict comprehension 
names = ["alice", "bob", "charlie"]

# Syntax: {key_expr: value_expr for item in iterable}
# Map each name to its character length
name_lengths = {name: len(name) for name in names}

print(name_lengths)
# Output: {'alice': 5, 'bob': 3, 'charlie': 7}