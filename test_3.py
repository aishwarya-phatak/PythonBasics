# sets - mutable
s1 = {10, 20, 30, 40, 55}
s2 = {10, 22, 33, 40, 59}

s1.update([20, 40, 56])
print(s1)

s1.update(s2)
print(s1)
print(s2)
s1.add(12)
print(s1)

s1.remove(40)
print(s1)

result = s1.union(s2)
result2 = s1.difference(s2)
result3 = s1.intersection(s2)
print(result)
print(result2)
print(result3)

# frozenset
s3 = frozenset([11, 78, 94, 23, 54, 88])
print(s3)
s4 = {34, 89, 77, 21}
resU = s3.union(s4)
print(s3)
resI = s3.intersection(s4)
resD = s3.difference(s4)
print(resU)
print(resI)
print(resD)
