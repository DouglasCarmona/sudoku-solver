class Sudoku:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.n = 9
        self.box = 3
        self.printsudoku()
        print('\n')


    def solvesudoku(self):
        if self.solve(0,0):
            self.printsudoku()
        else:
            print('There is no solution!')
    
    def solve(self,r: int, c:int):

        #if all rows were filled, sudoku was solved
        if r == self.n:
            return True
        
        #if all columns were filled, move to next row
        if c == self.n:
            return self.solve(r+1,0)
        
        if not self.isempty(r,c):
            return self.solve(r,c+1)

        for num in range(1,10): 
            if self.isvalid(num,r,c):
                self.grid[r][c] = num

                if self.solve(r,c+1):
                    return True
                    
                #Backtraking
                self.grid[r][c] = 0
        
        return False

    
    def isempty(self,r: int, c: int) -> bool:
        return self.grid[r][c] == 0


    def isvalid(self, num: int, r: int, c: int) -> bool:
        #Check if num is in the row
        if num in self.get_row(r):
            return False

        #Check if num is in the column
        if num in self.get_col(c):
            return False
        
        #Check if num is in the box
        if num in self.get_box(r,c):
            return False
        
        return True
    
    def get_row(self,r: int) -> list[int]:
        return self.grid[r]
    
    
    def get_col(self, c: int) -> list[int]:
        return [row[c] for row in self.grid]
    

    def get_box(self, r: int, c:int) -> list[int]:
        box = []
        for i, j in self.get_box_inds(r,c):
            box.append(self.grid[i][j])
        return box
    
    def get_box_inds(self, r: int, c: int) -> list[tuple[int,int]]:
        ind_box = []
        i0 = (r//self.box)*self.box 
        j0 = (c//self.box)*self.box
        for i in range(i0, i0 + self.box):
            for j in range(j0, j0 + self.box):
                ind_box.append((i,j))
        return ind_box

    
    def printsudoku(self):
        for i in range(self.n):
            if i % 3 == 0 and i!= 0:
                print(11*'- ')
            for j in range(self.n):
                if j % 3== 0 and j!= 0:
                    print('| ', end = '')
                if j == 8:
                    print(self.grid[i][j])
                else:
                    print(str(self.grid[i][j]) + ' ', end = '')

if __name__ == "__main__":

    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
        ]
        
    mysudoku = Sudoku(board)
    mysudoku.solvesudoku()
    


        



    
