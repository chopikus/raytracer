package dev.chopikus.raytracer;

import java.util.ArrayList;

import dev.chopikus.raytracer.geom.*;
import dev.chopikus.raytracer.hit.*;

public class App {
    public static void main(String[] args) {
        ArrayList<Hittable> hittables = new ArrayList<>();
        hittables.add(new Sphere(new Point(0.0, 0.0, -1.0), 0.5));
        HittableList world = new HittableList(hittables);

        new Camera(16.0 / 9.0, 400, 10)
            .render(world);
    }
}
