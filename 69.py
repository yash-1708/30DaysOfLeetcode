class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x

        start = 0
        end = x-1
        mid = 0

        while(start<=end):
            
            mid = start + (end-start)//2

            if mid*mid < x:
                start = mid+1
            elif mid*mid > x:
                end=mid-1
            else :
                break
        if mid*mid == x:
            return mid
        return end
