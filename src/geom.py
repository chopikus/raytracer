from __future__ import annotations
from dataclasses import dataclass
import random
import numpy as np
import numpy.typing as npt
import math

type FloatArray = npt.NDArray[np.float64]

""" Class for operating on a bunch of vectors at the same time.
"""
@dataclass
class Vec3Array:
    """ Invariants:
        * x.ndim == y.ndim == z.ndim == 1
        * x.size == y.size == z.size
    """
    x: FloatArray
    y: FloatArray
    z: FloatArray
   
    def __neg__(self) -> Vec3Array:
        return Vec3Array(-self.x, -self.y, -self.z)

    def __add__(self, v: Vec3Array) -> Vec3Array:
        return Vec3Array(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v: Vec3Array) -> Vec3Array:
        return Vec3Array(self.x - v.x, self.y - v.y, self.z - v.z)

    def mul(self, v: Vec3Array) -> Vec3Array:
        return Vec3Array(self.x * v.x, self.y * v.y, self.z * v.z)
    
    def __mul__(self, t: FloatArray) -> Vec3Array:
        return Vec3Array(self.x * t, self.y * t, self.z * t)

    def __truediv__(self, t: FloatArray) -> Vec3Array:
        return self * (1 / t)

    def __matmul__(self, v: Vec3Array) -> FloatArray:
        return self.x * v.x + self.y * v.y + self.z * v.z
    
    def __eq__(self, v: object) -> bool:
        if not isinstance(v, Vec3Array):
            return NotImplemented
        
        return np.allclose(self.x, v.x) \
           and np.allclose(self.y, v.y) \
           and np.allclose(self.z, v.z)

    def len(self) -> FloatArray:
        return np.sqrt(self.len_squared())

    def len_squared(self) -> FloatArray:
        return self.x * self.x + self.y * self.y + self.z * self.z
     
    def unit(self) -> Vec3Array:
        return self / self.len()

    def point_array(self) -> PointArray:
        return PointArray(self.x, self.y, self.z)

    def size(self) -> int:
        return self.x.size
    
    @staticmethod
    def repeat(p: Vec3, count: int) -> Vec3Array:
        xs: FloatArray = np.repeat(p.x, count)
        ys: FloatArray = np.repeat(p.y, count)
        zs: FloatArray = np.repeat(p.z, count)
        return Vec3Array(xs, ys, zs)

@dataclass
class PointArray(Vec3Array):
    """ Invariants:
        * x.ndim == y.ndim == z.ndim == 1
        * x.size == y.size == z.size
    """
    @staticmethod
    def repeat(p: Vec3, count: int) -> PointArray:
        return Vec3Array.repeat(p, count).point_array()
    
    def __eq__(self, p: object) -> bool:
        return Vec3Array.__eq__(self, p)

@dataclass
class RayArray:
    """ Invariants:
        * origin.x.size == direction.x.size
        * origin.y.size == direction.y.size
        * origin.z.size == direction.z.size
        * PointArray invariants for origin
        * Vec3Array invariants for direction
    """
    origin: PointArray
    direction: Vec3Array
    
    def at(self, t: FloatArray) -> PointArray:
        return (self.direction * t + self.origin).point_array()

    def size(self) -> int:
        return self.origin.size()

@dataclass
class Interval:
    min_: float
    max_: float
    
    @staticmethod
    def empty() -> Interval:
        return Interval(float('inf'), float('-inf'))

    @staticmethod
    def universe() -> Interval:
        return Interval(float('-inf'), float('inf'))

    def size(self) -> float:
        return self.max_ - self.min_

    def contains(self, x: float) -> bool:
        return (x >= self.min_ and x <= self.max_)

    def surrounds(self, x: float) -> float:
        return (x > self.min_ and x < self.max_)

@dataclass
class Vec3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    """Returns the uniformly distributed vector on a unit sphere.
       The returned vector is a unit vector.
    """
    @staticmethod
    def random_on_unit_sphere() -> Vec3:
        x, y, z, l = 0.0, 0.0, 0.0, 0.0
        while l == 0.0:
            x = random.gauss(0, 1)
            y = random.gauss(0, 1)
            z = random.gauss(0, 1)
            l = math.sqrt(x*x + y*y + z*z)
        return Vec3(x/l, y/l, z/l)
    
    """Returns the uniformly distributed vector on a unit sphere in the same hemisphere as vector `v`.
       Note: `v` is not required to be a unit vector.
       The returned vector is a unit vector.
    """
    @staticmethod
    def random_on_unit_hemisphere(v: Vec3) -> Vec3:
        r = Vec3.random_on_unit_sphere()
        if v @ r > 0.0:
            return r
        else:
            return -r
    
    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, v: Vec3) -> Vec3:
        return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v: Vec3) -> Vec3:
        return Vec3(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, t: float) -> Vec3:
        return Vec3(self.x * t, self.y * t, self.z * t)

    def __truediv__(self, t: float) -> Vec3:
        return self * (1 / t)

    def __matmul__(self, v: Vec3) -> float:
        return self.x * v.x + self.y * v.y + self.z * v.z

    def len(self) -> float:
        return math.sqrt(self.len_squared())

    def len_squared(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z
     
    def unit(self) -> Vec3:
        return self / self.len()

    def point(self) -> Point:
        return Point(self.x, self.y, self.z)

@dataclass
class Point(Vec3):
    pass

    @staticmethod
    def from_(v: Vec3) -> Point:
        return Point(v.x, v.y, v.z)
