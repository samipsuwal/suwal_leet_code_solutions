class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        tel = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        
        totalCombo =0
        combos=[]
        
        def helper(index, combo):
            if len(combo) >= len(digits):
                combos.append(combo)
                return
            
            for i in range(index, len(digits)):
                for text in tel[digits[i]]:
                    helper(i+1,combo+text)
            
        helper(0,"")
        
        
        return (combos)
                