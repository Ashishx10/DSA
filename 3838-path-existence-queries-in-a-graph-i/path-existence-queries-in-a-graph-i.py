class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        groups=[0]*n #to store the group id for each node
        current_id=0
        for i in range(1,n):
            if nums[i]-nums[i-1]>maxDiff:
                current_id+=1
            groups[i]=current_id
        answer=[]
        for li,ri in queries:
            answer.append(groups[li]==groups[ri])
        return answer

