def linearSearch(li, searchEle):
    for i in range(len(li)):
        if(searchEle == li[i]):
            return i
    else:
        return -1
    
li = [5, 3, 7, 10, 35, 23]
ele = int(input("Enter number to find:"))
ind = linearSearch(li,ele)

if(ind != -1):
    print(f'Index of {ele} is {ind}')
else:
    print(f'{ele} not found in list.')


