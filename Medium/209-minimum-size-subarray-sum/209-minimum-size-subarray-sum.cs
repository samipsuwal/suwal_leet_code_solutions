public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        // Edge case 1: nums is of length 1 and it doesn't meet the target
        if (nums.Length ==1 && nums[0] < target) {
            return 0;
        } 
        
        // Edge case 2: first element matches the target
        if (nums[0] >= target) {
            return 1;
        }
        
        int i = 0;
        int j = 0;
        int sum = nums[i];
        int minArr = nums.Length +1;
        bool solnFound = false;
        
        while (i < nums.Length){
            // move right forward
            j++;             
            if (j >= nums.Length) {
                break;
            }
            sum = sum + nums[j];            
            // move left forward
            while (sum >= target) {
                minArr = Math.Min(j - i +1, minArr);
                if (minArr == 1) {
                    return 1;
                }
                solnFound = true;
                sum = sum - nums[i];
                i++;
            }       
        }
        
        if (!solnFound) {
            return 0;
        }
        return minArr;
        
    }
}