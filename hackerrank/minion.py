s = 0 
k = 0
n = input("Enter any String= ") #y u v i
le = len(n) #4                   0 1 2 3 
for i in range(le):
    if n[i] in "AEIOUaeiou":
        s = s + (le-i) # 0 + 4-1 agar length me index sub karegey jaise aagey jayegay utne hi words banegey jo index utne hi words
    else:
        k = k + (le-i)

if s > k:
    print(f"aaina always win {s}")
elif k > s:
    print(f"kub jeet udar me di {k}")
else:
    print("aaina se koi nahi jeet skta chlo fir draw kar lete h")        



     



#afganisthan