class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=len(nums1)
        y=len(nums2)
        merged=[]
        for i in range(m):
                merged.append(nums1[i])
        for j in range(n):
            merged.append(nums2[j])
        merged.sort()
        for i in range(m+n):
            nums1[i]=merged[i]