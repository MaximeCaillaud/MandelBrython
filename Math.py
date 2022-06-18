from PIL import Image


def pointc(x, y):
    if y == 2:
        x = round(x + 0.0001, 4)
        y = -2
    else:
        y = round(y + 0.0001, 4)
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
    img = Image.new('RGB', (45000, 45000))
    c = (-2, -2)
    pixels = img.load()
    print("0%")
    while c != (2, 2):
        x = int(c[0]*10000+20000)
        y = int(c[1]*10000+20000)
        pct1 = int((c[0]+2)*100/4)
        if isMandelbrot(c):
            pixels[x, y] = (255, 255, 255)
        c = pointc(c[0], c[1])
        pct2 = int((c[0] + 2) * 100 / 4)
        if pct1 != pct2:
            print(str(pct2)+"%")
    img.show()

