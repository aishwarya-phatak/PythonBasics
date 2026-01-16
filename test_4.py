# dictionary
from collections import OrderedDict

dict1 = (
    {
        1: "Sushant",
        2: "Nikita",
        3: "Vrushali",
        4: "Shweta",
        5: "Pallavi"
    }
)

print(dict1)

print(dict1[3])
print(dict1[2])

for key, val in dict1.items():
    print("key is : {} and value is : {}".format(key, val))

for k in dict1.keys():
    print("key is : {} and value is : {}".format(k, dict1[k]))

# zip() function allows you to loop over two or more iterables
for k, v in zip(dict1.keys(), dict1.values()): print("key is : {} and value is : {}".format(k, v))

# student dictionary
student = {
    'enrollmentId': 23,
    'name': "Pallavi",
    'city': "Pune",
    'state': "Maharashtra",
    'bloodGroup': "A+"
}

print(student)

#dict1.clear(

for k,v in student.items():
    print(k,v)

employees = OrderedDict()
employees[11] = "Sushant"
employees[2] = "Nikita"
employees[34] = "Vrushali"
employees[24] = "Shweta"
employees[5] = "Pallavi"

for i,j in employees.items():
    print(i,j)
