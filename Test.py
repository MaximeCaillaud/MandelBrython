# Programme : mandelbrot.py
# Langage : Python 3.6 - Pygame 1.9
# Auteur : Mathieu
# Description : Calcule et affiche la fractale de Mandelbrot en noir et blanc
from PIL import Image



if __name__=="__main__":


    MAX_ITERATION = 50

    XMIN, XMAX, YMIN, YMAX = -2, +0.5, -1.25, +1.25

    img = Image.new('RGB', (4000, 4000))
    pixels = img.load()
    for y in range(4000):
        for x in range(4000):
            cx = (x * (XMAX - XMIN) / 500 + XMIN)
            cy = (y * (YMIN - YMAX) / 500 + YMAX)
            xn = 0
            yn = 0
            n = 0
            while (xn * xn + yn * yn) < 4 and n < MAX_ITERATION:
                tmp_x = xn
                tmp_y = yn
                xn = tmp_x * tmp_x - tmp_y * tmp_y + cx
                yn = 2 * tmp_x * tmp_y + cy
                n = n + 1
            if n == MAX_ITERATION:
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)

    img.show()