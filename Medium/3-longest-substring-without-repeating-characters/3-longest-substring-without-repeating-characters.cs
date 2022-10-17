public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if (s.Length == 0) {
            return 0;
        }
        
        if (s.Length ==1) {return 1;}
        
        int i =0; int j =0; int max = 1;
        
        Dictionary<char, int> dict = new(); 
        dict.Add(s[j], 1 );
        
        while (i < s.Length) {
            // move j right
            j++;
            if (j>= s.Length){return max;}
            
            if (dict.ContainsKey(s[j])){dict[s[j]] = dict[s[j]]+1;}
            else {dict.Add(s[j],1);}
            
            while(dict[s[j]] >1) {
                // move i right
                if (dict.ContainsKey(s[i])) {
                    dict[s[i]] = dict[s[i]] -1;
                    if (dict[s[i]] == 0) {dict.Remove(s[i]);}
                }
                i++;
            }
            
            max = Math.Max(max, j-i+1);
        }
        
        
        // while not all are unique
        
        return max;
        
    }
}