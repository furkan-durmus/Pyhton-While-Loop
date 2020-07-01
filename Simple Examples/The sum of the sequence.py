# Determine the sum of all elements in the sequence, ending with the number 0.

i=0
while True:
    s=int(input())
    if s==0:
        print(i)
        break
    i+=s

# Or

sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)  