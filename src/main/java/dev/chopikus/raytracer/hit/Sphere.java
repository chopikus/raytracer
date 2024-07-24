package dev.chopikus.raytracer.hit;

import java.util.Optional;
import java.util.Random;

import dev.chopikus.raytracer.geom.*;
import dev.chopikus.raytracer.util.*;

public record Sphere(Point center, double radius) implements Hittable {
    @Override
    public Optional<HitRecord> hit(Ray r, Interval i) {
        var orig = r.origin();
        var dir = r.direction();
        var OC = this.center.subtract(orig);
 
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
        if (i.surrounds(t1))
            t = t1;
        else if (i.surrounds(t2))
            t = t2;
        else
            return Optional.empty();
        
        var p = r.at(t);
        var outwardNormal = p.subtract(center).unit();
        boolean frontFace = r.direction().scalarProduct(outwardNormal) <= 0;
        var normal = frontFace ? outwardNormal : outwardNormal.minus();

        return Optional.of(new HitRecord(p, normal, t, frontFace));
    }

    public static Vec3 random(Random r) {
        double x=0.0, y=0.0, z=0.0, len=0.0;

        while (len == 0.0) {
            x = r.nextGaussian();
            y = r.nextGaussian();
            z = r.nextGaussian();
            len = Math.sqrt(x*x + y*y + z*z);
        }

        return new Vec3(x/len, y/len, z/len);
    }
}
