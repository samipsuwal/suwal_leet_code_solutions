public class Solution {
    public int Rob(int[] nums) {
        if (nums.Length == 1){
            return nums[0];
        }
        int max = Math.Max(nums[0], nums[1]);
        if (nums.Length  ==2) {
            return max;
        }
        int [] arr = new int[nums.Length];
        
        arr[0] = nums[0];
        int lastUsed = 0;
        
        if (nums[1] > nums[0]){
            arr[1] = nums[1];
            lastUsed =1;
        } else {
            arr[1] = nums[0];
            lastUsed =0;
        }
        
        for (int i = 2; i<nums.Length; i++) {
            if (lastUsed == i-1) {
                if ( nums[i] +arr[i-2] > arr[i-1]) {
                    arr[i] = nums[i] +arr[i-2];
                    lastUsed = i;
                }
                else {
                    arr[i] = arr[i-1];
                }
            } else {
                if ( nums[i] +arr[i-2] > arr[i-1]) {
                    arr[i] =  nums[i] +arr[i-2];
                    lastUsed = i;
                } else {
                    arr[i] = arr[i-1];
                }
            }
            max = Math.Max(max, arr[i]);
        }
        return max; 
        
    }
}