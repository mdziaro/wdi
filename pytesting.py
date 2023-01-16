from zad5_7 import *
import pytest
def test_py1():
    board = ChessBoard(10, [ChessKnight((0, 0)), ChessKnight((2, 1)), ChessKnight((5, 2))])
    assert board.knights_checking() == [((0, 0), (2, 1))], "Should find ((0, 0), (2, 1)). Test failed"
def test_py2():
    board = ChessBoard(10, [ChessKnight((0, 0)), ChessKnight((2, 1)), ChessKnight((1, 2))])
    assert board.knights_checking() == [((0, 0), (2, 1)), ((0, 0), (1, 2))], "Should find ((0, 0), (2, 1)), ((0, 0), (1, 2)). Test failed"
def test_py3():
    board = ChessBoard(10, [ChessKnight((0, 0)), ChessKnight((2, 2)), ChessKnight((3, 3))])
    assert board.knights_checking() == [], "Should find . Test failed"