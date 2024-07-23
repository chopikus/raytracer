package dev.chopikus.raytracer.hit;

import java.util.Optional;

import dev.chopikus.raytracer.geom.*;
import dev.chopikus.raytracer.util.*;

public interface Hittable {
    /* Returns a record of the earlist hit of ray r. */
    /* Returned HitRecord must have t surrounded in the interval i. */
    /* If such hit wasn't found, Optional.empty() is returned. */
    public Optional<HitRecord> hit(Ray r, Interval i);
}
