# Write a program to print pattern
# 10101
# 01010
# 10101
# 01010
# 10101

rows = 5
columns = 5

for i in range(rows):
    for j in range(columns):

        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print() 

