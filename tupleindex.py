def indexEle(tu, ele):
    count =  -1
    for i in tu:
        count += 1
        if (i == ele):
            
            return count
    else:
        return -1
    
tu = (10, 20, 30, 10, 40, 20, 40)
ele = 30
print("Index: ", indexEle(tu,ele))

