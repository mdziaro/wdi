import matplotlib.pyplot as plt

class ChessKnight:
    def __init__(self, position):
        self.position = position
        self.x, self.y = position

    def checks(self, other):
        x1, y1 = self.position
        x2, y2 = other.position
        return abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2


class ChessBoard:
    def __init__(self, size, knights):
        self.size = size
        self.knights = knights

    def plot(self):
        plt.figure()
        board = [[(0,0,0) for _ in range(self.size)] for _ in range(self.size)]
        for i in range(len(board)):
            for j in range(len(board)):
                if (i+j)%2 == 1:
                    board[i][j] = (255,255,255)
        for knight in self.knights:
            board[knight.x][knight.y] = (0,255,0)
        plt.imshow(board)
        plt.show()

    def knights_checking(self):
        checking_knights = []
        for i, knight1 in enumerate(self.knights):
            for j, knight2 in enumerate(self.knights):
                if i != j and knight1.checks(knight2):
                    if (knight2.position, knight1.position) not in checking_knights:
                        checking_knights.append((knight1.position, knight2.position))
        return checking_knights

    def plot_checking(self):
        plt.figure()
        board = [[(0,0,0) for _ in range(self.size)] for _ in range(self.size)]
        for i in range(len(board)):
            for j in range(len(board)):
                if (i+j)%2 == 1:
                    board[i][j] = (255,255,255)

        for knight in self.knights_checking():
            board[knight[0][0]][knight[0][1]] = (255,0,0)
            board[knight[1][0]][knight[1][1]] = (255,0,0)
        plt.imshow(board)
        plt.show()
