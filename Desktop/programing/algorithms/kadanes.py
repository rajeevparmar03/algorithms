#kadnes algorithm 
#largest sum contigious subarray 

def largestsubarray(arr):
    maxsofar=arr[0]
    maxEndinghere=arr[0]
    for i in range(1,len(arr)):
        maxEndinghere=max(arr[i],maxEndinghere+arr[i])
        maxsofar=max(maxsofar,maxEndinghere)
    return maxsofar

a=[-5,4,6,-3,4,-1]
result =largestsubarray(a)
print(result)
