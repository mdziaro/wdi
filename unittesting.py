from zad5_7 import *

def unit_test1():
    # test where two knights check each other
    knight1 = ChessKnight((0, 0))
    knight2 = ChessKnight((2, 1))
    knight3 = ChessKnight((5, 2))
    board = ChessBoard(10, [knight1, knight2, knight3])
    assert(board.knights_checking()) == [((0, 0), (2, 1))], "Should find ((0,0), (2,1)). Test 1 failed."
    print("Test 1 completed successfully")
    board.plot()
    board.plot_checking()

def unit_test2():
    # test where two knights check each other
    knight1 = ChessKnight((0, 0))
    knight2 = ChessKnight((2, 1))
    knight3 = ChessKnight((1, 2))
    board = ChessBoard(10, [knight1, knight2, knight3])
    assert (board.knights_checking()) == [((0, 0), (2, 1)), ((0, 0), (1, 2))], "Should find ((0, 0), (2, 1)), ((0, 0), (1, 2)). Test 2 failed."
    print("Test 2 completed successfully")
    board.plot()
    board.plot_checking()

def unit_test3():
    # test where two knights check each other
    knight1 = ChessKnight((0, 0))
    knight2 = ChessKnight((2, 2))
    knight3 = ChessKnight((3, 3))
    board = ChessBoard(10, [knight1, knight2, knight3])
    assert (board.knights_checking()) == [], "Should find . Test 3 failed."
    print("Test 3 completed successfully")
    board.plot()
    board.plot_checking()

unit_test1()
unit_test2()
unit_test3()