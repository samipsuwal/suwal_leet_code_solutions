public class Solution {
    public int LengthOfLongestSubstringKDistinct(string s, int k) {
        if (k == 0) return 0;
        Dictionary<char, int> dict = new ();
        
        int i =0;
        int j =0;
        int size = s.Length;
        int max =0;
        
        if (size ==1 && k ==1) {
            return 1;
        }
        dict.Add(s[i],1);
        while (i < size){
            
            while ( dict.Count <= k) {
                max = Math.Max(max, GetValueCount(dict));
                j++;
                if (j >= size) {
                    return max;
                }
                if (dict.ContainsKey(s[j])){
                   // Console.WriteLine("Counter " +s[j].ToString());
                    dict[s[j]] = dict[s[j]]+1;
                } else {
                    //Console.WriteLine("Adding " +s[j].ToString());
                    dict.Add(s[j],1);
                }
                
            }
            /*if (dict.ContainsKey(s[i]))
                if (dict[s[i]] > 0) dict[s[i]] = dict[s[i]]-1;
                else dict.Remove(s[i]);*/
            dict[s[i]] = dict[s[i]]-1;
            if (dict[s[i]] == 0) dict.Remove(s[i]);
            
            i++;
        }
        return max;
    }
    
    public int GetValueCount(Dictionary<char, int> dict) {
        int sum =0;
        foreach (KeyValuePair<char, int> c in dict) {
            //Console.WriteLine(c.Key.ToString()+ " " + c.Value);
            sum += c.Value;
        }
       // Console.WriteLine(sum);
        return sum;
    }
}