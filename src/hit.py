from dataclasses import dataclass
from typing import Optional, Sequence
from geom import *

@dataclass
class HitRecordArray:
    p: Point
    normal: Vec3
    t: float
    front_face: bool

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
    hittables: Sequence[Hittable]

    def hit(self, r: Ray, i: Interval) -> Optional[HitRecord]:
        result: Optional[HitRecord] = None
        cur: float = i.max_

        for h in self.hittables:
            hit_res = h.hit(r, Interval(i.min_, cur))
            if hit_res is not None:
                result = hit_res
                cur = hit_res.t

        return result

