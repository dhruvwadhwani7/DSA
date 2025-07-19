# def two_sums(nums,target):
#     for i,num in enumerate(nums):
#         complement = target - num
#         if complement in nums :
#             return [nums.index(complement),i]

# print(two_sums([3,3],6))


class Solution:
    def twoSum(nums,target):
        dict1 = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in dict1:
                return [dict1[complement],i]
            dict1[num] = i
        
print(Solution.twoSum([2,7,11,15],9))
print(Solution.twoSum([3,2,4],6))
print(Solution.twoSum([3,3],6))