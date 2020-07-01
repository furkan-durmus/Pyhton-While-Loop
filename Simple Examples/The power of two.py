# For a given integer N, find the greatest integer x where 2x( 2 power x) is less than or equal to N.
# Print the exponent value and the result of the expression 2x( 2 power x).
# Don't use the operation **.


a = int(input())
b=2
c=1
while b<=a:
    b*=2
    c+=1
print(c-1,b//2)