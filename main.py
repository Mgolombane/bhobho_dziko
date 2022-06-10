# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# assigning strings
x = "hello world"
y = "bho bho dziko"

#printing strings

print("english:", x)

print("chichewa:", y)

#importing necessary strings
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.972]

#ploting and printing
plt.plot(year, pop)

print(plt.plot(year, pop))

plt.show()

#help(plt) _ cancelled, the help call for the plt module

#plt.scatter(gdp, life_exp, s =pop)

import numpy as np

#np.vint16(127).bit_count()


from typing import Any

np.signedinteger[Any]

def add(x, y):
    return x+y

print(add(2,3))

def add(*args):
    print(args, type(args))

add(2, 3)

def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))

def total_fruits(**kwargs):
    print(kwargs, type(kwargs))

total_fruits(banana=5, mango=7, apple=8)

def total_fruits(**fruits):
    print(fruits, type(fruits))
    total = 0
    for amount in fruits.values():
        total += amount
    return total

print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))


y = [1, 2, 3, 4, 5, 6]

print(y)

import numpy as np

z = np.array(y)

print(z)

print(type(y))

print(type(z))

m = np.array([[1, 5, 2],
              [4, 7, 4],
              [2, 0, 9]])

print(m)

print(type(m))

print(m.shape)
#matrix transpose
print('Matrix transpose:', m.transpose(), '/n')

#matrix determinant
print('Matrix Determinant:', np.linalg.det(m), '/n')

#matrix inverse
m_inv = np.linalg.inv(m)
print('Matrix inverse:\n', m_inv, '\n')

#idendity matrix (result of matrix x matrix_inverse)

iden_m = np.dot(m, m_inv)

iden_m = np.round(np.abs(iden_m), 0)

print('Product of matrix and its inverse:\n', iden_m)

#eigendecomposition
n = np.array([[1, 5, 2],
             [4, 7, 4],
             [2, 0, 9]])

eigen_vals, eigen_vecs = np.linalg.eig(n)

print('Eigen Values:', eigen_vals, '\n')

print('Eigen Vectors:\n', eigen_vecs)

# SVD
m = np.array([[1, 5, 2],
             [4, 7, 4],
             [2, 0, 9]])

U, S, VT = np.linalg.svd(m)

print('Getting SVD outputs:-\n')

print('U:\n', U,'\n')
print('S:\n', S, '\n')
print('VT:\n', VT, '\n')

#descriptive statistics
import scipy as sp

import scipy.cluster as spc

#get data
nums = np.random.randint(1,20, size=(1,15))[0]
print('Data:', nums)
help(sp)
#det descriptive stats
print('Mean:', sp.mean(nums))
print('Median:', sp.median(nums))
#print('Mode:', spc.stats.mode(nums))
print('Standard Deviation:', sp.std(nums))
print('Variance:', sp.var(nums))
#print('Skew:', spc.stats.skew(nums))
#print('Kurtosis:', spc.stats.kurtosis(nums))



