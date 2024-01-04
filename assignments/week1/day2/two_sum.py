def twoSumMapBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            n_2=target-nums[i]
            if nums[j] == n_2:
                return i,j


def twoSumMap(nums, target):
    map1={}#value,index
    for i,n_1 in enumerate(nums):
        n_2 = target-n_1
        if n_2 in map1:
            return map1[n_2], i
        else: 
            map1[n_1]=i