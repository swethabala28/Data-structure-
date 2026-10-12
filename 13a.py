n = int(input("Enter number of students: "))
a = list(map(int, input("Enter roll numbers: ").split()))
x = int(input("Enter roll number to search: "))

found = False
for i in range(n):
    if a[i] == x:
        found = True
        break

if found:
    print("Linear Search: Roll Number found")
else:
    print("Linear Search: Roll Number not found")

a.sort()
low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if a[mid] == x:
        found = True
        break
    elif a[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Binary Search: Roll Number found")
else:
    print("Binary Search: Roll Number no")
