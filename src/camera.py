from util import *
from hit import *

class Camera:
    image_width: int
    image_height: int
    center: Point
    p00: Point
    dh: Vec3
    dv: Vec3
    pixel_samples: int
    depth: int

    def __init__(self, aspect_ratio: float, image_width: int, pixel_samples: int) -> None:
        self.depth = 10
        self.pixel_samples = pixel_samples
        self.image_width = image_width
        self.image_height = int(image_width / aspect_ratio)

        # Geometric units
        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (self.image_width / self.image_height)

        self.center = Point(0.0, 0.0, 0.0)
        h = Vec3(viewport_width, 0.0, 0.0)
        v = Vec3(0.0, -viewport_height, 0.0)
        self.dh = h / self.image_width
        self.dv = v / self.image_height

        viewport_center = (self.center - Vec3(0.0, 0.0, focal_length)).point()
        viewport_start = (viewport_center - v/2 - h/2).point()
        self.p00 = (viewport_start + (self.dv/2) + (self.dh/2)).point()
