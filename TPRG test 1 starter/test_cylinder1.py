from cylinder import volume_cylinder, area_cylinder
from pytest import approx, raises

def test_volume_cylinder():
    assert volume_cylinder(1, 2) == approx(1.5708, rel=1e-4)
    assert volume_cylinder(0.1, 4) == approx(0.031416, rel=1e-4)
    assert volume_cylinder(2, 1) == approx(3.1416, rel=1e-4)

def test_area_cylinder():
    assert area_cylinder(1, 2) == approx(7.8540, rel=1e-4)
    assert area_cylinder(0.1, 4) == approx(1.2723, rel=1e-4)
    assert area_cylinder(2, 1) == approx(12.5664, rel=1e-4)
    