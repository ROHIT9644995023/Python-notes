# we use enumerate function with for loop to track psition of our
# item in iterable


# How we can do this without enumeret function
names = ['abc', 'abcd', 'rohit']
# 0 ----> 'abc'
# 1 ----> 'abcd'
# 2 ----> 'rohit'

# position = 0
# for name in names:
#     print(f"{position} : {name}")
#     position += 1 

# with enumerat function

for pos, name in enumerate(names):
    print(f"{pos} : {name}")

# Define  a function that take two arguments
# 1.) list containing string
# 2.) string that want to fine in your list
# and this function will return the index of string in your list and 
# if string is not present then return -1

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
        return -1

print(find_pos(names, 'abcz'))