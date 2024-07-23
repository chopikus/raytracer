package dev.chopikus.raytracer.util;

public record Interval(double min, double max) {
    public static final Interval empty = new Interval();
    public static final Interval universe = new Interval(Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);

    public Interval() {
        this(Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY);
    }

    public double size() {
        return max - min;
    }

    public boolean contains(double x) {
        return x >= min && x <= max;
    }

    public boolean surrounds(double x) {
        return x > min && x < max;
    }
}
