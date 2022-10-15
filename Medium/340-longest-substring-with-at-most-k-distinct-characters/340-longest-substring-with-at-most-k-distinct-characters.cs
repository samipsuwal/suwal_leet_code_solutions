public class Solution {
    public int LengthOfLongestSubstringKDistinct(string s, int k) {
        if (k == 0) return 0;
        Dictionary<char, int> dict = new ();
        
        int i =0;
        int j =0;
        int size = s.Length;
        int max =0;
        int currLength =0;
        
        if (size ==1 && k ==1) {
            return 1;
        }
        dict.Add(s[i],1);
        currLength++;
        while (i < size){
            
            while ( dict.Count <= k) {
                max = Math.Max(max, currLength);
                j++;
                if (j >= size) {
                    return max;
                }
                if (dict.ContainsKey(s[j])){
                    dict[s[j]] = dict[s[j]]+1;
                    currLength++;
                } else {
                    dict.Add(s[j],1);
                    currLength++;
                }
                
            }
            dict[s[i]] = dict[s[i]]-1;
            if (dict[s[i]] == 0) dict.Remove(s[i]);
            currLength--;
            
            i++;
        }
        return max;
    }
    
    public int GetValueCount(Dictionary<char, int> dict) {
        int sum =0;
        foreach (KeyValuePair<char, int> c in dict) {
            sum += c.Value;
        }
        return sum;
    }
}