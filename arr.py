def find(arr1,arr2,arr3):
    print("Common value :", end="")
    arr1 = set(arr1)
    arr2 = set(arr2)
    arr3 = set(arr3)
    print(arr1 & arr2 & arr3)

array1 = [12,34,56,78,90,123]    
array2 = [12,23,123,45,56,78,98]
array3 = [ 123,56,47,90,87,12]

print("Array1 :",array1)
print("Array2 :",array2)
print("Array3 :",array3)

find(array1,array2,array3)

print("_________________________*((2):program)*__________________________")

str1 = input("String :")
str2 = input("String :")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if len(str1) == len(str2):
    if sorted_str1 == sorted_str2:
        print("Given strings are anagram")
    else:
        print("Given strings are not anagram")
else:
    print("Given strings are anagram")   


print("_____________________________(3):program_________________________")


my_string = "python"

x = 0

for i in my_string:
    x = x+1
    print(my_string[0:x])

for i in my_string:
    x = x-1
    print(my_string[0:x])


print("_____________________________(4):program_________________________")            


numbers = [1,2,3,4,5,6,7,8,9]
b = []
for i in numbers:
    b.append(i**2)
    print(b)
