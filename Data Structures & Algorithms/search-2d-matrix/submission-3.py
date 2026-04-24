class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        curr = -1
        for i in range(len(matrix)-1):
            if matrix[i][0]<target and matrix[i+1][0]>target:
                curr = i
                break
            elif matrix[i][0]==target:
                return True
            elif matrix[i+1][0]==target:
                return True
        if curr == -1:
            curr = len(matrix)-1
        st = 0
        dr = len(matrix[curr]) - 1
        
        while st <= dr:
            mij = (st + dr) // 2
            
            if matrix[curr][mij] == target:
                return True
            elif matrix[curr][mij] < target:
                st = mij + 1
            else:
                dr = mij - 1
        
        return False
        