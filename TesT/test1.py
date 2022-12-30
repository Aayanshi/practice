''''Q11. Take An Integer N From User, Print A String Array As Answer For All The Numbers From 1 To N Where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
example1
Input: n = 3
for 1,2,3
Output: ["1","2","Fizz"]
Example 2:
Input: n = 5
for 1,2,3,4,5
Output: ["1","2","Fizz","4","Buzz"]
hint: use list methods to create that list in the range till input'''

'''a = [ ]
n = int(input("Enter Number for Your list="))

for i in range(1,n):
    if i % 3 == 0 and i % 5 == 0:
        a.append("FizzBuzz")

    elif i % 3 == 0:
        a.append("Fizz")

    elif i % 5 == 0:
        a.append("Buzz")

    else:
        a.append(str(i))

print(a)'''


'''Q12. Given An Integer Num, Print The Number Of Steps To Reduce It To Zero. In One Step, If The Current Number Is Even,
 You Have To Divide It By 2, Otherwise, You Have To Subtract 1 From It.
Example 1:
Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.
hint: use while loop like while num !=0 and then write logic inside the loop'''

num = int(input("Enter number by your choice= "))
step = 0
while num != 0:
    if num % 2 == 0:
        num = num / 2 
        step = step + 1

    elif num % 2 != 0:
        num = num - 1
        step = step + 1 

print(f"So, steps have taken to become zero = {step}")

