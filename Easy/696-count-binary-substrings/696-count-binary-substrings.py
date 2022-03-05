class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans=0
        n = len(s)
        toMatch = s[0]
        li=[1]
        liCounter = 0

        for i in range (1,len(s)):
            if toMatch == s[i]:
                li[liCounter] = li[liCounter]+1
            else:
                liCounter+=1
                toMatch =s[i]
                li.append(1)

        for i in range (len(li)-1):
            low = min(li[i], li[i+1])
            ans+= low

        print(li)
        return ans
        