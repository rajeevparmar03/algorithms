#flood fill algorithm 
#used to fill color in specific cell 

def floodFill(grid,start_row,start_col,new_color):
    original_color=grid[start_row][start_col]

    if original_color==new_color or start_row<0 or start_row>=len(grid) or start_col<0 or start_col>=len(grid):
        return 
    

    def dfs(row,col):

        if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]!=original_color:
            return 
        
        grid[row][col]=new_color

        dfs(row-1,col)
        dfs(row+1,col)
        dfs(row,col-1)
        dfs(row,col+1)
    
    dfs(start_row,start_col)


grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]


result=floodFill(grid,2,2,3)

for row in grid :
    print(row)
