from util import Image, Color

def drawImage() -> None:
    width = 200
    height = 200
    img = Image(width, height)

    for x in range(width):
        for y in range(height):
            r = x / (width - 1)
            g = y / (height - 1)
            b = 0.0
            c = Color(r, g, b)
            img.set_pixel(x, y, c)
    
    img.save("output.png")

if __name__ == '__main__':
    drawImage()
