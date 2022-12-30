arr = [2,3,4,5,6,7,8,9,11,15,17,28,30,37,40,55,60,77,84,98,110,111]
'''search = input(" from Which search you want to go \n1.Linear Search\n2.Binary Search \nchoose one number asap! =   ")
if search == "1":
    print("Call = linear_search(arr,search)")
else :
    print("Call= binary_search(arr,target)")  '''  

target = int(input(f"Enter your number u want to search from{arr}= "))    

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(arr[i])
        else:
            continue
    #print("oops")
        
'''d = linear_search(arr,target)
print(d)     '''   

def binary_search(arr,target):
    l = 0
    h = len(arr)-1 
    while l <= h :
        mid = (l+h)//2
        if arr[mid] < target :
            l = mid + 1
        
        elif arr[mid] > target :
            h = mid - 1
        
        else:
            return mid    
    return -1                  


c = binary_search(arr,target)
print(c)
