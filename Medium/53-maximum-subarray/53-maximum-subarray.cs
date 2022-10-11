public class Solution {
    public int MaxSubArray(int[] nums) {
       
        int size = nums.Length;
        int[] arr = new int[size];
        
        arr[0] = nums[0];
        
        for ( int i =1; i< size; i++) {
            if (arr[i-1] + nums[i] > nums[i]){
                arr[i] = arr[i-1] + nums[i];
            } else {
                arr[i] = nums[i];
            }
        }
        
        int max = arr[0];
        foreach (int a in arr) {
            max = max > a ? max: a;
        }
        
        return max;
    }
}