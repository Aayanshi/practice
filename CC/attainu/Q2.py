'''Given a non-empty array of decimal digits representing a non-negative integer, increment one
to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each
element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:
Input: digits = [0]
Output: [1]
Constraints:
● 1 <= digits.length <= 100
● 0 <= digits[i] <= 9 (5 marks)'''


'''l = [0,9]
g = len(l)
#print(g)
for i in range(g-1,-1,-1):   
    b = l[i]+1 
    if b > 9 :
        l[i] = 0
        if i == 0 :
            b = [1] + b
    else :
        l[i] = l[i] +1 
        break        
    
print(l)
'''



a = [1,2,3] #length
# output = [1,2,4]
l = len(a)
count = 1 
sums = 0
for i in range(l-1, -1,-1): #reverse the list [3,2,1]
    sums = sums+a[i]*count  # = 0+[3]*1 = 3| = 3+2*10= 23| = 23+1*100=123
    count = count*10         # = 1 * 10 = 10|= 10*10 = 100 | = 100 * 10 = 1000 
print(type(sums) )                  #123
dums = str(sums+1)            #"124"
pums = []                      #
for i in range(len(dums)):      
    pums.append(int(dums[i]))     
print(pums)                     #[1,2,4]   







g = len(digits)
for i in range(g-1,-1,-1):   
    b = digits[i]+1 
    if b > 9 :
        digits[i] = 0
        if i == 0 :
            b = [1] + b
    else :
        digits[i] = digits[i] +1 
        break        

print(digits)





'''
a = [1,2,3] #length
# out = [1,2,4]
l = len(a)
count = 1 
sums = 0
for i in range(l-1, -1,-1):
    sums = sums+a[i]*count
    count = count*10
'''



''' c = a[i]*count             [3]*1 | 2
    sums = sums+c              # 
    count = count*10         #  '''


























































































































































































































































