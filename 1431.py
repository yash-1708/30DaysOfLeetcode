class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        myMax=max(candies)
        for i in range(len(candies)):
            curr=candies[i]
            curr+=extraCandies
            res.append(myMax<=curr)
        return res