class Solution:

    def __init__(self, w: List[int]):
        self.range= -1
        self.ranges= []
        for weight in w:
            self.range += weight
            self.ranges.append(self.range)


        

    def pickIndex(self) -> int:
        random_num=random.randint(0,self.range)
        left,right = 0,len(self.ranges)-1
        while left<right:
            mid=(left+right)//2
            if self.ranges[mid]<random_num:
                left= mid+1
            else:
                right=mid
        return left
#time complexity:o(n)
#space complexity:o(logn)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()