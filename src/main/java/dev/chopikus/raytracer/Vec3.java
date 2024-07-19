package dev.chopikus.raytracer;

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

    Point toPoint() {
        return new Point(x, y, z);
    }

    Vec3 minus() {
        return new Vec3(-x, -y, -z);
    }

    Vec3 add(Vec3 v) {
        return new Vec3(x + v.x, y + v.y, z + v.z);
    }

    Vec3 subtract(Vec3 v) {
        return new Vec3(x - v.x, y - v.y, z - v.z);
    }

    Vec3 multiply(double t) {
        return new Vec3(x * t, y * t, z * t);
    }

    Vec3 divide(double t) {
        return this.multiply(1/t);
    }

    Vec3 unit() {
        return this.divide(this.len());
    }

    double scalarProduct(Vec3 v) {
        return x * v.x + y * v.y + z * v.z;
    }

    double len() {
        return Math.sqrt(this.lenSquared());
    }

    double lenSquared() {
        return x*x + y*y + z*z;
    }
}
