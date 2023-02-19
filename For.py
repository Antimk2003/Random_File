AB = []
AC = int(input("Enter the value = "))

for i in range(AC):
    value = int(input("Enter the value = "))
    AB.append(value)

print("Original list = ",AB)

Left = AB[0]
for i in range(1,AC):
    AB[i-1] = AB[i]
AB[AC-1] = Left

print("Rotate list = ",AB)


print("************************|(2):program|***********************")


arr = [23,567,890,4536,2345]

maximum = arr[0]
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
print(maximum)

minimum = arr[0]
for i in range(len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
print(minimum)

print("____________________________________")

arr = [12,34,56,78,45]
print("min:", min(arr))
print("max:", max(arr))



print("************************|(3):program|***********************")


# program multiply wo matrics using nested loop

x = [[1,2,3],
    [3,4,5]]

y = [[5,6,7],
    [7,8,9]]

result = [[0,0,0],
         [0,0,0]] 

# iterate through rows
for i in range(len(x)):

    # iterate through columns
    for j in range(len(x[0])):
        result[i][j] = x[i][j] * y[i][j]
        
for r in result:
    print(r)

[[5,21],
[12,32],
[21,45]]    
