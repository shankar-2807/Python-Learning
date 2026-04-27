num = 12345
rev = 0
while (num > 0):
    d = num % 10
    num = num //10
    rev = rev * 10 + d

print(rev)