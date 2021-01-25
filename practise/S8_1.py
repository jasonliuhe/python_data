import matplotlib.pyplot as plt
import numpy as np

# part 1

x = np.linspace(0, 5, 11)
y = x ** 2

# print(x)
# print(y)

# plt.plot(x, y)
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')

# plt.subplot(1, 2, 1) # row, column
# plt.plot(x, y, 'r--')
# plt.subplot(1, 2, 2)
# plt.plot(y, x, 'g*-')

# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Set Title')

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
#
# axes1.plot(x, y)
# axes1.set_title('Larger Plot')
# axes2.plot(y, x)
# axes2.set_title('SMALLER PLOT')

# part 2

# fig, axes = plt.subplots()
# axes.plot(x, y, 'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')


# fig, axes = plt.subplots(nrows=1, ncols=2)
# axes[0].plot(x, y)
# axes[0].set_title('First Plot')
# axes[1].plot(y, x)
# axes[1].set_title('Second Plot')
# plt.tight_layout()

# fig = plt.figure(figsize=(8, 4), dpi=100)
# fig, axes = plt.subplots(figsize=(12,3))
# axes.plot(x, y, 'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')

# fig = plt.figure()
#
# ax = fig.add_axes([0,0,1,1])
#
# ax.plot(x, x**2, label="x**2")
# ax.plot(x, x**3, label="x**3")
# ax.legend(loc=0)

# part 3
# MATLAB style line color and style
fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-') # blue line with dots
ax.plot(x, x**3, 'g--') # green dashed line

plt.tight_layout()
plt.show()

quit()
