# sequences -- list datatype --mutable
list1 = [12, 34, 78, 45, 894]  # homogenous list
print(type(list1))
list1.sort()
print(list1)
list1.append(34)
list1.remove(12)
list1.append(77)
print(list1)
list1.reverse()
print(list1)

arr = [34, 98, 56, 12, 99]
list2 = list(arr)
print(type(list2))
print(type(arr))

list3 = [10, 20, "Bitcode", 34.23]  # heterogenous list
for eachVal in list3:
    print(eachVal, type(eachVal))

# bytearray  -- mutable
byteArray1 = bytearray()
byteArray1.append(34)

list5 = [34, 23, 12, 89, 13]
byteArr1 = bytearray(list5)
byteArr1[3] = 79
byteArr1.insert(0, 55)
byteArr1.append(90)
byteArr1.remove(34)
print(byteArr1)
print(type(byteArr1))
for i in byteArr1:
    print(i)

# tuples -- immutable
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("Bitcode", "Python", 42, 89.123, 10 + 10j)
print(tuple2)
list6 = [34, 2, 1289, 12]
tuple(list6)

# range -- immutable
print(list(range(5)))
print(list(range(6, 19)))
print(list(range(10, 30, 5)))
