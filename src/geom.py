from __future__ import annotations
from math import sqrt
from dataclasses import dataclass
import random

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
            l = sqrt(x*x + y*y + z*z)
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
        return sqrt(self.len_squared())

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

@dataclass
class Ray:
    origin: Point
    direction: Vec3
    
    def at(self, t: float) -> Point:
        return Point.from_(self.direction * t + self.origin)


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
