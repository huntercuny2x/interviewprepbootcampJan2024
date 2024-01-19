def rob(nums): 
    if len(nums) <= 2:
        return max(nums)
    
    rob1, rob2 = nums[0], max(nums[1],nums[0])

    for i in range(2,len(nums)):
        temp = max(nums[i] + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2