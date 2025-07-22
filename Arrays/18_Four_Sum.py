# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

# eg 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


# class Solution(object):
#     def fourSum(self, nums, target):
#         for i in nums:
#             a,l,r = nums[0],i+1,len(nums)-1
            
        
nums = [1,0,-1,0,-2,2]
target = 0
result = []

nums.sort()
for i,a in enumerate(nums) :
    if i>0 and a == nums[i-1]:
        continue
    
    l,r = i+1,len(nums)-1
    while l < r:
        fSum = a + nums[l] + nums[r]
        for j in nums :
            if (fSum == target - nums[j]) and a != target - nums[j] and l!= target - nums[j] and r != target - nums[j]:
                result.append([a,nums[l],nums[r],nums[j]])
        if fSum < target :
            l += 1
        elif fSum > target :
            r -= 1
print(result)
        