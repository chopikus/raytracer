from dataclasses import dataclass
from typing import Tuple
from geom import *
import numpy as np

@dataclass
class Sphere:
    center: Point
    radius: float
    
    """ Computes hits for multiple rays at the same time.
    """
    def hit(self, r: RayArray) -> FloatArray:
        origins: PointArray = r.origin
        directions: Vec3Array = r.direction

        radiuses = np.repeat(self.radius, r.size())
        centers = PointArray.repeat(self.center, r.size())

        ocs = centers - origins

        type Arr = FloatArray
        A: Arr = directions.len_squared()
        B: Arr = -2.0 * (ocs @ directions)
        C: Arr = ocs.len_squared() - radiuses * radiuses
        D: Arr = B*B - 4*A*C
    
        cond = D >= 0 #BoolArray(fix later)
        sq = np.sqrt(np.maximum(D, 0))
        t1: Arr = np.where(cond, (-B - sq) / (2 * A), np.nan)
        t2: Arr = np.where(cond, (-B + sq) / (2 * A), np.nan)

        # np.isnan(t1) == np.isnan(t2) always since the condition is the same
        choose_t1 = (~np.isnan(t1)) & (t1 <= t2)
        choose_t2 = (~np.isnan(t1)) & (t1 > t2)

        return np.select([choose_t1, choose_t2], [t1, t2], np.nan)
