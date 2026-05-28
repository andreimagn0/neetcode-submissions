class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(len(board)):
            for s in range(len(board)):
                index = (i // 3) * 3 + (s // 3)
                if board[i][s] != '.':
                    if board[i][s] in rows[i] or board[i][s] in squares[index]:
                        return False
                    else:
                        rows[i].add(board[i][s])
                        squares[index].add(board[i][s])
                if board[s][i] != '.':
                    if board[s][i] in cols[i]:
                        return False
                    else:
                        cols[i].add(board[s][i])
                
        return True