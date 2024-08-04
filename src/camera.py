from util import *
from geom import *
from sphere import *
import numpy as np
from typing import List

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

    # temporary method
    def decide_hit(self, rays: RayArray, world: List[Sphere]) -> FloatArray:
        hits: List[FloatArray] = []
        for sphere in world:
            arr = sphere.hit(rays)
            np.nan_to_num(arr, copy=False, nan=float('inf'))
            hits.append(arr)
        
        min_hit = hits[0]
        for i in range(1, len(hits)):
            min_hit = np.minimum(min_hit, hits[i])

        return min_hit

    def render_rays(self, r: RayArray, world: List[Sphere]) -> FloatArray:
        def f(arr: FloatArray) -> FloatArray:
            hit_time, rx, ry, rz = (arr[0], arr[1], arr[2], arr[3])
            a = (ry + 1.0) / 2.0
            start_color = np.array([1.0, 1.0, 1.0])
            end_color = np.array([0.5, 0.7, 1.0])
            if hit_time == float('inf'):
                return start_color * (1.0 - a) + end_color * a
            return np.array([1.0, 0.0, 0.0])

        hits: FloatArray = self.decide_hit(r, world)        
        unit_directions: Vec3Array = r.direction.unit()
        s = np.vstack((hits, unit_directions.x, unit_directions.y, unit_directions.z))
        result = np.apply_along_axis(f, 0, s)
        
        return result

    def render_pixel(self, world: List[Sphere], x: int, y: int) -> Color:
        xs = np.array([])
        ys = np.array([])
        zs = np.array([])
        centers = PointArray.repeat(self.center, self.pixel_samples)
        
        for sample in range(self.pixel_samples):
            offset_x = random.uniform(-0.5, 0.5)
            offset_y = random.uniform(-0.5, 0.5)

            ray_direction: Vec3 = self.p00 \
                                  + self.dh * (x + offset_x) \
                                  + self.dv * (y + offset_y) \
                                  - self.center

            xs = np.append(xs, ray_direction.x)
            ys = np.append(ys, ray_direction.y)
            zs = np.append(zs, ray_direction.z)

        rays_directions = Vec3Array(xs, ys, zs)
        rays = RayArray(centers, rays_directions)
        colors = self.render_rays(rays, world)

        colors_summed = np.sum(colors, axis = 1) / self.pixel_samples
        # print(colors, colors_summed)
        return Color(colors_summed[0], colors_summed[1], colors_summed[2])

    def render(self, world: List[Sphere]) -> None:
        img = Image(self.image_width, self.image_height)

        for x in range(self.image_width):
            for y in range(self.image_height):
                c = self.render_pixel(world, x, y)
                img.set_pixel(x, y, c)

        img.save("output.png")
