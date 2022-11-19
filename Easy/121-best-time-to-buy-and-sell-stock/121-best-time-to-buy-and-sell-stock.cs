public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length ==1){
            return 0;
        }
        
        int maxSoFar = prices[prices.Length-1];
        
        int[] arr = new int[prices.Length];
        arr[arr.Length-1] = 0;
        for (int i = prices.Length-2; i>=0; i--){
            if (prices[i] > maxSoFar) {
                arr[i] = 0; maxSoFar = prices[i];
            } else{
                arr[i] = maxSoFar - prices[i];
            }
        }
        maxSoFar =0;
        foreach (int a in arr) {
            maxSoFar = Math.Max(maxSoFar, a);
        }
        return maxSoFar;
    }
}