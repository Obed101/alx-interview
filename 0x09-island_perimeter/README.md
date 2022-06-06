# ISLAND PERIMETER - PYTHON
Calculating the perimiter of an island in a an ocean using python.


## HOW TO WORK IT OUT
- For every box, check if the left, right, top and bottom nodes are
water.
- If true, increment the perimeter by one.
- Else, continue
- If the top, right left or bottom is 0, then that part is water.

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
## This should display twelve
## Every figure represent one node

```
