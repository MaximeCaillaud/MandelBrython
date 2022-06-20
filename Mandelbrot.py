from PIL import Image


def pointc(x, y, pas=0.002, arrondi=3):
    if y == 2:
        x = round(x + pas, arrondi)
        y = -2
    else:
        y = round(y + pas, arrondi)
    return x, y


def pointczoom(x, y, pas=0.002, arrondi=3, minz =-0.1, maxz=0.1):
    if y == maxz:
        x = round(x + pas, arrondi)
        y = minz
    else:
        y = round(y + pas, arrondi)
    return x, y


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
    MAXIT = 500
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


def complet(taille=4000, pas=0.001, arrondi=3):
    print("0%")
    img = Image.new('RGB', (taille, taille))
    c = (-2, -2)
    pixels = img.load()
    while c != (2, 2):
        x = int(c[0] * (taille / 4) + (taille / 2))
        y = int(c[1] * (taille / 4) + (taille / 2))
        pct1 = int((c[0] + 2) * 100 / 4)
        if isMandelbrot(c):
            pixels[x, y] = (255, 255, 255)
        c = pointc(c[0], c[1], pas, arrondi)
        pct2 = int((c[0] + 2) * 100 / 4)
        if pct1 != pct2:
            print(str(pct2) + "%")
    return img


def zoom(taille=5000, pas=0.0000001, arrondi=7, zonex=(-1.7115, -1.711), zoney=(-0.00025, 0.00025)):
    img = Image.new('RGB', (taille, taille))
    c = (zonex[0], zoney[0])
    pixels = img.load()
    while c != (zonex[1], zoney[1]):
        x = int(abs((zonex[0]-c[0]) * 10000000))
        y = int(abs((zoney[0]-c[1]) * 10000000))
        if isMandelbrot(c):
            print(x, y)
            pixels[x, y] = (255, 255, 255)
        c = pointczoom(c[0], c[1], pas, arrondi, zoney[0], zoney[1])
    return img


if __name__ == "__main__":
    complet().show()
    zoom().show()




