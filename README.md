# raytracer

(based on 'Raytracing in one weekend')

So far this project is in progress, however there are some interesting results to look at.

While researching scientific programming libraries I ended up having 3 different implementations of the ray tracer in Java, Python, Numpy.

## Benchmarking

One of the implementations produces a simpler image than the other ones.

### Pic1

![Rendered picture](https://github.com/chopikus/raytracer/blob/main/pic1.png)

Size: 400x225, two spheres with 50% diffusion and red gradient background.

### Pic2

![Rendered picture](https://github.com/chopikus/raytracer/blob/main/piс2.png)

Size: 400x225, one red sphere without diffusion or computation of normal vector.

### Hardware, OS

CPU: Xeon® E5-2620 v2

GPU: GTX 1070

VM running Ubuntu 22.04

`python3 --version`: `Python 3.10.12`
`java -version`: openjdk version "21.0.4" 2024-07-16, OpenJDK Runtime Environment (build 21.0.4+7-Ubuntu-1ubuntu222.04), OpenJDK 64-Bit Server VM (build 21.0.4+7-Ubuntu-1ubuntu222.04, mixed mode, sharing)

### Results

Rendering Pic1:

Python implementation: real	0m42.393s user	0m42.371s sys	0m0.020s 
Command: `time (python3 src/main.py)`

Python implementation (Pypy): real	0m2.382s user	0m2.271s sys	0m0.105s
Command: `time (./pypy3.10-v7.3.16-linux64/bin/pypy3.10 raytracer/src/main.py)

Java implementation: real	0m1.016s user	0m1.694s sys	0m0.323s
Command: `time (java -jar target/raytracer-1.0-SNAPSHOT.jar)`


Rendering Pic2:
Numpy implementation: real	0m1.331s user	0m2.182s sys	0m0.194s
Command: `time (python3 src/main.py)`

