import heapq

def findKthLargest(nums, k):
    nums = [-num for num in nums]
    heapq.heapify(nums)

    for i in range(k-1):
        heapq.heappop(nums)
    
    return -1*heapq.heappop(nums)