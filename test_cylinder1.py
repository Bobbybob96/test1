"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 202x Test 1

test_cylinder1.py

Thomas Heine
100777741
"""

from cylinder1 import volume_cylinder, area_cylinder
from pytest import approx, raises

def test_volume_cylinder():
    assert volume_cylinder(1, 2) == approx(1.5708, rel=1e-4)
    assert volume_cylinder(0.1, 4) == approx(0.031416, rel=1e-4)
    assert volume_cylinder(2, 1) == approx(3.1416, rel=1e-4)

def test_area_cylinder():
    assert area_cylinder(1, 2) == approx(7.8540, rel=1e-4)
    assert area_cylinder(0.1, 4) == approx(1.2723, rel=1e-4)
    assert area_cylinder(2, 1) == approx(12.5664, rel=1e-4)

def test_volume_negative_height():
    with pytest.raises(ValueError):
        volume_cylinder(1, -2)

def test_area_negative_height():
    with pytest.raises(ValueError):
        area_cylinder(1, -2)