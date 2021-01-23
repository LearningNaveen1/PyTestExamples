import pytest

'''
    using annotation we can create a fixture
'''
@pytest.fixture()
def samplevalue():
    global a,b
    a=100
    b=200
    return a,b


def test_fixture(samplevalue):
    assert samplevalue[0] == 100
    assert samplevalue[1] == 200

