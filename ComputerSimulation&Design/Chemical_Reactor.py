import pygame

MX = 500

a = [0.0] * MX
b = [0.0] * MX
c = [0.0] * MX
mx = 0.0

def main():
    dt = .10
    time = MX
    in_ = 0
    i = 0
    k1,k2 = .05, .05
    a[0],b[0] = 1, .5

    # k1, k2 = map(float, input("Enter the rate of reaction (k1 k2): ").split())
    # a[0], b[0] = map(float, input("Enter initial amount of A and B: ").split())

    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    clock = pygame.time.Clock()

    print("........................................")
    print("|  Time   |  A(t)   |   B(t)  |  C(t)  |")
    print("........................................")

    print(f"|  {i:.2f}  |  {a[0]:.2f}  |  {b[0]:.2f}  | {c[0]:.2f}  |")
    mx = max(a[in_], max(b[in_], c[in_]))

    for i in range(1, time, 1):
        in_ += 1
        a[in_] = a[in_ - 1] + (k2 * c[in_ - 1] - k1 * a[in_ - 1] * b[in_ - 1]) * dt
        b[in_] = b[in_ - 1] + (k2 * c[in_ - 1] - k1 * a[in_ - 1] * b[in_ - 1]) * dt
        c[in_] = c[in_ - 1] + (2 * k1 * a[in_ - 1] * b[in_ - 1] - 2 * k2 * c[in_ - 1]) * dt

        print(f"|  {dt*i:.2f}  |  {a[in_]:.2f}  |  {b[in_]:.2f}  | {c[in_]:.2f}  |")
        mx = max(a[in_], max(b[in_], c[in_]))

    print("........................................")

    # Graphics part:

    inc = 70
    ymx = 600
    fctx = (800 - inc) / in_
    fcty = (ymx - inc * 5) / mx

    f = pygame.font.get_default_font()
    font = pygame.font.SysFont(f , 25)

    text1 = font.render('A', True, (255,255,255))
    text2 = font.render('B', True, (255,255,255))
    text3 = font.render('C', True, (255,255,255))
    text4 = font.render('Time -->', True, (255,255,255))

    screen.fill((60, 60, 60))
    pygame.draw.line(screen, (0,0,0), (inc,ymx-inc), (inc,inc))
    pygame.draw.line(screen, (0,0,0), (inc,ymx-inc), (900-inc,ymx-inc))
    screen.blit(text1, (30,150))
    screen.blit(text2, (30,320))
    screen.blit(text3, (30,500))
    screen.blit(text4, (350,550))

    running = True
    

    for j in range(1, in_ + 1):
        pygame.draw.line(screen, (0, 255, 0),
                         (int(inc + (j - 1) * fctx), int(ymx - inc - a[j - 1] * fcty)),
                         (int(inc + j * fctx), int(ymx - inc - a[j] * fcty)))

        pygame.draw.line(screen, (255, 255, 255),
                         (int(inc + (j - 1) * fctx), int(ymx - inc - b[j - 1] * fcty)),
                         (int(inc + j * fctx), int(ymx - inc - b[j] * fcty)))

        pygame.draw.line(screen, (255, 0, 0),
                         (int(inc + (j - 1) * fctx), int(ymx - inc - c[j - 1] * fcty)),
                         (int(inc + j * fctx), int(ymx - inc - c[j] * fcty)))

        pygame.display.flip()
        clock.tick(90)
        

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
