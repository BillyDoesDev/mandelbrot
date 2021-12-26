from PIL import Image, ImageDraw
import mandelbrot
import colorsys

# Image size (pixels)
WIDTH = 3840
HEIGHT = 2160

# drawing area
# values taken from https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set
RE_START = -2.0
RE_END = 0.47
IM_START = -1.12
IM_END = 1.12

im = Image.new(mode="RGB", size=(WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)

progress = 0
disp_progress = ""
print("Progress: ", end="")

try:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(len(disp_progress) * "\b", end="")
            # Convert pixel coordinate to complex number
            c = complex(
                RE_START + (x / WIDTH) * (RE_END - RE_START),
                IM_START + (y / HEIGHT) * (IM_END - IM_START),
            )
            iterations = mandelbrot.mandelbrot(c)
            # The color depends on the number of iterations
            # darker color indicates lesser  number of iterations
            color = iterations * 100 // mandelbrot.MAX_ITER

            # using colorsys to convery hsv to rgb
            # it's dumb, really, so we need to normalise all inputs (/360, /100 and /100 respectively)
            draw.point(
                [x, y],
                tuple(
                    round(i * 255)
                    for i in colorsys.hsv_to_rgb(264 / 360, 100 / 100, color / 100)
                ),
            )

            disp_progress = str(round((progress * 100 / (WIDTH * HEIGHT)), 2)) + "%"
            print(disp_progress, end="")
            progress += 1
except KeyboardInterrupt:
    im.convert(mode="RGB").save("output.png")
    print(x, y)

im.convert(mode="RGB").save("output.png")
