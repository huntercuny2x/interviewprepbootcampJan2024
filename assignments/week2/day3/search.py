def search(nums, target):
    start, end = 0, len(nums)-1 
    
    while start <= end:
        mid = (start+end)//2
        if nums[mid] < target:
            start=mid+1
        
        elif nums[mid] > target:
            end = mid-1
        
        else:
            return mid
    
    return -1