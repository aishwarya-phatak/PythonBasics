name = "Nikita"
name1 = "Sushant"

n = "A"
n1 = 'A'

numberFive : int = 45
numberSix = 767
print("numberSix value is : {}".format(numberSix))
print("number six value is %d" %numberSix)
print("numberFive and numberSix values are: {} and {}".format(numberFive, numberSix))
print('numberSix plus 5 -- ',numberSix + 5)
print("name is : {}".format(name))
print("name1 is : %s" %name1)

#format specifiers --
# %s - string , %d - decimal or integer, %f - floating point

#numeric data types in Python
#int , float, complex

num1 : int = 10
num2 : int = 23
num3 = num1

print(num1)
print(num2)
print(num3)

number : float = 45.23
print("number value is %f" %number)

numberThree : int
numberThree = 45
print(numberThree)

numberTwo = 13
print(complex(numberTwo,numberThree))
print(float(numberTwo))         #cast to float
print(numberTwo + 30.0)

numberOne : complex =  10 + 20j
print(f"numberOne real and imaginary value is {numberOne.real} -- {numberOne.imag}")

#data type - None
n2 = None
print(n2)

#bool
if numberThree > numberTwo : print("numberThree is greater than numberTwo")

result = numberThree > numberTwo
print(result)