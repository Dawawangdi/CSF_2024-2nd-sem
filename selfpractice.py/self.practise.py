#reverse array and strings

class Solution(object):
    def reverseWords(self,s):
        """
        :type.s: str
        :rtype : str
        """
        words = s.strip().split()
        words.reverse()
        return ' '.join(words)

sol = Solution()
print(sol.reverseWords("i   can   love u"))

#escape character('\')
sentence = 'i am \'coader \''
print(sentence)
q= "we will do it!\"said pema\""
print(q)

a = 'kham'
print(a[3])
x = ".  NameError"
for i in ".  NameError":
    print(i)

z = "kham"
print(len(z))

za = "Karma is good and well."  
print("good" in za)

u = "karma you can do it"
print("karma   " not in u)
print("karma" not in u)
if "do"  not in u:
    print("yes 'do' present in u.")

#slicing
#Syntax: string[start:stop]
#The start index is where the slice starts (inclusive).
#The stop index is where the slice ends (exclusive).
''' 
H   e   l   l   o   ,       W   o   r   l   d   !
0   1   2   3   4   5   6   7   8   9  10  11  12
-13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
'''
b = 'Hello, karma'
print(b[1:3])
print(b[:7])
print(b[3:])
print(b[-8:-3])
 










    

