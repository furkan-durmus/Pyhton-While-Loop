# Given a sequence of integer numbers ending with the number 0.
# Determine the length of the widest fragment where all the elements are equal to each other.

a=int(input())
wide=1
prewide=1
pre=0
while a!=0:
    pre=a
    a= int(input())
    if pre==a:
        wide+=1
    else:
        if wide>prewide:
            prewide=wide
        wide=1
print(prewide)

