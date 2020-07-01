# 1. Loop control flow: else
"""
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)

########

total_sum = 0
a = int(input())
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input())
else:
    print('Total sum is less than 21 and is equal to', total_sum, '.')


###

total_sum = 0
a = int(input())
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input())
else:
    print('Total sum is less than 21 and is equal to', total_sum, '.')


 ###


 for i in range(5):
    a = int(input())
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')
"""

# 2. Loop control flow: continue
"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
"""

# 3. While True:
"""
n = int(input())
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break
print('Length is', length)
"""

# 4.Multiple assignment
"""
a, b = 0, 1
print(a,b)  #0 1


a = 1
b = 2
a, b = b, a
print(a, b)
# 2 1


def fibonacci(n):
    previous = 1
    current = 1
    for i in range(n):
        previous, current = current, previous + current
    return current

print(fibonacci(6))



"""