from dataclasses import dataclass
from geom import *
from hit import *
from math import sqrt

@dataclass
class Sphere(Hittable):
    center: Point
    radius: float
    
    def hit(self, r: Ray, i: Interval) -> Optional[HitRecord]:
        orig = r.origin
        dir = r.direction
        OC = self.center - orig

        A = dir.len_squared()
        B = -2.0 * (OC @ dir)
        C = OC.len_squared() - self.radius * self.radius
        D = B*B - 4*A*C

        if D < 0:
            return None
        sqrt_d = sqrt(D)

        """Returning minimum time t that is in (tMin, tMax) range.
        """
        t1 = (-B - sqrt_d) / (2 * A)
        t2 = (-B + sqrt_d) / (2 * A)
        
        t: float
        if i.surrounds(t1):
            t = t1
        elif i.surrounds(t2):
            t = t2
        else:
            return None

        p: Point = r.at(t)
        outward_normal: Vec3 = (p - self.center).unit()
        front_face: bool = (r.direction @ outward_normal) <= 0.0
        normal: Vec3 = outward_normal if front_face else -outward_normal

        return HitRecord(p, normal, t, front_face)
