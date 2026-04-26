class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_checks = [0]*9
        row_checks = [0]*9
        column_checks = [0]*9
        db = defaultdict(bool)
        # check rows:
        for i in range(9):
            dr = defaultdict(bool)
            dc = defaultdict(bool)
            
            for j in range(9):
                if board[i][j]!="." and dr[board[i][j]]:
                    return False
                if board[j][i]!="." and dc[board[j][i]]:
                    return False

                if  board[i][j]!="." and db[(i//3,j//3,board[i][j])]:
                    return False
                
                db[(i//3,j//3,board[i][j])] = True
                dc[board[j][i]] = True
                dr[board[i][j]] = True
            

        return True


