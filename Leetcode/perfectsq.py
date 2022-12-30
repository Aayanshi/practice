'''Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false'''

def perfectsq(n):
    l = 0
    h = n 
    while l<=h:
        mid = (l+h)//2
        s = mid * mid

        if n == 1:
            return 1 

        if s == n :
            return mid

        elif s > n :
            h = mid - 1

        elif s < n :
            l = mid + 1

    return -1             


if __name__== "__main__":
    n = int(input("enter here= "))
    res = perfectsq(n)
    print(res)
    if res == -1 :
        print(False)
    else :
        print(True)    
