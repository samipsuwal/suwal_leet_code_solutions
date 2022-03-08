class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        totalCost=0
        while len(sticks) !=1:
            sticks.sort()
            a = sticks.pop(0)
            b = sticks.pop(0)

            totalCost += a+b
            sticks.append(a+b)

        return totalCost
        