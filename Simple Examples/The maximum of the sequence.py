# A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence.

a= int(input())
top=0
while a!=0:
    if top<a:
        top=a
    a = int(input())
print(top)