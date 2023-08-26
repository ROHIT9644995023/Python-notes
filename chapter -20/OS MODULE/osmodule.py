import os 

# print(os.getcwd()) # current location
# os.chdir('E:\python_tutorial')

# os.mkdir('movies') # create a new folder

# print(os.path.exists('movies')) # pahle se h folder so true othervise false
# if os.path.exists('movies'):
#     print('already exists')
# else:
#     os.mkdir('movies')

# open('file.txt','a').close() # create file
# os.mkdir(r'E:\python_tutorial\rohit') # drive change and create folder

# print(os.listdir()) # watch all files folders

for item in os.listdir():
    path = os.path.join(os.getcwd(),item)
    print(path)

