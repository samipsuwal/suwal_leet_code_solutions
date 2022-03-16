class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #wordDict.sort()
        def helper(s, wordDict, memo):

            if s in memo:
                return memo[s]
            if s=="":
                return True

            for w in wordDict:
                if s.startswith(w):
                    memo[s] = helper(s[len(w):], wordDict, memo)
                    if memo[s]==True:
                        return True

            memo[s] = False
            return memo[s]

        return helper(s, wordDict, {})