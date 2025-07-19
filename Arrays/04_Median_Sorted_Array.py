# nums1 = [1,3]
# nums2 = [2]
# sorted_arr =  sorted(nums1 + nums2)
# print(sorted_arr)
# median(sorted_arr)

#this is the BRUTE FORCE APPROACH 
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sorted_arr = sorted(nums1+nums2)
        length = len(sorted_arr)
        if length % 2 != 0:
            return sorted_arr[length // 2]
        else :
            mid1 = sorted_arr[length // 2]
            mid2 = sorted_arr[(length // 2)-1]
            return (mid1 + mid2)/2
#time complexity of this is O((n + m) log(n + m))

#Leetcode accepted 
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (n1 + n2 + 1) // 2 - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]


            r1 = float('inf') if mid1 == n1 else nums1[mid1]
            r2 = float('inf') if mid2 == n2 else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0.0
    
sol = Solution()
print(sol.findMedianSortedArrays([1,3,5,7,9],[2,3,5,10]))
print(sol.findMedianSortedArrays([1,3],[2]))
print(sol.findMedianSortedArrays([1,2],[3,4]))