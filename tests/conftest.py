
import pytest


@pytest.fixture(scope='session')
def almost():
    '''
    This fixture provides a function to check for almost-equality of floats.
    '''
    def compare_func(x, y):
        return abs(x - y) < 0.00000001
    return compare_func

