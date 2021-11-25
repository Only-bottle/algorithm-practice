import sys
sys.setrecursionlimit(10**6)

# DFS by color
def dfs_by_color(x, y, color):
    if color == "R" or color == "G":
        mat[x][y] = 0
    else:
        mat[x][y] = 1

    for i in range(4):
        new_x = dx[i] + x
        new_y = dy[i] + y

        if 0 <= new_x < num and 0 <= new_y < num and mat[new_x][new_y] == color:
            dfs_by_color(new_x, new_y, color)

# Set input
input = sys.stdin.readline
num = int(input())
mat = [list(input().strip()) for _ in range(num)]

# Set variables
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
red, green, blue, red_green = 0, 0, 0, 0

# People without red-green color blindness
for i in range(num):
    for j in range(num):
        if mat[i][j] == "R":
            dfs_by_color(i, j, "R")
            red += 1
        elif mat[i][j] == "G":
            dfs_by_color(i, j, "G")
            green += 1
        elif mat[i][j] == "B":
            dfs_by_color(i, j, "B")
            blue += 1

# People with red-green color blindness
for i in range(num):
    for j in range(num):
        if mat[i][j] == 0:
            dfs_by_color(i, j, 0)
            red_green += 1

# Result
count1 = red + green + blue
count2 = blue + red_green
print(f"{count1} {count2}")