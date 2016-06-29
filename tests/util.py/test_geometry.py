
import math
import random

from noobcraft.util.geometry import Vec2


def test_vec2_init_empty():
    '''
    The vec2 constructor should produce a null vector without arguments.
    '''
    v = Vec2()
    assert v.x == 0 and  v.y == 0

def test_vec2_init_coordinates():
    '''
    The vec2 constructor should produce a valid vector from coordinates.
    '''
    v = Vec2(2, 3)
    assert v.x == 2 and v.y == 3

def test_vec2_init_direction(almost):
    '''
    The vec2 constructor should produce a valid vector from direction and magnitude.
    '''
    v = Vec2(direction=0, magnitude=1)
    assert almost(v.x, 1) and almost(v.y, 0)
    v = Vec2(direction=math.pi / 2, magnitude=2)
    assert almost(v.x, 0) and almost(v.y, 2)
    v = Vec2(direction=math.pi, magnitude=3)
    assert almost(v.x, -3) and almost(v.y, 0)
    v = Vec2(direction=3 * math.pi / 2, magnitude=4)
    assert almost(v.x, 0) and almost(v.y, -4)

def test_vec2_abs(almost):
    '''
    The abs function should produce the magnitude of a vector.
    '''
    for i in range(100):
        m = random.uniform(0, 1)
        v = Vec2(direction=random.uniform(0, 2 * math.pi), magnitude=m)
        assert almost(abs(v), m)

def test_vec2_add(almost):
    '''
    Two instances of vec2 should produce the result of geometric addition upon addition.
    '''
    o = Vec2(1, 1)
    for i in range(100):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        v = o + Vec2(x, y)
        assert isinstance(v, Vec2) and almost(v.x, o.x + x) and almost(v.y, o.y + y)

def test_vec2_sub(almost):
    '''
    Two instances of vec2 should produce the result of geometric subtraction upon subtraction.
    '''
    o = Vec2(1, 1)
    for i in range(100):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        v = o - Vec2(x, y)
        assert isinstance(v, Vec2) and almost(v.x, o.x - x) and almost(v.y, o.y - y)

def test_vec2_mul_scalar(almost):
    '''
    An instance of vec2 multiplied by a scalar should multiply its magnitude.
    '''
    for i in range(100):
        m = random.uniform(0, 1)
        p = random.uniform(0, 1)
        v = Vec2(direction=random.uniform(0, 2 * math.pi), magnitude=m)
        assert isinstance(v, Vec2) and almost(abs(v * p), m * p)

def test_vec2_mul_dot():
    '''
    An instance of vec2 multiplied by an instance of vec2 should produce the dot product.
    '''
    assert Vec2(2, 4) * Vec2(5, 6) == 34

def test_vec2_div_scalar(almost):
    '''
    An instance of vec2 divided by a scalar should reduce its magnitude to a fraction.
    '''
    for i in range(100):
        m = random.uniform(0, 1)
        p = random.uniform(0, 1)
        v = Vec2(direction=random.uniform(0, 2 * math.pi), magnitude=m)
        assert isinstance(v, Vec2) and almost(abs(v / p), m / p)

