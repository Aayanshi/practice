#ainu ka sol
print("lets check leap year ")
year = (int(input("put here= ")))
if (year % 100 == 0 and year % 400 == 0 ) or year % 4 == 0 :
    print("yeyey, your year is leap year")
else :
    print("your year is not leap,sorry")

#solution leap year kubs ka sol2
year = int(input("enter the year to check =  "))
if year%100 == 0:
    if year%400 == 0:
        print("Hell yeah! \n its a leap year")
    else:
        ("nahi hai buddy leap year")

else:
    if year%4 == 0:
        print("you got it buddy \n its a leap year")
    else:
        print("sorli not a leap year sweetu")

paridha_list = [12, 14, 567, 34, 45, 87]
print(18 in paridha_list)
check = 12 not in paridha_list
if 14 in paridha_list :
    print("yes")
print(check)        
