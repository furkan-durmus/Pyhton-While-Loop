# The Fibonacci sequence is defined as follows:
# ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
# Given a non-negative integer n, print the nth Fibonacci number ϕn.
# This problem can also be solved with a for loop.


a = int(input())
pre=0
next=1
sum=0
i=0
while i<a:
    sum=pre+next
    pre,next,i=next,sum,(i+1)
print(pre)

# Or

n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)