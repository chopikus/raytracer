package dev.chopikus.raytracer.hit;

import java.util.ArrayList;
import java.util.Optional;

import dev.chopikus.raytracer.geom.*;
import dev.chopikus.raytracer.util.*;

public record HittableList(ArrayList<Hittable> hittables) implements Hittable {
    @Override
    public Optional<HitRecord> hit(Ray r, Interval i) {
        Optional<HitRecord> result = Optional.empty();
        double cur = i.max();

        for (var hittable : hittables) {
            Optional<HitRecord> hitResult = hittable.hit(r, new Interval(i.min(), cur));
            if (hitResult.isPresent()) {
                result = hitResult;
                cur = hitResult.get().t();
            }
        }

        return result;
    }
}
