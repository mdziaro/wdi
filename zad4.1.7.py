positions = [(1, 2), (2, 4), (3, 6), (4, 8), (6, 1), (7, 3), (8, 5), (91,91), (92,93)]


def find_checking_knights(positions):
    checking_knights = []

    # Loop through each knight position
    for i in range(len(positions)):
        r1, c1 = positions[i]

        # Loop through the rest of the knight positions
        for j in range(i + 1, len(positions)):
            r2, c2 = positions[j]

            # Check if the knights are in a position to check each other
            if abs(r1 - r2) == 2 and abs(c1 - c2) == 1 or abs(r1 - r2) == 1 and abs(c1 - c2) == 2:
                checking_knights.append((r1, c1))
                checking_knights.append((r2, c2))

    return checking_knights


import matplotlib.pyplot as plt


def visualize_knights(positions, dim):

    # Create a dimxdim grid of zeros
    grid = [[0 for _ in range(dim)] for _ in range(dim)]

    # Loop through the knight positions and set the grid value at those positions to 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i%2 == j%2:
                grid[i][j] = 0
            else:
                grid[i][j] = 1


    # Use matplotlib to visualize the grid
    plt.rcParams["figure.figsize"] = (10*dim, 10 * dim)
    plt.matshow(grid, cmap="gray")
    for r, c in positions:
        if r%2 == c%2:
            plt.text(r - 0.5, c - 0.6, "\u2658", fontsize=(1000/dim))
        else:
            plt.text(r - 0.5, c - 0.6, "\u2658", fontsize=(1000/dim), color="white")

    plt.show()

# Positions of knights on the chessboard

# Find the positions of knights that check each other
checking_knights = find_checking_knights(positions)
print(checking_knights)

# Visualize the positions of the knights on the chessboard
#visualize_knights(positions)

# Visualize the positions of the knights that check each other on the chessboard
visualize_knights(checking_knights, 100)
