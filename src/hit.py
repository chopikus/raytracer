from dataclasses import dataclass
from typing import Optional, List
from geom import *

@dataclass
class HitRecord:
    p: Point
    normal: Vec3
    t: float
    frontFace: bool

@dataclass
class Hittable:
    """Returns a record of the earlist hit of ray r.
    Returned HitRecord must have t surrounded in the interval i.
    If such hit wasn't found, None is returned.
    """
    def hit(self, r: Ray, i: Interval) -> Optional[HitRecord]:
        raise NotImplementedError

@dataclass
class HittableList(Hittable):
    hittables: List[Hittable]

    def hit(self, r: Ray, i: Interval) -> Optional[HitRecord]:
        result: Optional[HitRecord] = None
        cur: float = i.max_

        for h in self.hittables:
            hitRes = h.hit(r, Interval(i.min_, cur))
            if hitRes is not None:
                result = hitRes
                cur = hitRes.t

        return result

