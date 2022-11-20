''' question 1
  FizzBuzz - if a number is divisible by 3 - print Fizz, if a number is
divisible by 5 - print Fuzz,if a number is divisible by both - print
Fizz-Buzz'''

n1 = int(input("enter your no.- "))
if n1 % 3 ==0 and n1 % 5 == 0:
    print("fizz-Buzz")
elif n1 % 3 == 0:
    print("fizz")
elif n1 % 5 == 0 :
    print("fuzz")
else :
    print("beta tumse na ho paayega")       





n1 = int(input("enter your no.- "))
if n1 % 3 and n1 % 5:
    print("fizz-Buzz")
