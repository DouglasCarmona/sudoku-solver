# The board must be a list of list where each list is a row. 
# Each row must have 9 values. Blank spaces are denoted by 0

# This function prints the board in a readable format
def print_board(bo: list):
    for i in range(len(bo)):
        if i % 3  == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j!= 0:
                print("| ", end = "")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")


        