'''write a python program to print even length words in a string'''
n = "heya i m doing python"
m = n.split()
for i in m:
    if len(i) % 2 == 0:
        print(i)

    
    else:
        continue    

'''"Display Fibonacci series up to 20 terms"
'''
n = int(input("your number = "))
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
first = 0
second = 1
for i in range(0,n): # 0,1,2,3,4,5,6.........20 (n tak hi batayega)
    print(first,end="   ") # 0 , 1 , 1 ,2 ,3 ,5, 8 ,13,21
    c = first + second # c = 0+1, 1 + 1 ,1+2(3), 2 + 3, 3 +5(8),5 +8(13),8 +13(21),13+21(34),21+34(55)
    first = second     # 0 = 1 , 1 = 1, 1 = 2 2 = 3, 3 =5 , 5= 8,8 = 13,13 =21,21=34
    second = c         # 1 = (0+1) ,1 = 2, 2 = 3 , 3 = 5, 5 =8 ,8=13 13 =21,21 =34,34 =55

print()                # first ki value = second se update hokar ke eaual hogi = aur second ki value update ho kar = c ke eaual hogi (in loop)
print(first)    
print(second)
print(c)






'''apna laptop dikha do'''


    

