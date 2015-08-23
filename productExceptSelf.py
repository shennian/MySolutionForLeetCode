class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [1]
        s = 1
        for i in range(1, len(nums)):
            s *= nums[i-1]
            a.append(s)
        b = [1]
        s = 1
        n = nums[::-1]
        for i in range(1, len(n)):
            s *= n[i-1]
            b.append(s)
        b = b[::-1]
        r = []
        for i in range(len(a)):
            r.append(a[i]*b[i])
        return r
