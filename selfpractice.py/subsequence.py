class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i ,j = 0,0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1

        if i == len(s):
            print (True) 
        else:
            print(False)

        return(s,t)
    
sol = Solution()
s = ("axc")
t= ("ahbgdc")
print(sol.isSubsequence(s,t))




