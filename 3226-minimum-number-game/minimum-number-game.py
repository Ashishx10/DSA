import heapq
class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        # Convert the list into a min-heap
        heapq.heapify(nums)
        arr = []
        # Simulate the game until the heap is empty
        while nums:
            alice_pick = heapq.heappop(nums)
            bob_pick = heapq.heappop(nums)
            # Bob appends first, then Alice
            arr.append(bob_pick)
            arr.append(alice_pick)
        return arr
