arr = [1, 14, 20, 30, 32, 37, 54, 56, 70, 78, 94]
target = int(input(f"Enter your target from {arr} = "))

def Binary_Search(arr,target):
    l = 0
    h = len(arr)-1
    while l <= h :
        mid = (l+h)//2 
        if arr[mid] < target :
            l = mid + 1

        elif arr[mid] > target :
            h = mid - 1

        else :
            return mid

    return -1                

result =Binary_Search(arr,target)
print(result)