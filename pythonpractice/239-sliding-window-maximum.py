from typing import List

""" You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array 
to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max of the sliding window. """


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if len(nums) == 0:
            return ans
        from collections import deque

        q = deque()

        for i in range(0, len(nums)):
            if len(q) > 0 and i - q[0] >= k:
                q.popleft()
            while len(q) > 0 and nums[i] > nums[q[len(q) - 1]]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans


print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
