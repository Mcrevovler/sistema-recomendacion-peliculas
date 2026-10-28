from src.logica import y, o, no, implica, bicond


def test_y():
    assert y(True, True) is True
    assert y(True, False) is False
    assert y(False, True) is False
    assert y(False, False) is False


def test_o():
    assert o(True, True) is True
    assert o(True, False) is True
    assert o(False, True) is True
    assert o(False, False) is False


def test_no():
    assert no(True) is False
    assert no(False) is True


def test_implica():
    assert implica(True, True) is True
    assert implica(True, False) is False
    assert implica(False, True) is True
    assert implica(False, False) is True


def test_bicond():
    assert bicond(True, True) is True
    assert bicond(True, False) is False
    assert bicond(False, True) is False
    assert bicond(False, False) is True