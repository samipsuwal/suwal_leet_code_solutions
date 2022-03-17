class Solution:
    ans=0
    def numDecodings(self, s: str) -> int:
        
        arr=[]
        
        for i in range(1,27):
            arr.append(str(i))
            
            
        
        def helper(s, arr, memo):
            
            if s =="":
                return 1
            if s in memo:
                return memo[s]
            
            for a in arr:
                if s.startswith(a):
                    temp = helper(s[len(a):], arr, memo)
                    self.ans+=temp
                        
            
            memo[s]= self.ans
            return False
        memo={}
        helper(s, arr,memo)
        return (self.ans)
        