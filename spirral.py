import sys

# Initial variables
solved = []
done_rows = done_cols = 0

first_line = sys.stdin.readline().rstrip().split(" ")
size = len(first_line)
matrix = [[None]*size for _ in range(size)]

# Add the first line to the answer and matrix
matrix[0] = [x for x in first_line]
for i in range(1, size):
    matrix[i] = [x for x in sys.stdin.readline().rstrip().split(" ")]

# Process the last guy
if size % 2 == 0:
    last = matrix[size//2][(size//2)-1]
else:
    last = matrix[size//2][size//2]

# Go through the maze
for _ in range((size // 2) + 1):
    solved += matrix[done_rows][done_cols:size-done_cols-1]
    solved += [matrix[i][size-done_cols-1] for i in range(0+done_rows, size-done_rows)]
    solved += matrix[size-done_rows-1][done_cols+1: size-done_cols-1][::-1]
    solved += [matrix[i][done_cols] for i in range(size-done_rows-1, done_rows, -1)]

    done_rows += 1
    done_cols += 1

print(solved)

