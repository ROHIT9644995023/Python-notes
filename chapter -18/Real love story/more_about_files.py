# with open('story.txt','r', encoding='utf-8') as f:
#     print(f.encoding)
#     data = f.read()
#     print(data)

with open('love_story.txt','r') as f:
    data = f.read(100)
    while len(data) > 0:
        print(data)
        data = f.read(100)
