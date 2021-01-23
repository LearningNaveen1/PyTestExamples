import pytest

'''
    Scope of fixture can be defined as function, class, module, package or session (f,c,m,p,s)
'''

@pytest.fixture(scope="module")
def samplevalue1():
    a = 100
    return a
@pytest.fixture(scope="module")
def samplevalue2():
    b = 200
    return b

