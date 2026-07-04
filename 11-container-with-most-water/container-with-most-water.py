class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        max_amount=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])#increment shorter wall to get larger area
            a=w*h
            max_amount=max(max_amount,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_amount
#time complexity:o(n)
#space complexity:o(1)