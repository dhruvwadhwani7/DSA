# s = "abcabcbb"
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dict1 = {}
        maxlength = 0
        l = 0
        for r in range(len(s)):
            if s[r] in dict1 and dict1[s[r]]>=l:
                l = dict1[s[r]] + 1
            
            dict1[s[r]] = r 
            
            maxlength = max(maxlength,r-l+1)
            
        return maxlength
                 
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
        
        
# s = "abcabcbb"
# print(s[1:8])
# # print(s.split())
# for letters in s : 
#     print(letters)
# dict1 = {}
# for i in range(0,len(s)):
#     substring = s[0:i]
#     if substring in dict1 : 
#         return 
    