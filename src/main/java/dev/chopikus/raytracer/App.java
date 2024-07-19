package dev.chopikus.raytracer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class App {
    static Logger logger = LoggerFactory.getLogger(App.class);

    public static Color rayColor(Ray r) {
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
                Point pixelCenter = p00
                                    .add(dh.multiply(x))
                                    .add(dv.multiply(y))
                                    .toPoint();

                Vec3 rayDirection = pixelCenter
                                    .subtract(cameraCenter);

                Ray r = new Ray(pixelCenter, rayDirection);
                image.setPixel(x, y, rayColor(r));
            }
        }
        image.write("target/output.png", "png");
    }
}
