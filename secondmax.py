li = [5, 3, 7, 2, 9, 10, 20, 15]

max = li[0]
smax = 0

for i in range(0, len(li)):
    if(max < li[i]):
        smax = max
        max = li[i]
    elif(smax <li[i]):
        smax = li[i]

print("Maximam: ", max)
print("Second maximum: ", smax)

