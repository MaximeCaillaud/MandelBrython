
import pygame


if __name__=="__main__":
    MAX_ITERATION = 50
    XMIN, XMAX, YMIN, YMAX = -1.25, 1.25, -1.25, +1.25
    LARGEUR, HAUTEUR = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Fractale de Mandelbrot")
    for y in range(HAUTEUR):
        for x in range(LARGEUR):
            xn = (x * (XMAX - XMIN) / LARGEUR + XMIN)
            yn = (y * (YMIN - YMAX) / HAUTEUR + YMAX)
            cx = 0.285
            cy = 0.01
            n = 0
            while (xn * xn + yn * yn) < 4 and n < MAX_ITERATION:
                tmp_x = xn
                tmp_y = yn
                xn = tmp_x * tmp_x - tmp_y * tmp_y + cx
                yn = 2 * tmp_x * tmp_y + cy
                n = n + 1
            if n == MAX_ITERATION:
                screen.set_at((x, y), ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256))
            else:
                screen.set_at((x, y), ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256))
    pygame.display.flip()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                p = pygame.mouse.get_pos()
                px = (p[0] * (XMAX - XMIN) / LARGEUR + XMIN)
                py = (p[1] * (YMIN - YMAX) / HAUTEUR + YMAX)
                print("({};{})".format(px, py))
