def intersectionOfList(li1 , li2):
    li = []
    for ele in li1:
        if(ele in li2):
            li.append(ele)
    return li
    
li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]
res= intersectionOfList(li1 , li2)
print("Intersection of list is :",res)

