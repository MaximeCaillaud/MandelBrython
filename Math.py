import sys

from PIL import Image
import json


def pointc(indy,indx):
    tabc = []
    x = -2.0001
    while x < indx:
        x = round(x + 0.0001, 4)
        y = -2.0001
        while y < indy:
            y = round(y + 0.0001, 4)
            tabc.append((int(x*1000+2000), int(y*1000+2000)))
    return tabc


def pointcvalide(ind=1):
    cx = 2.0001
    while cx > -ind:
        cx = round(cx - 0.0001, 4)
        cy = 2.0001
        while cy > -ind:
            cy = round(cy - 0.0001, 4)
            x = 0
            y = 0
            i = 0
            while distom(x, y) < 4 and i < 50:
                xy = suite(x, y, cx, cy)
                x = xy[0]
                y = xy[1]
                i += 1
            if i == 50:
                f = open("cvalide.txt", "a")
                f.write(str((x, y)) + ",")
    return


def suitex(x, y, cx):
    x = (x ** 2) - (y ** 2) + cx
    return x


def suitey(x, y, cy):
    y = (2 * x * y) + cy
    return y


def distom(x, y):
    om = x ** 2 + y ** 2
    return om


def suite(x, y, cx, cy):
    tpx=x
    tpy=y
    x = suitex(tpx, tpy, cx)
    y = suitey(tpx, tpy, cy)
    return x, y


def isMandelbrot(c):
    MAXIT = 50
    x = 0
    y = 0
    i = 0
    while distom(x, y) < 4 and i < MAXIT:
        xy = suite(x, y, c[0], c[1])
        x = xy[0]
        y = xy[1]
        i += 1
    if i == MAXIT:
        return True
    else:
        return False


if __name__ == "__main__":
    img = Image.new('RGB', (4000, 4000))
    pixels = img.load()
    cs = pointc(2, 2)
    cvalide = []
    for c in cs:
        x = int(c[0])
        y = int(c[1])
        if isMandelbrot(c):
            cvalide.append(c)
            pixels[x, y] = (255, 255, 255)
    fichier = open("cvalide.txt", "w")
    fichier.write(str(cvalide))
    img.show()

