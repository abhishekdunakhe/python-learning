import numpy as np

# one-dimensional array
a = np.array([1, 2, 3, 4, 5])
print(a) # [1 2 3 4 5]
print(a.shape) # (5,) this is no of col (col,)

# two-dimensional array
b = np.array([(1, 2, 3, 4, 5),(1, 2, 3, 4, 5)])
print(b)
print(b.shape) # (2,5) this is no of row, col (row, col)

c = np.array([(1, 2, 3, 4, 5),(1, 2, 3, 4, 5)], dtype=float)
print(c)


# create numpy array of Zeros
x = np.zeros((2,3))
print(x)

y = np.ones((4,5))
print(y)

z = np.full((3,4),"A")
print(z)

p = np.eye(5)
print(p)

# create numpy array with random values.
q = np.random.random((3,4))
print(q)

# r = np.random.randint(1,50,(3,4))
r = np.random.randint(1,10,(3,4))
print(r)

s = np.linspace(10, 20, 6)
print(s) # this gives value 6 values with upto 20

t = np.arange(10, 40, 6)
print(t) # this gives value with 6 steps

list1 = [10, 20, 30, 40, 50]
np_array = np.asarray(list1) # also we can use array instead of asarray
print(np_array)
print(type(np_array))

u = np.random.randint(10,90,(4,4))
print(u) # it gives value between 10 to 90 in 4 by 4 matrix
print(u.shape) # it gives (row,col)
print(u.size) # it gives how many numbers in matrix
print(u.ndim) # it gives dimensions
print(u.dtype) # it gives int32 means integer with 32 bits

list3 = [1,2,3,4]
list4 = [4,5,6,7,8]
print(list3 + list4) # this concate two list

v = np.random.randint(10,20,(4,4))
w = np.random.randint(30,40,(4,4))
print(v)
print(w)
print(v+w)
print(np.add(v,w))
print(v-w)
print(np.subtract(v,w))
print(v*w)
print(np.multiply(v,w))
print(v/w)
print(np.divide(v,w))


# transpose the matrix
array4 = np.random.randint(10,30,(3,2))
print(array4)
# trans = np.transpose(array4)  # these are two methods of transpose the array.
trans = array4.T  # transpose row into col and col into row.
print(trans)
print(trans.shape)

array5 = array4.reshape(2,3) # by reshape we can change the shape of array.
print(array5)
print(array5.shape)