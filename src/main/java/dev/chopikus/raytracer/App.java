package dev.chopikus.raytracer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class App 
{    
    static Logger logger = LoggerFactory.getLogger(App.class);
    
    public static void main( String[] args )
    {
        int imageWidth = 256;
        int imageHeight = 256;
        int colorResolution = 255;

        System.out.printf("P3\n%d %d\n255\n", imageWidth, imageHeight);
        for (int y=0; y<imageHeight; y++) {
            for (int x=0; x<imageWidth; x++) {
                var r = (double) x / (imageWidth - 1);
                var g = (double) y / (imageHeight - 1);
                var b = 0.0;

                System.out.printf("%d %d %d\n", (int) (r * colorResolution), (int) (g * colorResolution), (int) (b * colorResolution));
            }
        }
    }
}
