package dev.chopikus.raytracer.geom;

import java.util.Random;

public class Vec3 {
    public double x, y, z;

    public Vec3() {
        x = 0.0f;
        y = 0.0f;
        z = 0.0f;
    }

    public Vec3(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    /* Returns the uniformly distributed vector on a unit sphere */
    public static Vec3 randomOnUnitSphere(Random r) {
        double x=0.0, y=0.0, z=0.0, len=0.0;

        while (len == 0.0) {
            x = r.nextGaussian();
            y = r.nextGaussian();
            z = r.nextGaussian();
            len = Math.sqrt(x*x + y*y + z*z);
        }

        return new Vec3(x/len, y/len, z/len);
    }

    /* Returns the uniformly distributed vector on a unit sphere in the same hemisphere as `normal` vector. */
    public static Vec3 randomOnUnitHemisphere(Random r, Vec3 normal) {
        var v = randomOnUnitSphere(r);
        if (v.scalarProduct(normal) > 0.0) {
            return v;
        } else {
            return v.minus();
        }
    }

    public Point toPoint() {
        return new Point(x, y, z);
    }

    public Vec3 minus() {
        return new Vec3(-x, -y, -z);
    }

    public Vec3 add(Vec3 v) {
        return new Vec3(x + v.x, y + v.y, z + v.z);
    }

    public Vec3 subtract(Vec3 v) {
        return new Vec3(x - v.x, y - v.y, z - v.z);
    }

    public Vec3 multiply(double t) {
        return new Vec3(x * t, y * t, z * t);
    }

    public Vec3 divide(double t) {
        return this.multiply(1/t);
    }

    public Vec3 unit() {
        return this.divide(this.len());
    }

    public double scalarProduct(Vec3 v) {
        return x * v.x + y * v.y + z * v.z;
    }

    public double len() {
        return Math.sqrt(this.lenSquared());
    }

    public double lenSquared() {
        return x*x + y*y + z*z;
    }
}
