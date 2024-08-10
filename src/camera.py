from util import *
from geom import *
from sphere import *
import numpy as np
from numba.typed import List # type: ignore

@jitclass
class Camera:
    image_width: int
    image_height: int
    center: Vec3 # actually point
    p00: Vec3 # actually point
    dh: Vec3
    dv: Vec3
    pixel_samples: int
    depth: int
    samples_one_time: int

    def __init__(self, aspect_ratio: float, image_width: int, pixel_samples: int, samples_per_one_time: int) -> None:
        self.samples_one_time = samples_per_one_time
        self.depth = 10
        self.pixel_samples = pixel_samples
        self.image_width = image_width
        self.image_height = int(image_width / aspect_ratio)

        # Geometric units
        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (self.image_width / self.image_height)

        self.center: Point = Vec3(0.0, 0.0, 0.0)
        h = Vec3(viewport_width, 0.0, 0.0)
        v = Vec3(0.0, -viewport_height, 0.0)
        self.dh = h / self.image_width
        self.dv = v / self.image_height

        viewport_center: Point = (self.center - Vec3(0.0, 0.0, focal_length))
        viewport_start: Point = (viewport_center - v/2 - h/2)
        self.p00: Point = (viewport_start + (self.dv/2) + (self.dh/2))

    def render_rays(self, rays: RayArray, sphere: Sphere) -> FloatArray:
        print(f"calling render_rays for {rays.size()} rays")

        hits: FloatArray = np.minimum.reduce(sphere.hit(rays))
        unit_directions: Vec3Array = rays.direction.unit()
        ry = unit_directions.y
        a = (ry + 1.0) / 2.0
        result_size = rays.size()

        # makes result_size columns of (r, g, b)^T
        column_rep = lambda r,g,b: np.array([r, g, b]) \
                                     .repeat(result_size) \
                                     .reshape((-1, result_size))

        bg = column_rep(1.0, 1.0, 1.0) * (1.0 - a) + \
             column_rep(0.5, 0.7, 1.0) * a
        
        red = column_rep(1.0, 0.0, 0.0)

        return np.where(hits == np.inf, bg, red)

    def render_pixels(self, sphere: Sphere, pixel_samples: int) -> FloatArray:
        ray_count = self.image_height * self.image_width * pixel_samples
        centers: PointArray = Vec3Array_repeat(self.center, ray_count)
        x_offsets = np.random.uniform(-0.5, 0.5, ray_count)
        y_offsets = np.random.uniform(-0.5, 0.5, ray_count)

        """
        Generating xs and ys
         Example:
          width = 2
          height = 3
          pixel_samples = 2
          0. xfirst = [0, 0, 0, 1, 1, 1]
          1. xs = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
          2. ys = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
        """
        xs: FloatArray = np.zeros(ray_count)
        ys: FloatArray = np.zeros(ray_count)
        zs: FloatArray = np.zeros(ray_count)
        index: int = 0
        for _ in range(pixel_samples):
            for c in range(self.image_width * self.image_height):
                xs[index] = c / self.image_height
                ys[index] = c % self.image_height
                index += 1

        vecs: Vec3Array = Vec3Array(xs + x_offsets, ys + y_offsets, zs)
        dhs: Vec3Array = Vec3Array_repeat(self.dh, ray_count)
        dvs: Vec3Array = Vec3Array_repeat(self.dv, ray_count)

        p00_repeated: PointArray = Vec3Array_repeat(self.p00, ray_count)
        ray_directions = p00_repeated + vecs.mul(dhs + dvs) - centers

        rays = RayArray(centers, ray_directions)
        colors = self.render_rays(rays, sphere)

        print(colors.size, pixel_samples)
        colors_splitted = np.split(colors, pixel_samples, axis=1)
        return np.add.reduce(colors_splitted) / pixel_samples
        
    def render(self, sphere: Sphere) -> None:
        colors = np.zeros((3, self.image_width * self.image_height))
        times = self.pixel_samples // self.samples_one_time
        #for _ in range(times):
        #    colors += self.render_pixels(sphere, self.samples_one_time)
        colors /= times

        """
        img = Image(self.image_width, self.image_height)

        i: int = 0
        for x in range(self.image_width):
            for y in range(self.image_height):
                c = Color(colors[0][i], colors[1][i], colors[2][i])
                img.set_pixel(x, y, c)
                i += 1

        img.save("output.png")
        """
