# WAP to count the accorences given value in tuple.
def countEle(tu, ele):
    count = 0
    for i in tu:
        if (i == ele):
            count += 1
    return count

tu = (10, 20, 30, 10, 40, 20, 40)
ele = 10
print("count: ", countEle(tu,ele))



def countEle(tu, ele):
    count = 0
    for i in tu:
        if (i == ele):
            count += 1
    return count

tu = (10, 20, 30, 10, 40, 20, 40)
ele = 10
print("Index: ", countEle(tu,ele))























