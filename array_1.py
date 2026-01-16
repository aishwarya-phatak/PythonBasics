#import array
import array as a

numbers = a.array('i',[23,12,67,89,54])
print(numbers)
print(numbers[0])
print(numbers[1])

for eachNumber in numbers:print(eachNumber)

for eachNumber in numbers:
    print(eachNumber * 10)

lengthOfArray = len(numbers)
print("lengthOfArray is {}".format(lengthOfArray))

#range usage in for loop, len used to get length of array
for position in range(len(numbers)):
    print(numbers[position])
