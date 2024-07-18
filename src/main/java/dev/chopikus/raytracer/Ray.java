package dev.chopikus.raytracer;

public class Ray {
    public Point origin;
    public Point direction;

    public Ray(Point origin, Point direction) {
        this.origin = origin;
        this.direction = direction;
    }

    public Point at(double t) {
        return direction
                .multiply(t)
                .add(origin)
                .toPoint();
    }
}
