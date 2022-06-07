# ISLAND PERIMETER - PYTHON
Calculating the perimiter of an island in a an ocean using python.


## PROBLEM
Create a function `def island_perimeter(grid):`
that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:  
0 represents water  
1 represents land  
Each cell is square, with a side length of 1  
Cells are connected horizontally/vertically (not diagonally).  
grid is rectangular, with its width and height not exceeding 100  
- The `grid` is completely surrounded by water  
- There is only one island (or nothing).  
- The island doesn't have "lakes" (water inside that isn't
connected to the water surrounding the island).


## HOW I WORK IT OUT
- For every box, check if the left, right, top and bottom nodes are
water.
- If true, increment the perimeter by one.
- Else, continue
- If the top, right, left or bottom is `0`, then that part is water.
- If it is `1`, it is land.

## Testing
You can test with the following example
```

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))
## This should display 12
## Every figure represent one node

```
