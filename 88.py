class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total=len(nums1)

        for i in range(m,total):
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()