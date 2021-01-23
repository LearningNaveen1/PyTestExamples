import pytest

'''
    In this file we will check for multiple ways to call fixtures
        a. Simple way which is already covered with other examples.
        b. Another way is @pytest.mark.usefixtures("<<FIXTURE_NAME>>")
            while using b method we don't need to define explicit way for fixture. 
'''

@pytest.fixture(scope="module")
def get_NameCheck():
    global test_a
    test_a = 100
    return test_a

@pytest.mark.usefixtures("get_NameCheck")
def test_get_Names():
    print(type(get_NameCheck))
    print(get_NameCheck)
    assert get_NameCheck == 1000

