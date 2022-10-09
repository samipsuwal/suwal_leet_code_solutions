public class Solution {
    public int ArraySign(int[] nums) {
        int product =1;
        
        foreach (int num in nums) {
            product *= num;
            if (product >0){
                product =1;
            } 
            if (product <0) {
                product = -1;
            }
        }
        
        if (product ==0){
            return 0;
        } else if (product > 0){
            return 1;
        } else {
            return -1;
        }
        
    }
}