# Given a sequence of non-negative integers, where each number is written in a separate line.
# Determine the length of the sequence, where the sequence ends when the integer is equal to 0.
# Print the length of the sequence (not counting the integer 0). The numbers following the number 0 should be omitted.
i=0
while True:
    if int(input())==0:
        print(i)
        break
    i+=1


# OR

len = 0
while int(input()) != 0:
    len += 1
print(len)