#quick sort  
def quick_sort(arr):
    if len(arr)<=1:
     return arr
    else:
       pivot=arr[0]
       smaller=[x for x in arr[1:] if x<=pivot]
       greater =[x for x in arr[1:] if x>pivot]
       

       return quick_sort(smaller) +[pivot] +quick_sort(greater)

arr=[23,4,67,14,16,9,35]
sorted =quick_sort(arr)
print(sorted )
