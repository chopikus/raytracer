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

    def ray_color(self, r: Ray, world: Hittable, depth: int) -> Color:
        if depth <= 0:
            return Color(0.0, 0.0, 0.0)

        hr: Optional[HitRecord] = world.hit(r, Interval(0.0001, float('inf')))
        if hr is not None:
            normal = hr.normal
            random_vector = Vec3.random_on_unit_hemisphere(normal)
            
            return self.ray_color(Ray(hr.p, random_vector), world, depth - 1) \
                   * 1/2
            # return 1/2 * Color(normal.x + 1.0, normal.y + 1.0, normal.z + 1.0)

        unit_dir: Vec3 = r.direction.unit()

        # unitDir.y can be from -1 to 1.
        a = (unit_dir.y + 1.0) / 2.0
        start_color = Color(1.0, 1.0, 1.0)
        end_color = Color(1.0, 0.0, 0.0)

        return start_color * (1.0 - a) + end_color * a

    def render_pixel(self, world: Hittable, x: int, y: int) -> Color:
        pixel_color = Color(0.0, 0.0, 0.0)

        for sample in range(self.pixel_samples):
            offset_x = random.uniform(-0.5, 0.5)
            offset_y = random.uniform(-0.5, 0.5)

            ray_direction: Vec3 = self.p00 \
                                  + self.dh * (x + offset_x) \
                                  + self.dv * (y + offset_y) \
                                  - self.center

            r = Ray(self.center, ray_direction)
            pixel_color += self.ray_color(r, world, self.depth)
        
        return pixel_color / self.pixel_samples

    def render(self, world: Hittable) -> None:
        image = Image(self.image_width, self.image_height)

        for x in range(self.image_width):
            for y in range(self.image_height):
                image.set_pixel(x, y, self.render_pixel(world, x, y))

        image.save("output.png")
