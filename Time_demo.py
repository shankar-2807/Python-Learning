import time

# print(1)
# time.sleep(1)
# print(2)

# for i in range(1, 10):
#     print(i)
#     time.sleep(1)

# print(time.location())

# str = '30-04-2025 10:09:15'
# print(time.strftime('%d-%m-%Y %H:%M:%S'))   #"F" means format: locationtime formating to given formet
# time.strptime

print(time.strftime('%d-%m-%Y %H:%M:%S'))
print(time.strptime('30-04-2025 10:09:15' , '%d-%m-%Y %H:%M:%S'))

#if we run this file directly the answer is, __namae__ return __main__
#if the file execute from another file, __name__ returns name of this file

