def containsDuplicateBruteForce(nums):
    #brute force time complexity of O(n^2) but a space complexity of O(1)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True 

    return False

def containsDuplicateMap(nums):
    map1={}
    for i in nums:
        if i in map1:
            return True
        else:
            map1[i]=True
    
    return False

nums1 = [1,7,3,4,6,7]
nums2 = [1,7,3,4,6]
print(containsDuplicateBruteForce(nums1))
print(containsDuplicateMap(nums1))
print(containsDuplicateBruteForce(nums2))
print(containsDuplicateMap(nums2))      