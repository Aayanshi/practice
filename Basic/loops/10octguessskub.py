#Guess the number
from random import randint
tries = 0
result = randint(1,10)

guess = int(input("guess a number between 1-10 bud! = "))
tries = tries+1

while guess != result :
    if guess > result:
        print("your guess is too high")
        guess = int(input("guess again= "))
        tries = tries+1
    elif guess < result:
        print("your guess is too low")
        guess = int(input("try again= "))
        tries = tries+1
print("congo you got the number this time")
print("it took you", tries," tries to guess the number")



from random import randint
value = 0
ans = randint(1,5)

n1 = (int(input("likh do aukaat me 1 to 5= ")))
value = value + 1

while ans!=n1 :
    if ans > n1 :
        print("your no. is low")
        n1 = int(input("fir se= "))
        value = value + 1
    elif ans < n1 :
        print("your no, is high like u")
        n1 = int(input("last baari= "))
        value = value + 1
print("you are correct , tukka aacha h")        
print("you have tried", value ,"baar")

    
