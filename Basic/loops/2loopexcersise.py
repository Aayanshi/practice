#1.write a python program to print all even numbers 
# from 1 to 100 using for loop.
n1=input("enter your number btw 1 to 100= ")
for i in range(0,101,2):
    print(i,"this is your even numbers")


#2.write a python program to print table of number 
# entered by user using for loop.    
print("chlo table seekhe")
n2 = int(input("enter your number= "))
for i in range(1,11):
    answer = n2*i
    print(n2,"X",i,"=",answer)


table=int(input("here- ")) 
for i in range(1,5)  :
    ans = table * i 
    print(ans)

#3. write a python program to traverse through a 
# string characters using for loop. stringg = "aainaismindblowing"
name = "aainaismindblowing"
for i in name:
    print(i)

name = "aaina"
for i in range(len(name)-1,-1,-1):
    print(name[i])
    
#pallindrome
name = str(input("name to check its pallindrome- "))
reverse = ""
for i in range(len(name)-1,-1,-1):
    reverse = reverse + name[i]
if name == reverse:
    print(name, "its pallindrome")
else :
    print(name,"not huh")    
   

   
    