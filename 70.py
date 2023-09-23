class Solution:
    def helper(self, n: int, memory: dict[int:int]) -> int:
        if n in memory:
            return memory.get(n) 
        step1 =  self.helper(n-1,memory)
        step2 =  self.helper(n-2,memory)

        ans = step1 + step2
        memory.update({n:ans})
        return ans

    def climbStairs(self, n: int) -> int:
        memory = {0:1,1:1}
        return self.helper(n,memory)