#lee algorithm is used in bfs in grid from collections import deque
from collections import deque
def leealgo(grid ,start,target):
    row =len(grid)
    cols=len(grid[0])
    movement =[(-1,0),(1,0),(0,-1),(0,1)]
    
    queue=deque()
    visited=set()

    queue.append((*start,0))
    visited.add(start)

    while queue:
        x,y,level=queue.popleft()

        if (x,y)==target:
            return level

        for dx ,dy in movement:
            nx=x+dx
            ny=y+dy
        
        if 0<=nx<row and 0<=ny<cols and grid[nx][ny]!=0 and (nx,ny) not in visited :
            queue.append((nx,ny,level+1))
            visited.add((nx,ny))
    
    return -1

grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1]
]
start=(0,0)
target=(4,4)

shortetsPathLength=leealgo(grid,start,target)

if shortetsPathLength !=-1:
    print(f"the shortest path  {start} to {target} is {shortetsPathLength}")
else:
    print(f"thieris no shortest path {start} to {target}") 
