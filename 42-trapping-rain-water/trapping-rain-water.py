class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        l=0
        n=len(height)
        r=n-1
        maxL=height[l]
        maxR=height[r]
        while l<r:
            if height[l]<height[r]:
                if maxL>height[l+1]:
                    water+=maxL-height[l+1]
                l+=1
                maxL=max(maxL,height[l])
            else:
                if maxR>height[r-1]:
                    water+=maxR-height[r-1]
                r-=1
                maxR=max(maxR,height[r])
        return water
#time complexity:o(n)
#space complexity:o(1)
        