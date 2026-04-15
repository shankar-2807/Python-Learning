def selectionsort(li):
    for i in range(0, len(li) - 1):
        ind = i
        for j in range(i + 1, len(li)):
            if(li[ind] > li[j]):
                ind = j
        li[i], li[ind] = li[ind], li[i]
        print(li)
    return li

li = [60, 50, 40, 30, 20, 10]
print("sorted list:", selectionsort(li))



