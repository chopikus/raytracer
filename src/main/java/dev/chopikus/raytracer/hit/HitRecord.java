package dev.chopikus.raytracer.hit;

import dev.chopikus.raytracer.geom.*;

public record HitRecord(Point p, Vec3 normal, double t, boolean frontFace) {}
