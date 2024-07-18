package dev.chopikus.raytracer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class App 
{    
    static Logger logger = LoggerFactory.getLogger(App.class);

    public static void main( String[] args )
    {
        var imageWidth = 256;
        var imageHeight = 256;
        var image = new Image(imageWidth, imageHeight);
        for (int x=0; x<imageWidth; x++) {
            for (int y=0; y<imageHeight; y++) {
                var r = (double) x / (imageWidth - 1);
                var g = (double) y / (imageHeight - 1);
                var b = 0.0;
                image.setPixel(x, y, r, g, b);
            }
        }
        image.write("target/output.png", "png");
    }
}
