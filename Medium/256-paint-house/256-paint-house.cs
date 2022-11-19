public class Solution {
    private Dictionary<string, int> memo;
    public int MinCost(int[][] costs) {
        int min = Int32.MaxValue;
        int currMin;
        
        this.memo = new ();
        
        for (int j =0; j < costs[0].GetLength(0); j++){
            currMin = helper(costs[0][j], costs, 0, j);
            min = Math.Min(min, currMin);
        }
        return min;
    }
    
    public int helper(int prev, int[][] costs, int prevI, int prevJ){
        string key = prevI + " " + prevJ;
        
        if(memo.ContainsKey(key)) return memo[key];
        
        int min = Int32.MaxValue;
        if (prevI +1 >= costs.GetLength(0)){
        
            return prev;
        }
       
        for (int j = 0; j< costs[0].GetLength(0); j++) {
            if (j == prevJ) continue;
            min = Math.Min(min, helper(costs[prevI+1][j], costs, prevI+1, j));
        }
        
        memo.Add(key, min + prev);
          
        return min + prev;
        
    }
}