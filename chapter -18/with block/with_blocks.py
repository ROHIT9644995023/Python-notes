# f = open('file1.txt')
# print(f.read())
# f.close

# with block
# content manager
with open('file1.txt') as f:
    data = f.read()
    print(data)

print(f.closed)