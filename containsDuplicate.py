class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mdict = {}
        n = 0
        for num in nums:
            try:
                mdict[num] += 1
            except:
                mdict[num] = 1
        for (k, v) in mdict.items():
            if v >= 2:
                return True
        return False
