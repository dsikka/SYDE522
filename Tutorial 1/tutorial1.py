from collections import defaultdict
import pandas as pd
import numpy as np

a = 1
b = 'abc'
c, d = 1., 2**1000
n = None
m = True
type(a), type(b), type(c), type(d), type(n), type(m)

# int type can hold bigint numbers as well
val = 2**1000
print(val)

# Other important types
# Set non repetitive, will automatically remove repeated values
type([1, 2, 3]), \
type({'a': 1}), \
type({1, 2, 3}), \
type( ([1, 2], 2, "3", 3.14) )

d = defaultdict(type(None))
d['a'] = 1
if d['b'] is None:
	print("True")

# iteration
for i in range(10):
    print(i)

# enumerate
a = [2, 3, 4]
for idx, el in enumerate(a):
    print((idx, el))

list(enumerate('abcdefg', 0))
list(enumerate('abcdefg', 2))

# zip
# Can iterate over multiple by using zips
a = [1, 2, 3]
b = [4, 5, 6]

for a, b in zip(a, b):
    print((a, b))

# list comprehensions
[2*a for a in range(10)]

# set comprehensions
{2*a for a in range(10)}

{1 for a in range(10)}

# dict comprehensions

{i: a for i, a in enumerate('abc') }


###
# define arrays
np.array([[1, 2, 3], [4, 5, 6]])

# matrix multiply
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[1], [2], [3]])

print(arr.shape, arr2.shape)
# matrix multiplication/dot product
np.dot(arr, arr2)

# np.linalg for linear algebra functions
np.linalg.inv([[1, 2], [3, 4]])

# find normal
np.linalg.norm([1, 2, 3])

# find normal
np.linalg.norm([1, 2, 3])

def eucledean_distance(a, b):
    return np.linalg.norm(a - b, axis=1)

eucledean_distance(np.random.rand(10, 2), np.random.rand(10, 2))

data = pd.read_csv('./adult.csv')
data.is_high_income = (data.income == '>59k')*1.
data.is_high_income.mean()
data.education.unique()