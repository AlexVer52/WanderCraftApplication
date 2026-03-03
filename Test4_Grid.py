grid = []
count = 0

with open("input4.txt", "r") as f:
    for line in f:
        lines = line.strip()
        if not lines:
            continue
        grid.append(list(lines))

rows = len(grid)
cols = len(grid[0])

# relative offsets for the 8 neighbors
dirs8 = [(-1,-1), (-1,0), (-1,1),
         ( 0,-1),         ( 0,1),
         ( 1,-1), ( 1,0), ( 1,1)]

def count_at_neighbors(r, c):
    count = 0
    for dr, dc in dirs8:
        rr = r + dr
        cc = c + dc
        # stay inside the grid
        if 0 <= rr < rows and 0 <= cc < cols:
            if grid[rr][cc] == '@':
                count += 1
    return count

while True:
    # Create a list for position to remove
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell == '@':
                neighbors = count_at_neighbors(r, c)
                if neighbors < 4:
                    count +=1
                    to_remove.append((r, c))
            elif cell == '.':
                continue
    if not to_remove:
        break
    # Remove the cells marked for removal
    for r, c in to_remove:
        grid[r][c] = '.'
print(count)