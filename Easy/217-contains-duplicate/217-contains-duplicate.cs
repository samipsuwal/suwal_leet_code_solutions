public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary <int, bool> dict = new Dictionary<int, bool>();
        
        foreach (int num in nums){
            if (dict.ContainsKey(num)){
                return true;
            } else {
                dict.Add(num, true);
            }
        }
        return false;
    }
}