# Given an integer not less than 2. Print its smallest integer divisor greater than 1.



n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)






# Or
a = int(input())
b=2
while b<=a:
    if a%b==0:
        print(b)
        break
    b+=1




# Or
a = int(input())
mdvider=1
for i in range(2,a+1):
    if a%i==0:
        mdvider=i
        break
print(mdvider)
