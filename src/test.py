import unittest
from geom import Vec3

class TestVec3(unittest.TestCase):
    def test_add_matmul(self):
        v: Vec3 = Vec3(1.0, 2.0, 3.0)
        w: Vec3 = Vec3(3.0, 2.0, 1.0)
        z: Vec3 = v + w
        s: float = v @ w
        self.assertEqual(z, Vec3(4.0, 4.0, 4.0))
        self.assertEqual(s, 10.0)
