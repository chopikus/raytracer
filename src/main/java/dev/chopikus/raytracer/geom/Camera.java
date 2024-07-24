package dev.chopikus.raytracer.geom;

import java.util.Optional;
import java.util.Random;

import dev.chopikus.raytracer.hit.*;
import dev.chopikus.raytracer.util.*;

public class Camera {
    private int imageWidth;
    private int imageHeight;
    private Point center;
    private Point p00;
    private Vec3 dh;
    private Vec3 dv;
    private int pixelSamples;
    private Random random = new Random();
    private int depth = 10;

    public Camera(double aspectRatio, int imageWidth, int pixelSamples) {
        this.pixelSamples = pixelSamples;
        this.imageWidth = imageWidth;
        imageHeight = (int) (imageWidth / aspectRatio);

        /* Geometric units */
        var focalLength = 1.0;
        var viewportHeight = 2.0;
        var viewportWidth = viewportHeight * ((double) imageWidth / imageHeight);

        center = new Point(0.0, 0.0, 0.0);

        Vec3 h = new Vec3(viewportWidth, 0.0, 0.0);
        Vec3 v = new Vec3(0.0, -viewportHeight, 0.0);
        dh = h.divide(imageWidth);
        dv = v.divide(imageHeight);

        Point viewportCenter = center
                                .subtract(new Vec3(0, 0, focalLength))
                                .toPoint();

        Point viewportStart = viewportCenter
                                .subtract(v.divide(2))
                                .subtract(h.divide(2))
                                .toPoint();
        
        p00 = viewportStart
                    .add(dv.divide(2))
                    .add(dh.divide(2))
                    .toPoint();
    }

    public Color rayColor(Ray r, Hittable world, int depth) {
        if (depth <= 0) {
            return new Color(0.0, 0.0, 0.0);
        }

        Optional<HitRecord> hr = world.hit(r, new Interval(0.001, Double.POSITIVE_INFINITY));
        
        if (hr.isPresent()) {
            var normal = hr.get().normal();
            var randomVector = Vec3.randomOnUnitHemisphere(random, normal);
            
            return rayColor(new Ray(hr.get().p(), randomVector), world, depth-1)
                    .divide(2.0);
            /*return new Color(normal.x + 1.0, normal.y + 1.0, normal.z + 1.0)
                       .divide(2.0);*/
        }

        Vec3 unitDir = r.direction().unit();
        /* unitDir.y() can be from -1 to 1. */
        var a = (unitDir.y + 1.0) / 2.0;
        var startColor = new Color(1.0, 1.0, 1.0);
        var endColor = new Color(1.0, 0.0, 0.0);

        return startColor
               .multiply(1.0 - a)
               .add(endColor.multiply(a));
    }

    public void render(Hittable world) {
        var image = new Image(imageWidth, imageHeight);

        for (int x = 0; x < imageWidth; x++) {
            for (int y = 0; y < imageHeight; y++) {
                var pixelColor = new Color(0.0, 0.0, 0.0);

                for (int sample = 0; sample < pixelSamples; sample++) {
                    double offsetX = random.nextDouble() - 0.5;
                    double offsetY = random.nextDouble() - 0.5;

                    Vec3 rayDirection = p00
                                    .add(dh.multiply(x + offsetX))
                                    .add(dv.multiply(y + offsetY))
                                    .subtract(center);
                    
                    Ray r = new Ray(center, rayDirection);
                    pixelColor = pixelColor.add(rayColor(r, world, this.depth));
                }

                pixelColor = pixelColor.divide(pixelSamples);
                image.setPixel(x, y, pixelColor);
            }
        }
        image.write("target/output.png", "png");
    }
}
