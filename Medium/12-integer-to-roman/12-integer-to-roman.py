class Solution:
    def intToRoman(self, num: int) -> str:
        
        #place 1, 10, 20...
        
        def getRomanOfDigit(digit, place):
            
            
            dict = {
                0: {1:"",2:"", 3:"", 4:""},
                1: {1:"I",2:"X", 3:"C", 4:"M"},
                2: {1:"II",2:"XX", 3:"CC", 4: "MM"},
                3: {1:"III",2:"XXX", 3:"CCC", 4: "MMM"},
                4: {1:"IV",2:"XL", 3:"CD"},
                5: {1:"V",2:"L", 3:"D"},
                6: {1:"VI",2:"LX", 3:"DC"},
                7: {1:"VII",2:"LXX", 3:"DCC"},
                8: {1:"VIII",2:"LXXX", 3:"DCCC"},
                9: {1:"IX",2:"XC", 3:"CM"},
                
            }
            
            return dict[digit][place]
            
        ans=""
        place =1
        while num > 0:
            digit = num%10
            ans = getRomanOfDigit(digit, place)+ans
            place+=1
            num = num//10
            
        return ans
            
            
            
        