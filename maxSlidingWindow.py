class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        x = len(nums)
        if x == 0:
            return []
        i = k - 1
        r = []
        while i <= (x-1):
            n = max(nums[i-k+1:i+1])
            r.append(n)
            i += 1
        return r
