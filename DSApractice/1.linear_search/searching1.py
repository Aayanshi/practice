# linear Search is one way search (2d)
'''lst = ["apple","lichi","guava","orange","pineapple","mango","kiwi"]
target = "banana"
c = False
for i in lst:
    if i == target :
        c = True
    else :
        continue
       
print(c)

l = [2,4,1,4,17,45,74,46,64,9,00,6,9,28]
n = int(input("enter your number which u chahte ho jaldi bolo= "))
def Search(l,n):
    for i in range(len(l)):
        if l[i] == n :
            return i
            
    return False'''


'''a = Search(l,n)
print(a)
'''

def fruits(ls,x):
    target = x
    if target in ls:
        return True
    return False
  

if __name__ == "__main__":
    ls = [23,67,55,34,28,89,90,1,4,82,00,45,17]
    x = int(input("enter your fav. in list number= "))
    result = fruits(ls,x)
    
    if result == True :
        print("Yes we got it!")
    else:
        print("Oops sorry man!")    


l = [2,4,1,4,17,45,74,46,64,9,00,6,9,28]
t = int(input("number of list u wanted= "))
for i in range(len(l)):
    if l[i] == t:
        print(i)
    else :
        print(l[-1])