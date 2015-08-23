class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for x in range(m)]
        l = 0
        for j in range(m):
            for i in range(n):
                dp[j][i]=int(matrix[j][i])
                if i and j and dp[j][i]:
                    dp[j][i]=min(dp[j-1][i-1], dp[j][i-1],dp[j-1][i])+1
                l = max(dp[j][i], l)
        return l*l
