#merge sort 


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid =len(arr)//2
    left_half = arr[:mid]
    right_half=arr[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)

    return merge(left_half,right_half)

def merge(left,right):
    result=[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j>len(right):
        result.append(right[i])
        j+=1

    return result


arr=[38,27,43,10]
result=merge_sort(arr)
print(result)

