#part one using recursive dfs

def search(word, grid):
    row, col = len(grid), len(grid[0])
    count = 0

    def find(r, c, i, dr, dc):
        if i == len(word):
            return True
        if (r < 0 or r >= row or c < 0 
            or c >= col or grid[r][c] != word[i]):
            return False
        
        return find(r + dr, c + dc, i + 1, dr, dc) #stay in current direction via reeeeecursion baby
    
    #horizontal/vertical/diagonal
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for r in range(row):
        for c in range(col):
            if grid[r][c] == word[0]:  
                for dr, dc in directions:
                    if find(r, c, 0, dr, dc): #pass a direction/stick to it
                        count += 1  
    return count

"""

#used as testing

grid = [
    ['a','','','a','s','z','w'],
    ['a','x','m','a','s','z','w'],
    ['a','z','m','','','z','w'],
    ['a','z','m','a','','z','w']
]

"""

with open('day_four.txt', 'r') as f:
    grid1 = [list(line.strip()) for line in f]
print(search("XMAS", grid1)) 
