'''Input:'''
s = ["h","e","l","l","o"]
pt1 = 0
pt2 = len(s)-1

while pt1 < pt2 :
    c = s[pt1]
    s[pt1] = s[pt2]
    s[pt2] = c
    pt1 = pt1 + 1
    pt2 = pt2 - 1
print(s)        