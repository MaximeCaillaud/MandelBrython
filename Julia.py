from PIL import Image


def pointm(x, y):
    if y == 1.25:
        x = round(x + 0.0001, 4)
        y = -1.25
    else:
        y = round(y + 0.0001, 4)
    return x, y


def suitex(x, y, cx):
    x = (x ** 2) - (y ** 2) + cx
    return x


def suitey(x, y, cy):
    y = (2 * x * y) + cy
    return y


def suite(x, y, cx, cy):
    tpx=x
    tpy=y
    x = suitex(tpx, tpy, cx)
    y = suitey(tpx, tpy, cy)
    return x, y


def distom(x, y):
    om = x ** 2 + y ** 2
    return om


def isJulia(m,c):
    MAXIT = 500
    x = m[0]
    y = m[1]
    i = 0
    while distom(x, y) < 4 and i < MAXIT:
        xy = suite(x, y, c[0], c[1])
        x = xy[0]
        y = xy[1]
        i += 1
    return i


def juliacomplet(c, taille=25000):
    m = (-1.25, -1.25)
    img = Image.new('RGB', (taille, taille))
    pixels = img.load()
    while m != (1.25, 1.25):
        x = int(m[0] * 10000 + taille/2) - 1
        y = int(m[1] * 10000 + taille/2) - 1
        print(x, y)
        res = isJulia(m, c)
        pixels[x, y] = (int(10 * res) % 256, int(1 * res) % 256, int(1 * res) % 256)
        m = pointm(m[0], m[1])
    return img


if __name__ == "__main__":
    c = (-0.8, 0.156)
    juliacomplet(c).show()

