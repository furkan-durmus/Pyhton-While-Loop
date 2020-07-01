# For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.
a= int(input())
sq=1
while sq**2<=a:
    print(sq**2)
    sq+=1

