from PIL import Image


def pointc(ind=1):
    tabc = []
    x = 2.001
    while x > -ind:
        x = round(x - 0.001, 3)
        y = 2.001
        while y > -ind:
            y = round(y - 0.001, 3)
            tabc.append((x, y))
    return tabc


def suitex(x, y, cx):
    x = (x ** 2) - (y ** 2) + cx
    return x


def suitey(x, y, cy):
    y = (2 * x * y) + cy
    return y


def distom(x, y):
    om = ((x ** 2) + (y ** 2))
    return om


def suite(x, y, cx, cy):
    x = suitex(x, y, cx)
    y = suitey(x, y, cy)
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
    cs = pointc(2)
    cvalide = []
    for c in cs:
        x = int(c[0]*1000)
        y = int(c[1]*1000)
        if isMandelbrot(c):
            cvalide.append(c)
            pixels[x, y] = (255, 0, 0)

    #fichier = open("cvalide.txt", "w")
    #fichier.write(str(cvalide))

    img.show()

