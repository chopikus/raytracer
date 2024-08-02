from __future__ import annotations
from typing import Tuple
from dataclasses import dataclass
import random
import numpy as np
import numpy.typing as npt

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

    def __mul__(self, t: FloatArray) -> Vec3Array:
        return Vec3Array(self.x * t, self.y * t, self.z * t)

    def __truediv__(self, t: FloatArray) -> Vec3Array:
        return self * (1 / t)

    def __matmul__(self, v: Vec3Array) -> FloatArray:
        return self.x * v.x + self.y * v.y + self.z * v.z

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
    def repeat(p: Tuple[float, float, float], count: int) -> Vec3Array:
        xs: FloatArray = np.repeat(p[0], count)
        ys: FloatArray = np.repeat(p[1], count)
        zs: FloatArray = np.repeat(p[2], count)
        return Vec3Array(xs, ys, zs)

@dataclass
class PointArray(Vec3Array):
    """ Invariants:
        * x.ndim == y.ndim == z.ndim == 1
        * x.size == y.size == z.size
    """
    @staticmethod
    def repeat(p: Tuple[float, float, float], count: int) -> PointArray:
        return Vec3Array.repeat(p, count).point_array()


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
