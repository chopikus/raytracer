import unittest
from geom import *
import random
import numpy as np
import numpy.typing as npt

class TestVec3Array(unittest.TestCase):
    def test_add_matmul(self) -> None:
        arr = np.array
        v: Vec3Array = Vec3Array(arr([1.0]), arr([2.0]), arr([3.0]))
        w: Vec3Array = Vec3Array(arr([3.0]), arr([2.0]), arr([1.0]))
        z: Vec3Array = v + w
        s: FloatArray = v @ w
        self.assertEqual(z, Vec3Array(arr([4.0]), arr([4.0]), arr([4.0])))
        self.assertEqual(s, arr([10.0]))

    """
    def test_random_on_unit_sphere(self) -> None:
        random.seed(1)
        v: Vec3Array = Vec3Array.random_on_unit_sphere()
        self.assertAlmostEqual(1.0, v.len())

    def test_random_on_unit_hemisphere(self) -> None:
        random.seed(2)
        v: Vec3Array = Vec3Array(1.0, 0.0, 0.0)
        w: Vec3Array = Vec3Array.random_on_unit_hemisphere(v)
        self.assertTrue(v @ w >= 0.0)
    """

    def test_unit(self) -> None:
        arr = np.array
        v: Vec3Array = Vec3Array(arr([0.0, 0.0, 3.0, 3.0, 0.0]), #X
                                 arr([0.0, 2.0, 0.0, 0.0, 5.0]), #Y
                                 arr([1.0, 0.0, 0.0, 4.0, 0.0])) #Z 
        
        w: Vec3Array = Vec3Array(arr([0.0, 0.0, 1.0, 0.6, 0.0]), #X
                                 arr([0.0, 1.0, 0.0, 0.0, 1.0]), #Y
                                 arr([1.0, 0.0, 0.0, 0.8, 0.0])) #Z 
        
        self.assertTrue(v.unit() == w)


class TestRay(unittest.TestCase):
    def test_at(self) -> None:
        arr = np.array
        origins: PointArray = Vec3Array(arr([0.0, 0.0]), #X
                                         arr([0.0, 0.0]), #Y
                                         arr([0.0, 0.0])) #Z

        directions: Vec3Array = Vec3Array(arr([1.0, 2.0]), #X
                                          arr([3.0, 4.0]), #Y
                                          arr([5.0, 6.0])) #Z
        
        ts: FloatArray = arr([100.0, 5.0])

        expected: PointArray = Vec3Array(arr([100.0, 10.0]),
                                          arr([300.0, 20.0]),
                                          arr([500.0, 30.0]))
        
        computed: PointArray = RayArray(origins, directions).at(ts)
        
        self.assertTrue(expected == computed)

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
