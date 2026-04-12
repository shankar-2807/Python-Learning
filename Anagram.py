def checkAna(str1, str2):
    if(len(str1) == (str2)):
        data = {}
        for chr1, chr2 in zip(str1,str2):
            if chr1 not in data.keys():
                data[chr1] = 1
            else:
                data[chr1] = data[chr1] + 1
            
            if chr2 not in data.keys():
                data[chr2] = -1
            else:
                data[chr2] = data[chr2] - 1

        for val in data.values():
            if(val != 0):
                return f" '{str1}' and '{str2}' are not Anagram strings."
            else:
                return f" '{str1}' and '{str2}' are Anagram strings."
        
    else:
        return f" '{str1}' and '{str2}' are Anagram strings."


str1 = 'listen'
str2 = 'silent'

print(checkAna(str1, str2))