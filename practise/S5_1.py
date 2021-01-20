import numpy as np

my_list = [1, 2, 3]
print(my_list)

arr = np.array(my_list)
print(arr)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(my_mat))

print(np.arange(0, 10, 2))

print(np.zeros(3))

print(np.zeros((5, 5)))

print(np.ones(4))

print(np.linspace(0, 5, 10))

print(np.eye(4))

print(np.random.rand(5))

print(np.random.rand(5, 5))

print(np.random.randn(4, 4))

print(np.random.randint(1, 100, 10))

arr = np.arange(25)
print(arr)
ranarr = np.random.randint(0, 50, 10)
print(ranarr)
print(arr.reshape(5, 5))
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(arr.shape)
print(arr.reshape(5, 5).shape)
print(arr.dtype)
