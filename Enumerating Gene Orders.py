'''
itertools is a Python module that provides efficient tools for creating and working with iterators,
especially for looping, combinations, permutations, and infinite sequences.
'''

import itertools

# Read input
n = 5

# Generate list from 1 to n
nums = list(range(1, n+1))

# Get all permutations
perms = list(itertools.permutations(nums))

# Print the total number of permutations
print(len(perms))

# Print each permutation
for p in perms:
    print(' '.join(map(str, p)))
