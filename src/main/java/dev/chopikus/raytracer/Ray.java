package dev.chopikus.raytracer;

public record Ray(Point origin, Vec3 direction) {
    public Point at(double t) {
        return direction
               .multiply(t)
               .add(origin)
               .toPoint();
    }
}
