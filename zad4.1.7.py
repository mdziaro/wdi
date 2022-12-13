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

    # colour the board in a checker pattern

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i%2 == j%2:
                grid[i][j] = 0
            else:
                grid[i][j] = 1

    plt.rcParams["figure.figsize"] = (10*dim, 10 * dim)
    plt.matshow(grid, cmap="gray")
    #place knights in the corresponding positions
    for r, c in positions:
        if r%2 == c%2:
            plt.text(r - 0.5, c - 0.6, "\u2658", fontsize=(1000/dim))
        else:
            plt.text(r - 0.5, c - 0.6, "\u2658", fontsize=(1000/dim), color="white")

    plt.show()

# Tests:
dimension = 10
#positions = [(1, 2), (2, 4), (3, 5)] # szachują się wzajemnie
#positions = [(1, 2), (2, 3), (3, 4)] # żaden się nie szachuje
#positions = [(1, 2), (2, 1), (3, 3)] # jeden jest szachowany przez dwa jednocześnie

#test losowy:
'''
import random
positions = []
for _ in range(random.randint(0, 100)):
    temp = ((random.randint(0, dimension-1), random.randint(0, dimension-1)))
    if temp not in positions:
        positions.append(temp)
print(positions)
'''

# Find the positions of knights that check each other

checking_knights = find_checking_knights(positions)
checking_knights_pairs = []
for i in range(0, len(checking_knights)-1, 2):
     checking_knights_pairs.append([checking_knights[i], checking_knights[i+1]])
print("Szachujące się pary: ", checking_knights_pairs)


# Visualize the positions of the knights on the chessboard
visualize_knights(positions, dimension)

# Visualize the positions of the knights that check each other on the chessboard
visualize_knights(checking_knights, dimension)
