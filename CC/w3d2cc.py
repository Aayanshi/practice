'''Week 3- Day 2 : Coding Challenge
(Maximum marks -15)

Q1. Write a function to print length of a list
(Easy) (5 marks)

Q2. Write a function to print the reverse of a list, pass the list as a
parameter (Easy) (5 marks)

Q3. Write a function that returns(not prints) the data-type of the last element in a list '''

#1.
a = [2,4,6,1,34,29,33,56,204,"py"]
print(len(a))



b = (2,7,6,8,9)
#2.
def rever(b):
    print(list(b[::-1]))
        
rever(b)

#3.
def last(a):
    return(type(a[0]))

v = last(a)
print(v)
