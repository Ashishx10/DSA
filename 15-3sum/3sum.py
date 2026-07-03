class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        answer=[]
        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if summ==0:
                    answer.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif summ<0:
                    j+=1
                else:
                    k-=1
        return answer
#time complexity:o(n^2)
#space complexity:o(n)