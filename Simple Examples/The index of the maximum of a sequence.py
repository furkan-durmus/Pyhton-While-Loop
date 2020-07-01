# A sequence consists of integer numbers and ends with the number 0. Determine the index of the largest element of the sequence.
# If the highest element is not unique, print the index of the first of them.

a=int(input())
index=1
maxindex=0
max=0

while a!=0:
    if a>max:
        max=a
        maxindex=index
    a = int(input())
    index+=1
print(maxindex)