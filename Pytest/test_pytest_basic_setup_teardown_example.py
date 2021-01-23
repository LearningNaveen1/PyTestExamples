import pytest

'''
    Typical setup and tearsown examples as compared with other languages as well
    Constraints with this - 
        a. Syntax has to be mentioned as below and module is also needs to be provided.
        b. Any change in the name will fail to perform the setup and teardown actions.
           
'''


def setup_module(module):
    global a
    a= 100

def test_value_of_a():
    assert a == 100, "Working fine"

def test_value_of_a_failed_scenario():
    assert a+1 == 100, "Value of a doesn't match a"

def teardown_module(module):
    a = 0
    print('HELOO')