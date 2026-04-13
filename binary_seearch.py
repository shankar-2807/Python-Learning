def binarySearch(li, searchEle):
    beg = 0
    end = len(li)-1
    while(beg <= end):
        mid = (beg + end) // 2
        if(searchEle == li[mid]):
            return mid
        elif(searchEle > li[mid]):
            beg = mid+1
        elif(searchEle < li[mid]):
            end = mid -1
    else:
        return - 1
    


li = [10, 20, 30, 40, 50, 60]
ele = int(input("Enter number to find:"))
ind = binarySearch(li, ele)
if(ind != -1):
    print(f'Index of {ele} is {ind}')
else:
    print(f'Index of {ele} not found.')








