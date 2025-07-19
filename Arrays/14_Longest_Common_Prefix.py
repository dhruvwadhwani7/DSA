strs = ["flower","flow","flight"]
strs2 = []
strs3 = ["dog","racecar","car"]
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         if strs == []:
#             return "Empty List"
#         prefix = strs[0]    
#         for word in strs :
#             while word[:len(prefix)] != prefix :   #while not word.startswith(prefix):
#                 prefix = prefix[:-1]
                
#                 if prefix == "":
#                     return "" 
#         return prefix
                


#LEETCODE ACCEPTED 

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs :
            return ""
        prefix = strs[0]     
        for word in strs :
            while word[:len(prefix)] != prefix :   
                prefix = prefix[:-1]
                
                if prefix == "":
                    return "" 
        return prefix
    
sol = Solution() 
print(sol.longestCommonPrefix(strs))
print(sol.longestCommonPrefix(strs2))
print(sol.longestCommonPrefix(strs3))
                
