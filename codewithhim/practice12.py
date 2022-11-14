'''paint your name in three rows and 5 columns'''
n = input("your name= ")
for i in range(0,3,1):
    for j in range(0,5,1):
        print(n, end=" ")
    print()        