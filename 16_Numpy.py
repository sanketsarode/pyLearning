import numpy as np  # as defined package as alias to avoid the large naming system

arr = [1, 2, 3]
print(arr, type(arr))

a = np.array([1, 2, 3])  # single dimension numpy array
print(a, type(a))

b = np.array([[1, 2], [3, 4]])  # 2 dimensional array
print(b)

c = np.array([[1, 2, 3], [4, 5]])  # single dimension array containing list
print(c)

d = np.arange(0, 100)   # 0 included 100 not included
print(d)

e = np.zeros((5, 6))  # creates array of zeros with 5 rows and 5 columns
print(e)

e = np.zeros(8)  # 1 D array of 8 in lenght
print(e)

f = np.linspace(0, 20, 10)  # creates a linearly spaced vector with spacing
print(f)

g = np.asarray(arr)  # converts an existing list into an array
print(g)

# reshapes an existing array to the specified dimensions
h = e.reshape((2, 2, 2))
print(h)

h = e.reshape((4, 2))
print(h)

i = h.ravel()  # converts into single dimension array
print(i)

ele = d[5]
print(ele)

ele = d[5] + 1
print(ele)
print(ele + 1)
print(type(ele))
print(type(ele + 1))
print(type(8))
print(type(8+1))

j = np.arange(20)
arr = slice(1, 10, 2)
print(j)
print(j[arr])
print(arr)

print(j[2:9])
print(j[1:10:2])
print(j[2:])
print(j[:7])

k = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(k[0:2, 0:2])
print(k[1:2, 1:2])
# before colon include the index but after colon its upto.
# ex: from 1st row upto 2nd row but not 2nd row. and from 1st column to 2nd column but not 2nd column
print(k[1:, :1])

# attributes of array:

print(k.shape)
print(k.ndim)
print(k.itemsize)

# empty array:

l = np.empty([2, 3], dtype=int)
print(l)

# Save and Read From File

print(np.savetxt('numpy.txt', k))
print(np.loadtxt('numpy.txt'))

k = [1, 2, 3]
print(np.savetxt('numpy.txt', k))
print(np.loadtxt('numpy.txt'))

k = (1, 2, 3)
print(np.savetxt('numpy.txt', k))
print(np.loadtxt('numpy.txt'))

k = np.array([[1, 2, 3], [4, 5, 6]])
print(np.savetxt('numpy.csv', k, delimiter=','))
print(np.genfromtxt('numpy.csv', delimiter=','))