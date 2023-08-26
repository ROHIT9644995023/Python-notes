# readfile
# open function (open text file)
# read method (read text file)
# seek method (read again file)
# tell method (read indexing possition)
# readline method (one time in read one line)
# readlines method (text file of in one list)
# close method (need close file)
# name , closed

f = open('file1.txt')

# print(f'curser position - {f.tell()}') 
# print(f.read())
# print(f'curser position - {f.tell()}') 

# print(f.readline(), end="")
# print(f.readline())
# print(f.readline())

# print(f'curser position - {f.tell()}')
# print('before seek method')
# f.seek(0) 
# print('after seek method')
# print(f'curser position - {f.tell()}')
# print(f.read())

# lines = f.readlines()
# print(lines)
# print(len(lines))
# for line in lines:
    # print(line,end="")

# name , closed
# print(f.name)
# print(f.closed)

f.close()

# print(f.closed)
