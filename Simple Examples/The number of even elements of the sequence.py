# Determine the number of even elements in the sequence ending with the number 0.

a=int(input())
even=0
while a!=0:
    if a%2==0:
        even+=1
    a=int(input())
print(even)