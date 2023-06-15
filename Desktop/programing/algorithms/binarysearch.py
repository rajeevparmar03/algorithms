#binary search algorithm 

def binarysearch(arr=[],element=int):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=low+(high -low)//2
        if arr[mid]==element:
            return mid 
        elif arr[mid]<element:
            low=mid+1
        else:
            high=mid-1
    return -1


arr=[2,4,6,8,9,10,15]
element=10
result=binarysearch(arr,element)
print(result)

