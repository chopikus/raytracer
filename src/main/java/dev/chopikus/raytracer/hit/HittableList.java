package dev.chopikus.raytracer.hit;

import java.util.ArrayList;
import java.util.Optional;

import dev.chopikus.raytracer.geom.*;

public record HittableList(ArrayList<Hittable> objects) implements Hittable {
    @Override
    public Optional<HitRecord> hit(Ray r, double tMin, double tMax) {
        return Optional.empty();
    }
}
