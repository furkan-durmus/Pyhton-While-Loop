# A sequence consists of integer numbers and ends with the number 0.
# Determine how many elements of this sequence are equal to its largest element.

a=int(input())
ans=1
max=0

while a!=0:
    if a>max:
        max,ans=a,1
    elif a==max:
        ans+=1
    a = int(input())
print(ans)

# Or
