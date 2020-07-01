# Determine the average of all elements of the sequence ending with the number 0.

i=0
count=0
s=int(input())
while s!=0:
    i+=s
    count+=1
    s=int(input())
print(i/count)