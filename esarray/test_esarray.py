from esarray import ESArray


def test_esarray_constructor():
    a = ESArray([1, 2, 3, 4])
    assert isinstance(a, list)
    assert len(a) == 4
    assert a[0] == 1
    assert a[1] == 2
    assert a[2] == 3
    assert a[3] == 4


def test_esarray_join_ints():
    a = ESArray([1, 2, 3, 4])
    assert a.join("&") == "1&2&3&4"
    assert a.join("___") == "1___2___3___4"


def test_esarray_join_strs():
    a = ESArray("ABCDE")
    assert a.join("&") == "A&B&C&D&E"
    assert a.join("___") == "A___B___C___D___E"


def test_esarray_join_tuples():
    a = ESArray([(), (1, 2, 3)])
    assert a.join("&") == "()&(1, 2, 3)"
    assert a.join("___") == "()___(1, 2, 3)"


def test_esarray_every_simple():
    a = ESArray([1, 2, 3, 4])
    assert a.every(lambda v: v > 2) == False
    assert a.every(lambda v: v > 0) == True
    assert ESArray(["a", "z"]).every(lambda v: v.islower()) == True
    assert ESArray(["a", "Z"]).every(lambda v: v.islower()) == False


def test_esarray_every_bool():
    assert ESArray([1, 2, 3, 4]).every(lambda v: v) == True
    assert ESArray([0, 1]).every(lambda v: v) == False
    assert ESArray(["test", ""]).every(lambda v: v.islower()) == False


def test_esarray_for_each():
    seen = []

    def collect(x):
        seen.append(x)

    a = ESArray([4, 3, 2, 1])
    a.for_each(collect)
    assert seen == [4, 3, 2, 1]


def test_esarray_for_each_return():
    a = ESArray([4, 3, 2, 1])
    assert a.for_each(lambda x: x) is None


def test_esarray_flatten_simple():
    y = ESArray([[3, 4], 5, [6, 7]])
    flat = y.flatten()
    assert flat == [3, 4, 5, 6, 7]


def test_esarray_flatten():
    y = ESArray([[3, 4], [5], 6, [7, [8, [9, 10]]]])
    flat = y.flatten()
    assert flat == [3, 4, 5, 6, 7, 8, 9, 10]


def test_esarray_flatten_no_mod():
    y = ESArray([[3, 4], [5], 6, [7, [8, [9, 10]]]])
    flat = y.flatten()
    assert y[0] == [3, 4]
    assert y[1] == [5]
    assert y[2] == 6
    assert y[3] == [7, [8, [9, 10]]]
