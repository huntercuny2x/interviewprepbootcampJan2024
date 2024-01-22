def subsets(nums):
    power_set = []

    def backtrack(i, sub_set):
        if i == len(nums):
            power_set.append(sub_set[::])
            return

        sub_set.append(nums[i])
        backtrack(i+1,sub_set)

        sub_set.pop()
        backtrack(i+1,sub_set) 

    backtrack(0,[])
    return power_set   