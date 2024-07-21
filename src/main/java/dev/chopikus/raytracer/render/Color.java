package dev.chopikus.raytracer.render;

public record Color(double r, double g, double b) {
    public Color add(Color another) {
        return new Color(r + another.r, g + another.g, b + another.b);
    }

    public Color subtract(Color another) {
        return new Color(r - another.r, g - another.g, b - another.b);
    }

    public Color multiply(double c) {
        return new Color(r * c, g * c, b * c);
    }

    public Color divide(double c) {
        return new Color(r / c, g / c, b / c);
    }
}
