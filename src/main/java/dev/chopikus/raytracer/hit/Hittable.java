package dev.chopikus.raytracer.hit;

import java.util.Optional;

import dev.chopikus.raytracer.geom.*;

public interface Hittable {
    /* Returns a record of the earlist hit of ray r. */
    /* Returned HitRecord must have t in the interval (tMin, tMax). */
    /* If such hit wasn't found, Optional.empty() is returned. */
    public Optional<HitRecord> hit(Ray r, double tMin, double tMax);
}
