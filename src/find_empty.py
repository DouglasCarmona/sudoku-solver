# This function return the blank spaces in the board 
# Output format: Tuple

def find_empty(bo: list):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) # row, col
    return None
