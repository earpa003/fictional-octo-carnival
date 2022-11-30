# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




# must be in-place sort
def merge_sort(arr,cmp):
    if len(arr)<=1: return arr

    mid = len(arr)//2
    A = merge_sort(arr[:mid],cmp)
    B = merge_sort(arr[mid:],cmp)

    i,j = 0,0
    for x in range(len(arr)):
        if cmp(A[i],B[j]) <= 0:
            arr[x] = A[i]
            i += 1
        else:
            arr[x] = B[j]
            j += 1

    return arr

# must be in-place sort
def quick_sort(arr,cmp):
    pass