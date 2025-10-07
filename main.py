import sys, pygame, math, time
from plot import *

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

pygame.init()

screen = pygame.display.set_mode((1152, 864))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

px = 24 # ile px w 1 metrze
fps = 60 # liczba klatek na sekunde

"""
roc = 904 # ro cieczy [kg/m^3]
rop = 84 # ro pilki [kg/m^3]
R = 0.038 # srednica pilki [m]
Rp = R/2 # promien pilki [m]
g = 9.81 # przyspieszenie ziemskie [m/s^2]
eta = 0.056 # lepkosc [Pa*s]
"""
roc = float(input("Podaj gestosc cieczy [kg/m^3]"))
rop = float(input("Podaj gestosc kuli [kg/m^3]"))
R = float(input("Podaj srednice kuli [m]"))
g = float(input("Podaj przyspieszenie grawitacyjne [m/s^2]"))
eta = float(input("Podaj lepkosc cieczy [Pa*s]"))

Rp = R/2 # promien pilki [m]

x, y = 288, 0
vel_x, vel_y = 0, 0

Vp = ((4/3) * math.pi * Rp*Rp*Rp) # objetosc pilki [m^3]
m = rop * Vp # masa pilki [kg]
b = 6 * math.pi * eta * Rp

plot_a_y = Plotter(556, 412, "a = ")
plot_vel_y = Plotter(556, 412, "Vy = ")

a_vals = []
vel_y_vals = []

time_scale = 0.5
t1 =time.time()
dt = 1/fps

a = g*(1-(roc/rop))-(b/m)*vel_y
vel_y += a * dt

a_vals.append(a)
vel_y_vals.append(vel_y)

running = True
while running:
    dt = time.time() - t1
    t1 = time.time()

    dt *= time_scale

    screen.fill((255,255,255))

    temp_i = 0
    for i in range((864//(px*2)) + 1):
        pygame.draw.rect(screen, (128,128,128), (0, temp_i - (y%(px*2)), 1152, px))
        temp_i += px * 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            time_scale += event.y * 0.1
            time_scale = clamp(time_scale, 0.1, 5)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    a = g*(1-(roc/rop))-(b/m)*vel_y
    vel_y += a * dt
    y += vel_y * px * dt

    a_vals.append(a)
    vel_y_vals.append(vel_y)

    plot_a_y.update(a_vals)
    plot_vel_y.update(vel_y_vals)
    
    screen.blit(plot_a_y.surf, (576, 432))
    screen.blit(plot_vel_y.surf, (576, 0))

    screen.blit(font.render(str(round(time_scale * 100, 0))+"%", True, (0,255,0)), (0,0))

    pygame.draw.circle(screen, (255, 0, 0), (288, 432), Rp * px * 10)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
