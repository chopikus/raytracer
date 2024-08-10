from util import *
from camera import *
from sphere import *

if __name__ == '__main__':
    hittables: List[Sphere] = []
    hittables.append(Sphere(center=Point(0.0, 0.0, -1.0), radius=0.5))
    #hittables.append(Sphere(center=Point(0.0, -100.5, -1.0), radius=100.0))

    world = hittables
    camera = Camera(16.0 / 9.0, 400, 10, 1)
    camera.render(world)
