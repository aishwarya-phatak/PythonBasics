from array import *

marks = array('i',[34,12,67,84,93])
length = len(marks)
copy_marks = array(marks.typecode,marks)
print("----------------------")
print("----------------------")
copy_marks_1 = marks
copy_marks_1.remove(34)
copy_marks_1.append(55)
print(copy_marks_1)
print("----------------------")
print("----------------------")
print(marks)
print("----------------------")
for i in marks: print(i)
print("----------------------")
for i in copy_marks:print(i)
print("----------------------")
for i in marks : print(i * 2)
print("----------------------")
copy_2_marks = array(marks.typecode,[i * 2 for i in marks])
for eachMarks in copy_2_marks:
    print(eachMarks)