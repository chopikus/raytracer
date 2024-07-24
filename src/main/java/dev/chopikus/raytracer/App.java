package dev.chopikus.raytracer;

import java.util.ArrayList;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import dev.chopikus.raytracer.geom.*;
import dev.chopikus.raytracer.hit.*;

public class App {
    static Logger logger = LoggerFactory.getLogger(App.class);

    public static void main(String[] args) {
        ArrayList<Hittable> hittables = new ArrayList<>();
        hittables.add(new Sphere(new Point(0.0, 0.0, -1.0), 0.5));
        hittables.add(new Sphere(new Point(0.0, -100.5, -1.0), 100.0));
        HittableList world = new HittableList(hittables);

        new Camera(16.0 / 9.0, 1000, 250)
            .render(world);
    }
}
