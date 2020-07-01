# The sequence consists of distinct positive integer numbers and ends with the number 0.
# Determine the value of the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.

a=int(input())
max=0
max2=-1

while a!=0:
    if max<a:
        max=a
    a=int(input())
    if max<a and max>max2:
        max2=max
        max=a
    elif max>a and a>max2:
        max2=a

print(max2)

# Or

first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)
