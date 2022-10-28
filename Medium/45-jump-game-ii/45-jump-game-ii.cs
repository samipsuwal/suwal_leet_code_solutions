public class Solution {
    public int Jump(int[] nums) {
        
        int n = nums.Length;
        if (n ==1) return 0;
        
        
        
        int[] cans = new int[n];
        
        for (int i = n-2; i >=0; i--){
            // we can go to the last index from here
            if (i + nums[i]>= n-1) {
                cans[i] = 1;
                continue;   
            }
            
            int candi = nums[i];
            
            // Atleast one of the candi can take it there.
            int minStep = n;
            bool canJump = false;
            while (candi>0){
                // current step + candidate can jump over
               /* if (nums[i] + cans[candi+i]>= n-i -1){
                    minStep = Math.Min(minStep, cans[candi+i]+1);  
                }*/
                if (cans[candi+i]>0){
                    minStep = Math.Min(minStep, cans[candi+i]+1);    
                    canJump = true;
                }
                candi--;
            }
            if (canJump)
                cans[i] = minStep;
            else
                cans[i] = 0;
        }
        
       
        
        return cans[0];
        
        
        
    }
}