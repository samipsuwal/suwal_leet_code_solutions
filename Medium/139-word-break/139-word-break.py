class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, wordDict, memo):

            if s in memo:
                return memo[s]
            if s=="":
                return True

            for w in wordDict:
                if s.startswith(w):
                    T = helper(s[len(w):], wordDict, memo)
                    if T==True:
                        return True

            memo[s] = False
            return memo[s]
            

        return helper(s, wordDict, {})