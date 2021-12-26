# Mandelbrot Set Generator 
A small script written in Python3 that generates a viaual representation of the Mandelbrot set.

<p align="center">
    <img width="640" height="360" src="./sample.png" alt="Mandlebrot set">
</p>

### Abstract
The colors in the output image are in HSV format. The darker pixels represent those areas where the reast recursion was made (basically those parts which do not belong in the set), and vice-versa. The algorithm used is, of course: $$`z_{n+1}=(z_{n})^{2}+c, z_{0}=0`$$

## Dependencies
- [Pillow](https://pypi.org/project/Pillow/) </br>
To get it installed, simply do: 
```sh
pip install Pillow
```

## Installation
To get started, simply clone the repo, cd into it and run it.. it's as easy as it gets...
```sh
git clone https://github.com/DarkKnight450/mandelbrot.git
cd mandelbrot
python main.py
```
The image will be saved in the current working directory as `output.png`

## Customizing output
You may change the resolution of the output image by changing its height and width in [main.py](https://github.com/DarkKnight450/mandelbrot/blob/main/main.py#L6)
```python
# Image size (pixels)
WIDTH = 3840
HEIGHT = 2160
```
Further, you may change the recursion depth in [mandlebrot.py](https://github.com/DarkKnight450/mandelbrot/blob/main/mandelbrot.py#L3)
```python
MAX_ITER = 1e2
```
The darker pixels represent those areas where the reast recursion was made.
In the code snipplet below, `color` represents the brightness. You may obviously change the HSV values as you want in [main.py](https://github.com/DarkKnight450/mandelbrot/blob/main/main.py#L43)
```python
draw.point(
    [x, y],
    tuple(
        round(i * 255)
        for i in colorsys.hsv_to_rgb(<hue> / <saturation>, 100 / 100, color / 100)
    ),
)
```
