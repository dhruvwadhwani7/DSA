#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0


class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and  a == nums[i-1]:
                continue
            
            l,r = i+1,len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0 :
                    r -= 1
                elif threeSum < 0 :
                    l += 1
                else :
                    result.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r  :
                        l += 1 
        return result
    
sol = Solution()
# print(sol.threeSum([-2,-1,0,2,1]))
print(sol.threeSum([-1,0,1,2,-1,-4])) #pass
print(sol.threeSum([0,1,1]))
print(sol.threeSum([0,0,0]))

