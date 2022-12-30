# rat maze 
def ratmaze(i,j,n,m,maze):
    if i >= n :
        return 0
    if j >= m :
        return 0
    if maze[i][j] == 1:
        return  0
    if  i == n-1 and j == m-1 :
        return 1
    
    rat = ratmaze(i+1,j,n,m,maze) + ratmaze(i,j+1,n,m,maze)
    return rat


if __name__ == "__main__":
    maze = [
        [0,0,1],
        [1,0,0],
        [1,0,0]
    ]
    
    n = len(maze)
    m = len(maze[0])
    
    print(f"maze is {n} x {m} dimension ")
    
    result = ratmaze(0,0,n,m,maze)
    print(f"only {result}  ways to escape your rat")









def micewheat(i,j,n,m,mazes):
    if i >= n :
        return 0
    if j >= m :
        return 0
    if mazes[i][j] == 1 :
        return 0
    if i == n-1 and j == m-1 :
        return 1    

    mice = micewheat(i+1,j,n,m,mazes) + micewheat(i,j+1,n,m,mazes) 
    return mice     




if __name__ == "__main__" :

   mazes = [[0,0,1,0,1],
            [0,0,0,1,0],
            [1,0,0,0,0]
   ]


   n = len(mazes)
   m = len(mazes[0])
   print(f"mazes of {n} x {m} dimension")

   ans = micewheat(0,0,n,m,mazes)
   print(f"so, {ans} oonly ways left ")