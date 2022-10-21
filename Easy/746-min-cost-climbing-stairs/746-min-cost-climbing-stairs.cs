public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
          int[] minCost = new int[cost.Length];

            minCost[0] = cost[0];
            minCost[1] = cost[1];
            for (int i = 2; i < minCost.Length; i++)
            {
                if (minCost[i - 2] < minCost[i - 1])
                {
                    minCost[i] = minCost[i - 2] + cost[i];
                }
                else
                {
                    minCost[i] = minCost[i - 1] + cost[i];
                }
            }

            if (minCost[minCost.Length - 1] < minCost[minCost.Length - 2])
            {
                return minCost[minCost.Length - 1];
            }

            return minCost[minCost.Length - 2];
        
    }
}