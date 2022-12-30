# recursion
#  1. factorial

def factorial(num):
    if num == 1 :
        return 1
    c = num * factorial(num-1)
    return c   

def fibonacii(num):
    if num == 0:
        return 1
    if num == 1:
        return 1

    b = fibonacii(num-1) + fibonacii(num-2) 
    return b   



#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
#0  1  2  3  4  5   6   7   8   9  10   11



if __name__ == "__main__" :
    num = int(input("here= "))
    re = factorial(num)
    print(f"factorial of {num} is {re}")

    ans = fibonacii(num)
    print(f"fibonaccii of {num} is {ans} ")


