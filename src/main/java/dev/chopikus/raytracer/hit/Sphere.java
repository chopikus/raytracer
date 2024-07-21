package dev.chopikus.raytracer.hit;

import java.util.Optional;

import dev.chopikus.raytracer.geom.*;

public record Sphere(Point center, double radius) implements Hittable {
    @Override
    public Optional<HitRecord> hit(Ray r, double tMin, double tMax) {
        var orig = r.origin();
        var dir = r.direction();
        var OC = this.center
                     .subtract(orig);

        var A = dir.lenSquared();
        var B = OC.scalarProduct(dir) * -2.0;
        var C = OC.lenSquared() - (this.radius*this.radius);
        var D = B*B - 4*A*C;

        if (D < 0) {
            return Optional.empty();
        }

        var sqrtD = Math.sqrt(D);

        /* Returning minimum time t that is in (tMin, tMax) range. */
        var t1 = (-B - sqrtD) / (2 * A);
        var t2 = (-B + sqrtD) / (2 * A);
        
        double t;
        if (t1 > tMin && t1 < tMax)
            t = t1;
        else if (t2 > tMin && t2 < tMax)
            t = t2;
        else
            return Optional.empty();
        
        var p = r.at(t);
        var normal = p.subtract(center).unit();
        return Optional.of(new HitRecord(p, normal, t));
    }
}
