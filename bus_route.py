loc = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"]

dist = [1100, 890, 2500, 3890, 8520, 2100, 3200, 1850, 4135]

src  = (input("Enter source: "))
dest = (input("Enter destination: "))

i_src = loc.index(src)
i_dest = loc.index(dest)
i = i_src
total_dist = 0

while(i != i_dest):
    total_dist = total_dist + dist[i]

    if(i == len(loc) - 1):
        i = 0
    else:
        i += 1

charges = (total_dist / 1000) * 16
print("charges: ", charges)



