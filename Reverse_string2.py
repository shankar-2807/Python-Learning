def rev_str2(str):
    rev_str = ''
    for ele in str:
        rev_str = ele + rev_str
    return rev_str

str = " Hello World!"
print("Reverse String: ",rev_str2(str))

