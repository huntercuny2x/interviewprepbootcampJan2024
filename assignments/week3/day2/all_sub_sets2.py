def subsetsWithDup(nums): 
    power_set = []
    nums.sort()
    
    def backtrack(i, sub_set):
        if i == len(nums):
            power_set.append(sub_set[::])
            return

        sub_set.append(nums[i])
        backtrack(i+1,sub_set)

        sub_set.pop()
        
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i+1,sub_set)

    backtrack(0,[])
    return power_set