# sequences in python
# string
str1 = "Pallavi"
str2 = 'Python'

print(str1)
print(str1.find("i"))
print(str1.count("l"))
print(str2)
print(str1[0])
print(str1[3:6])
print(str1[1:])
print(str1[:4])
print(str1[-4: -1])

print(str1.upper())
print(str1.lower())
print(str1.split())
print(str1.split("a"))

print(str1.join(["Akolkar", "Vijay", "Abc"]))

arr1 = ["Python", "C", "Happy", "Learning"]
stringResult = "--".join(arr1)
print(stringResult)

print("--".join(arr1))

# ASCII -- A to Z -- 65 to 90
# ASCII -- a to z -- 97 to 122

# bytes ---> representation is using b prefix in an array of string
bArr = b"ABC"
for i in bArr:
    print(i)

numbers1 = [11, 12, 13, 14, 15]
bArr2 = bytes(numbers1)
for i in bArr2:
    print(i)

print(bArr2)

print(bArr2[0:2])
