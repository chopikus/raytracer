import unittest
from geom import Vec3, Interval
import random

class TestVec3(unittest.TestCase):
    def test_add_matmul(self) -> None:
        v: Vec3 = Vec3(1.0, 2.0, 3.0)
        w: Vec3 = Vec3(3.0, 2.0, 1.0)
        z: Vec3 = v + w
        s: float = v @ w
        self.assertEqual(z, Vec3(4.0, 4.0, 4.0))
        self.assertEqual(s, 10.0)

    def test_random_on_unit_sphere(self) -> None:
        random.seed(1)
        v: Vec3 = Vec3.random_on_unit_sphere()
        self.assertAlmostEqual(1.0, v.len())

    def test_random_on_unit_hemisphere(self) -> None:
        random.seed(2)
        v: Vec3 = Vec3(1.0, 0.0, 0.0)
        w: Vec3 = Vec3.random_on_unit_hemisphere(v)
        self.assertTrue(v @ w >= 0.0)

class TestInterval(unittest.TestCase):
    def test_empty_contains(self) -> None:
        x = Interval.empty()
        self.assertFalse(x.contains(0))

    def test_universe_contains(self) -> None:
        x = Interval.universe()
        self.assertTrue(x.contains(0))

    def test_contains_surrounds(self) -> None:
        x = Interval(0.0, 0.5)
        self.assertTrue(x.contains(0.0))
        self.assertTrue(x.contains(0.25))
        self.assertTrue(x.contains(0.5))
    
    def test_surrounds(self) -> None:
        x = Interval(0.0, 0.5)
        self.assertFalse(x.surrounds(0.0))
        self.assertTrue(x.surrounds(0.25))
        self.assertFalse(x.surrounds(0.5))
