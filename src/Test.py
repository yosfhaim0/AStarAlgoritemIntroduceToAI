import state


def test_colume():
    assert state.columnShouldBe([[1, 8, 3, 6, 5, 4, 7, 2, 0], ""], 5) == 2, "Should be 2"
    assert state.columnShouldBe([[1, 8, 3, 6, 5, 4, 7, 2, 0], ""], 8) == 2, "Should be 6"
    assert state.columnShouldBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 15) == 3, "Should be 6"
    assert state.columnShouldBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 5) == 1, "Should be 6"
    assert state.columnShouldBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 14) == 2, "Should be 6"
    assert state.columnActualBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 0) == 2, "Should be 6"
    assert state.columnActualBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 2) == 3, "Should be 6"
    assert state.columnActualBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 15) == 1, "Should be 6"
    assert state.columnActualBe([[1, 8, 3, 6, 5, 4, 7, 2, 0], ""], 8) == 1, "Should be 6"
    assert state.columnActualBe([[1, 8, 3, 6, 5, 4, 7, 2, 0], ""], 8) == 1, "Should be 6"


def test_row():
    assert state.rowShouldBe([[1, 8, 3, 6, 5, 4, 7, 2, 0], ""], 8) == 2, "Should be 6"
    assert state.rowShouldBe([[1, 8, 3, 6, 5, 4, 7, 2, 0], ""], 2) == 0, "Should be 6"
    assert state.rowShouldBe([[1, 8, 3, 6, 5, 4, 7, 2, 0], ""], 3) == 1, "Should be 6"
    assert state.rowShouldBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 2) == 0, "Should be 6"
    assert state.rowShouldBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 5) == 1, "Should be 6"
    assert state.rowShouldBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 15) == 3, "Should be 6"
    assert state.rowShouldBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 11) == 2, "Should be 6"
    assert state.rowActualBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 15) == 0, "Should be 6"
    assert state.rowActualBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 0) == 3, "Should be 6"
    assert state.rowActualBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 2) == 3, "Should be 6"
    assert state.rowActualBe([[1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 2], ""], 14) == 3, "Should be 6"
    assert state.rowActualBe([[1, 15, 3, 4, 5, 6, 7, 14, 9, 10, 11, 12, 13, 8, 0, 2], ""], 14) == 1, "Should be 6"


def hdistance_test():
    assert state.hdistance([[8, 1, 3, 2, 6, 5, 0, 4, 7], ""]) == 11, "Should be 11"
    assert state.hdistance([[7, 4, 0, 5, 6, 2, 3, 1, 8], ""]) == 12, "Should be 11"
    assert state.hdistance([[0, 1, 2, 6, 7, 8, 3, 4, 5], ""]) == 6, "Should be 6"
    assert state.hdistance([[0, 3, 6, 1, 4, 7, 2, 5, 8], ""]) == 8, "Should be 8"
    assert state.hdistance([[0, 3, 4, 6, 1, 5, 7, 8, 2], ""]) == 8, "Should be 8"
    assert state.hdistance([[4, 3, 7, 5, 8, 6, 1, 0, 2], ""]) == 15, "Should be 8"
    assert state.hdistance([[1, 15, 3, 4, 5, 6, 7, 14, 9, 10, 11, 12, 13, 8, 0, 2], ""]) == 27, "Should be 27"


if __name__ == "__main__":
    test_colume()
    test_row()
    hdistance_test()
    print("Everything passed")
