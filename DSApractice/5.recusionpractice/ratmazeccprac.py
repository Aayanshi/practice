##cc practice

def waysmouse(i,j,n,m,maze):
    if i >= n:
        return 0
    if j >= m:
        return 0
    if maze[i][j] == 1 :
        return 0  
    if i == n-1 and j == n-1 :
        return 1  

    c = waysmouse(i+1,j,n,m,maze)  + waysmouse(i,j+1,n,m,maze)
    return c


if __name__ == "__main__":



    maze =    [[1, 0, 0, 0],
               [1, 1, 0, 1],
               [0, 1, 0, 0],
               [1, 1, 1, 1]]
    
    n = len(maze)
    m = len(maze[0])
    print(f"Dimension = {n} x {m} ")



    result = waysmouse(0,0,n,m,maze)
    print(result, "only way")

    



