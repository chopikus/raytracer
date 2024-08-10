from util import *
from camera import *
from sphere import *
from numba import jit # type: ignore

@jit
def main_func() -> None:
    #hittables: List[Sphere] = []
    #hittables.append(Sphere(center=Vec3(0.0, 0.0, -1.0), radius=0.5))
    #hittables.append(Sphere(center=Point(0.0, -100.5, -1.0), radius=100.0))

    #world = hittables
    camera = Camera(16.0 / 9.0, 1000, 250, 1)
    camera.render(Sphere(Vec3(0.0, 0.0, -1.0), 0.5))

if __name__ == '__main__':
    main_func()
    
