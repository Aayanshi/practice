'''Q - 3 ) Valid Anagram (5 Marks):
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false'''
''''''
'''
n = input("here= ")
s = input("here= ")


def anagram(n,s):
    k = False
    for i in n:
        if i not in s or len(n) != len(s):
            return k
        else:
            k = True
    return k            


re = anagram(n,s)
print(re)'''

'''def anagram(n,s):
    k = True
    for i in n:
        if i in s and len(n) == len(s):
            return k
        else:
            k = False
    return k            

re = anagram(n,s)
print(re)'''


'''Q- 2 ) Average Salary Excluding the Minimum and Maximum Salary (5
marks)
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
Given an array of unique integers salary where salary[i] is the salary of the
employee i.
Return the average salary of employees excluding the minimum and maximum
salary.
Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000
respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
'''
                         


'''mi = sorted(n)
mi.remove(mi[0])
mi.remove(mi[-1])
l = len(mi)
c = 0
for i in mi:
    c = c + i
print(c/l)   ''' 

'''n = [1000,2000,3000]
l = len(n)

d = []
for i in range(len(n)):
    mi = n[0]
    me = 0
    for i in range(len(n)):
        if n[i] < mi :
            mi = n[i] 
            me = i
    d.append(mi)
    n.remove(mi)
c = d[1:len(d)-1] 
v = sum(c)

print(v/len(c))  ''' 


salary= [4000,3000,1000,2000]
f = []
for i in range(len(salary)):
    mi = salary[0]
    me = 0
    for i in range(len(salary)):
        if mi > salary[i]:
            mi = salary[i]
            me = i
    f.append(mi)
    salary.remove(mi)
c = 0
for i in range(1,len(f)-1):
    c = c + f[i]
d =c/(len(f)-2)
print(f)
print(d) 






                