package dev.chopikus.raytracer;

import java.util.Optional;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import dev.chopikus.raytracer.geom.*;
import dev.chopikus.raytracer.hit.*;
import dev.chopikus.raytracer.render.*;

public class App {
    static Logger logger = LoggerFactory.getLogger(App.class);

    static Sphere sphere = new Sphere(new Point(0.0, 0.0, -1.0), 0.5);

    static Color rayColor(Ray r) {
        var spherePoint = new Point(0.0, 0.0, -1.0);
        Optional<HitRecord> hr = sphere.hit(r, -10000, 10000);
        
        if (hr.isPresent()) {
            Vec3 N = r.at(hr.get().t())
                      .subtract(spherePoint)
                      .unit();
            
            /* Since N is normalized, each coordinate can be from -1 to 1. */
            return new Color(N.x + 1.0, N.y + 1.0, N.z + 1.0)
                       .divide(2.0);
        }

        Vec3 unitDir = r.direction().unit();
        /* unitDir.y() can be from -1 to 1. */
        var a = (unitDir.y + 1.0) / 2.0;
        var startColor = new Color(1.0, 1.0, 1.0);
        var endColor = new Color(0.5, 0.7, 1.0);

        return startColor
               .multiply(1.0 - a)
               .add(endColor.multiply(a));
    }

    public static void main(String[] args) {
        /* Image units */
        var aspectRatio = 16.0 / 9.0;
        var imageWidth = 400;
        var imageHeight = (int) (imageWidth / aspectRatio);

        /* Geometric units */
        var focalLength = 1.0;
        var viewportHeight = 2.0;
        var viewportWidth = viewportHeight * ((double) imageWidth / imageHeight);

        Point cameraCenter = new Point(0.0, 0.0, 0.0);

        Vec3 h = new Vec3(viewportWidth, 0.0, 0.0);
        Vec3 v = new Vec3(0.0, -viewportHeight, 0.0);
        Vec3 dh = h.divide(imageWidth);
        Vec3 dv = v.divide(imageHeight);

        Point viewportCenter = cameraCenter
                               .subtract(new Vec3(0, 0, focalLength))
                               .toPoint();

        Point viewportStart = viewportCenter
                              .subtract(v.divide(2))
                              .subtract(h.divide(2))
                              .toPoint();
        
        Point p00 = viewportStart
                    .add(dv.divide(2))
                    .add(dh.divide(2))
                    .toPoint();

        var image = new Image(imageWidth, imageHeight);
        for (int x = 0; x < imageWidth; x++) {
            for (int y = 0; y < imageHeight; y++) {
                Vec3 rayDirection = p00
                                    .add(dh.multiply(x))
                                    .add(dv.multiply(y))
                                    .subtract(cameraCenter);
                
                /* There was a bug in the past creating a new Ray(pixelCenter, rayDirection) */
                Ray r = new Ray(cameraCenter, rayDirection);
                image.setPixel(x, y, rayColor(r));
            }
        }
        image.write("target/output.png", "png");
    }
}
