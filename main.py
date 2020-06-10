# Day -9
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        # i=0
        # j = 0
        # while i<len(s) and j<len(t): 
        #     print(t[j])
        #     if (s[i] == t[j]):
        #         # print(t[j])
        #         i+=1   
        #     else:
        #         j+=1
        # print(i)
        # return i==len(s)
        if(len(s)==0): 
            return True
        if(len(t)==0):
            return False
        if(s[0]==t[0]):
            return self.isSubsequence(s[1:],t[1:])
        else:
            return self.isSubsequence(s,t[1:])