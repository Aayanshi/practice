'''x = int(input("enter your number= ")) #8
l = 0                                 #0
h = x                                 #8 [0,1,2,3,4,5,6,7,8]
                                   
mid = (l + h)//2                      #0+8//2 = 4         |repeat until l > h so l = 0; h =2     |now m = 3, l= 3, h= 4      | now l = h 3 = 3
if  x == 0 and x == 1 :
    print(x)
while l < h:
    s = mid * mid                     # s = 4*4 = 16       | s = 2*2 =4            |             | s = 3*3= 9                 | not run noww
    if s == x :                       # 8 = 16 not         | 4 == 8 not                          | 9 = 8not
        print(mid)

    elif s < x :                      # 16 < 8 not         | 4 < 8 ; true [0,1,2,{l}3,4{h}]      | 9< 8 not
        l = mid + 1 

    else:  
        h = mid                       # h =8, 8 = 4                                               | h = 3

    mid = (l+h)// 2                   # 0+4 // 2 = 2        |m = 3 +4 //2 = 3                     | 3+3 // 2  = 3

print(mid-1)                                                                                     #| 3 -1 = 2 ans
   '''
#square = square root X square root isme se ek single 
             



n = int(input("Enter your number= "))
l = 0
h = n
mid = (l+h)//2
if n == 0 or n == 1 :
    print(n)
while l < h :
    s = mid * mid
    if s == n :
        print(mid) 
    elif s < n :
        l = mid + 1

    else :
        h = mid

    mid = (l+h) // 2

print(mid-1)            


