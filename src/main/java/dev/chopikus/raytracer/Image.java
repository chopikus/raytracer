package dev.chopikus.raytracer;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Image {
    private BufferedImage buf;

    public Image(int imageWidth, int imageHeight) {
        buf = new BufferedImage(imageWidth, imageHeight, BufferedImage.TYPE_INT_RGB);
    }

    /* Set a pixel (x, y) color to (r, g, b).
     * r, g, b must be in the range [0.0, 1.0].
     * Throws ArrayIndexOutOfBoundsException if (x, y) is out of bounds.
     * Throws IllegalArgumentException if r, g, b are not in the range [0.0, 1.0].
    */
    public void setPixel(int x, int y, double r, double g, double b) {
        var color = new Color((float) r, (float) g, (float) b);
        buf.setRGB(x, y, color.getRGB());
    };

    /* Writes the Image to a file under a path name.
     * fileType is not appended to pathName.
     */
    public void write(String pathName, String fileType) {
        try {
            File outputFile = new File(pathName);
            ImageIO.write(buf, fileType, outputFile);
        }
        catch (IOException e) {
            System.err.printf("Error writing to a file! pathName=%s, fileType=%s\n", pathName, fileType);
            e.printStackTrace(System.err);
        }
    };
}