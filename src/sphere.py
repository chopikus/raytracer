from dataclasses import dataclass
from geom import *
from hit import *
import numpy as np

FARAWAY = 1.0e9

@dataclass
class Sphere(Hittable):
    center: Point
    radius: float
    
    def hit(self, r: Ray) -> float:
        orig = r.origin
        dir = r.direction
        OC = self.center - orig

        A = dir.len_squared()
        B = -2.0 * (OC @ dir)
        C = OC.len_squared() - self.radius * self.radius
        D = B*B - 4*A*C
        
        t1: float = np.where(D >= 0, (-B - np.sqrt(D)) / (2 * A), FARAWAY)
        t2: float = np.where(D >= 0, (-B - np.sqrt(D)) / (2 * A), FARAWAY)
        return np.where(t1 < t2, t1, t2)
