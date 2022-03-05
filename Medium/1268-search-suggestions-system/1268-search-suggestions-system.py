class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        finalAns = []
        
        
        productIndex = 0
        
        for i in range (1, len(searchWord) +1):
            ans = []
            sub = searchWord[:i]
            
            counter = 0
            
            while len(ans) < 3 and counter < len(products):
                if sub == products[counter][:i]:
                    ans.append(products[counter])
                    
                counter+=1
                
            finalAns.append(ans)
            
        return finalAns
        