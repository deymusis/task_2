"""Create a list using the for loop, which will consist of 5 elements.

Create an empty list and perform operations on it:

add the number 5 and -6
add the whole first list to it
sort the list

Print both lists without loops."""

a = []

for i in range(5):
    a.append(i)
    i += 1

b = []

b.extend([5, -6])
b.extend(a)
b.sort()

print(a)
print(b)