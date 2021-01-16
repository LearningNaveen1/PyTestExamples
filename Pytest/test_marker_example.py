import pytest

def test_m1():
    a =3
    b=4
    assert a+1 == b, "Failed"

def test_m2():
    assert True

def test_m3():
    assert False

@pytest.mark.login
def test_login_file1():
    print("Inside file1 login")

