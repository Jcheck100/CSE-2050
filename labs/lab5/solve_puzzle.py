def solve_puzzle(board): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    return _solve_puzzle(board, index=0, visited=set())

def _solve_puzzle(board, index, visited):

    if index == len(board) - 1:
        return True
    if index in visited:
        return False
    
    visited.add(index)
                
    index_cw = (index + board[index]) % len(board)
    index_ccw = (index - board[index]) % len(board)

    return _solve_puzzle(board, index_cw, visited) or _solve_puzzle(board, index_ccw, visited)