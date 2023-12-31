# define generator function 
# take one number as argument
# generator a sequence of even numbers from 1 to that number
# 5 ----> 2,4
# 7 ----> 2,4,6

# SOLUTION
def even_generator(n):
    # for num in range(1,n+1):
    for num in range (2,n+2,2):
        if num %2==0:
            yield(num)

even_nums = even_generator(20)
for num in even_nums:
    print(num)