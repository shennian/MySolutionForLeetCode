class Solution(object)
    def searchMatrix(self, matrix, target)

        type matrix List[List[int]]
        type target int
        rtype bool

        m = len(matrix)
        n = len(matrix[0])
        i = n-1
        j = 0
        while i = 0 and j = (m-1)
            if matrix[j][i] == target
                return True
            elif matrix[j][i]  target
                i -= 1
            elif matrix[j][i]  target
                j += 1
        return False
