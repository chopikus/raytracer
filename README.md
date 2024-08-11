# raytracer

(based on 'Raytracing in one weekend')

So far this project is in progress, however there are some interesting results to look at.

While researching scientific programming libraries I ended up having 4 different implementations of the ray tracer in Java, Python, Numpy.

## Benchmarking

Every rendering is done on CPU except for cupy implementation.

### Pic1

![Rendered picture](https://github.com/chopikus/raytracer/blob/main/pic1.png)

Size: 400x225, two spheres with 50% diffusion and red gradient background, rendered with 10 samples per pixel.

### Pic2

![Rendered picture](https://github.com/chopikus/raytracer/blob/main/pic2.png)

Size: 400x225, one red sphere without diffusion or computation of normal vector, rendered with 10 samples per pixel.


### Pic3

![Rendered picture](https://github.com/chopikus/raytracer/blob/main/pic3.png)

Size: 1000x562, one red sphere without diffusion or computation of normal vector, rendered with 240 samples per pixel.


### Hardware, OS

CPU: Xeon® E5-2620 v2

GPU: GTX 1070

RAM: 32Gb

VM running Ubuntu 22.04

`python3 --version`: `Python 3.10.12`

`java -version`: `openjdk version "21.0.4" 2024-07-16, OpenJDK Runtime Environment (build 21.0.4+7-Ubuntu-1ubuntu222.04), OpenJDK 64-Bit Server VM (build 21.0.4+7-Ubuntu-1ubuntu222.04, mixed mode, sharing)`

### Results

Rendering Pic1:

|Implementation|Real Time|Result of `time` command   |Command   |Branch|
|---|---|---|---|---|
|Python|**42.393s**|`real	0m42.393s user	0m42.371s sys	0m0.020s`   |`time (python3 src/main.py)`   |`main`|
|Python (Pypy)|**2.382s**|`real	0m2.382s user	0m2.271s sys	0m0.105s`   |`time (./pypy3.10-v7.3.16-linux64/bin/pypy3.10 raytracer/src/main.py)`   |`main`|
|Java|**1.016s**|`real	0m1.016s user	0m1.694s sys	0m0.323s`   |`time (java -jar target/raytracer-1.0-SNAPSHOT.jar)`   |`java-impl`|

Rendering Pic2:
|Implementation|Real Time|Result of `time` command   |Command   |Branch|
|---|---|---|---|---|
|Python|**19.185s**|`real	0m19.185s user	0m20.224s sys	0m0.052s`|`time (python3 src/main.py)`|`python-simple-impl`|
|Python (Numpy)|**1.331s**|`real	0m1.331s user	0m2.182s sys	0m0.194s`|`time (python3 src/main.py)`|`speedup`|
|Java|**0.552s**|`real	0m0.552s user	0m0.810s sys	0m0.167s`|`time (java -jar target/raytracer-1.0-SNAPSHOT.jar)|`java-simple-impl`|

Rendering Pic3:
|Implementation|Real Time|Result of `time` command   |Command   |Branch|
|---|---|---|---|---|
|Python (cupy) (**On GPU**)|**2.658s**|`real	0m2.658s user	0m1.723s sys	0m1.909s`|`time (python3 src/main.py)`|`cupy-speedup`|
|Python (numpy)|**48.923s**|`real	0m48.923s user	0m34.417s sys	0m15.646s`|`time (python3 src/main.py)`|`speedup`|
|Java|**18.256s**|`real	0m18.256s user	0m17.582s sys	0m1.565s`|`time (java -jar target/raytracer-1.0-SNAPSHOT.jar)`|`java-simple-impl`|

## Future

TODO Benchmark rendering the same picture for all implementations.
