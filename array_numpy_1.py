import numpy as np
from numpy import *

print(any([0,7,0]))
arr7 = np.array([1,2,0])
print(all(arr7))
arr8 = np.array([1,2,30])
arrRes = arr7 == arr8
print(arrRes)
array1 = np.array([45,34,23,21,90,55,78])
print(array1)
newArr = array1 + 6
print(newArr)

array2 = np.array([1,2,3,4,5,6,65],"int")
print(array2)

array3 = np.array([56,89,34,51,49],"float")
for i in array3:print(i)

arr4 = np.array(["Sushant","Pallavi","Vrushali","Shweta","Nikita"])
for eachName in arr4:print(eachName)

array1 = append(array1,99)

array2 = insert(array2,3,44)
print(array2)

array3 = delete(array3,0)
print(array3)

arrayAddition = add(array1,array2)
print(arrayAddition)

arrayDivide = divide(array1,array2)
print(arrayDivide)

arrayMultiplication = multiply(array1,array2)
print(arrayMultiplication)

arraySubtraction = subtract(array1,array2)
print(arraySubtraction)

print(shape(array1))   #imp - length in terms of an array but shape gives dimensions for vectors, matrices, tensors etc.


array5 = linspace(1,10,4)
print(array5)

arr1 = zeros(5,"int")
print(arr1)

arr2 = ones(5,"float")
print(arr2)