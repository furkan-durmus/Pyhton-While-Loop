# A sequence consists of integer numbers and ends with the number 0.
# Determine how many elements of this sequence are greater than their neighbours above.

a=int(input())
ans=-1
temp=0
while a!=0:
    if temp<a:
        ans+=1
    temp=a
    a=int(input())
print(ans)

# Or

prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)