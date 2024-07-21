package dev.chopikus.raytracer.hit;

import java.util.Optional;

import dev.chopikus.raytracer.geom.*;

public interface Hittable {
    public Optional<HitRecord> hit(Ray r, double tMin, double tMax);
}
