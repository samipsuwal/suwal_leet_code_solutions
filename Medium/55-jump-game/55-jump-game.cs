public class Solution {
    public bool CanJump(int[] nums) {
        int len = nums.Length;
        
        if (len ==1) {
            return true;
        }
        
        int lastIndex = len -1;
        
        for (int i = len -2; i >=0; i--){
            if (i + nums[i] >= lastIndex){
                lastIndex = i;
            }
        }
        
        if (lastIndex ==0) return true;
        return false;
    }
    
    
}