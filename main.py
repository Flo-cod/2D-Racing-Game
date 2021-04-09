import pygame
from PIL import Image
import math
import modu
# Initialising
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Race")
clock = pygame.time.Clock()

# Background
filename = "backgroundupdate.png"
img = Image.open(filename)

back = pygame.image.load("backgroundupdate.png")
# Car
carimg = pygame.image.load("car.png")
got = "no"
gotten = False
changed = False
x_time = 20
y_time = 20
carx = 300
cary = 95
car_change = 0
angle = 270
angle_change = 0
player_out = False
player_won = False
player_won_possible = True
player_out_possible = True
# Time
font = pygame.font.Font("freesansbold.ttf", 40)
font2 = pygame.font.Font("freesansbold.ttf", 150)
font3 = pygame.font.Font("freesansbold.ttf", 100)
font4 = pygame.font.Font("freesansbold.ttf", 60)


def show_time(milliseconds, x ,y):
    time = font.render("Time: " + str(int((milliseconds/1000))), True, (255, 255, 255))
    screen.blit(time, (x, y))


def show_end(mills, won):
    if not won:
        gameover = font2.render("Game Over", True, (255, 255, 255))
        screen.blit(gameover, (70, 220))
    if won:


        wonner = font2.render("Finished!", True, (255, 255, 255))
        screen.blit(wonner, (130, 120))
        timer = font3.render("Time:" + str(float((mills/1000))) + "s", True, (255, 255, 255))
        screen.blit(timer, (280, 240))


def show_records(first, second, third):
    if underline == 1:
        firste = font4.render("1st: " + str(first) + "s", True, (255, 0, 0))
        seconde = font4.render("2nd: " + str(second) + "s", True, (255, 255, 255))
        thirde = font4.render("3rd: " + str(third) + "s", True, (255, 255, 255))
    elif underline == 2:
        firste = font4.render("1st: " + str(first) + "s", True, (255, 255, 255))
        seconde = font4.render("2nd: " + str(second) + "s", True, (255, 0, 0))
        thirde = font4.render("3rd: " + str(third) + "s", True, (255, 255, 255))
    elif underline == 3:
        firste = font4.render("1st: " + str(first) + "s", True, (255, 255, 255))
        thirde = font4.render("3rd: " + str(third) + "s", True, (255, 0, 0))
        seconde = font4.render("2nd: " + str(second) + "s", True, (255, 255, 255))
    else:
        firste = font4.render("1st: " + str(first) + "s", True, (255, 255, 255))
        seconde = font4.render("2nd: " + str(second) + "s", True, (255, 255, 255))
        thirde = font4.render("3rd: " + str(third) + "s", True, (255, 255, 255))
    screen.blit(firste, (320, 350))
    screen.blit(seconde, (320, 400))
    screen.blit(thirde, (320, 450))
def show(x, y, surface, screen):
    screen.blit(surface, (x, y))


while True:
    if pygame.event.get(pygame.QUIT): break
    # Background
    screen.blit(back,(0, 0))
    if player_out:
        if player_out_possible:
            if pygame.event.get(pygame.QUIT): break
            mills = pygame.time.get_ticks()
            x_time = 1000
            y_time = 1000
            screen.fill((0, 0, 0))
            player_won_possible = False
            show_end(mills, False)

    if player_won:
        if player_won_possible:
            if got == "no":
                miller = pygame.time.get_ticks()
                got = "notnoyousackgesicht"
            x_time = 1000
            y_time = 1000
            show_end(miller, True)
            if not changed:
                first, second, third, underline = modu.recordsetting(miller)
                changed = True
            show_records(first, second, third)
            screen.blit(carimg, (carx, cary))
            player_out_possible = False

        if pygame.event.get(pygame.QUIT): break
    # Time
    mills = pygame.time.get_ticks()
    show_time(mills, x_time, y_time)
    # Buttons
    pygame.event.pump()
    keys = pygame.key.get_pressed()


    if keys[pygame.K_UP]:
        car_change = 2
        cary += math.cos(angle * 2 * math.pi / 360) * car_change
        carx += math.sin(angle * 2 * math.pi / 360) * car_change
    if keys[pygame.K_DOWN]:
        car_change = -2
        cary += math.cos((angle) * 2 * math.pi / 360) * car_change
        carx += math.sin((angle) * 2 * math.pi / 360) * car_change
    if keys[pygame.K_LEFT]:
        angle_change = 2
    if keys[pygame.K_RIGHT]:
        angle_change = -2
    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        car_change = 0
        angle_change = 0
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        angle_change = 0

    angle += angle_change




    img_copy = pygame.transform.rotate(carimg, angle)
    new_carx, new_cary = carx - int(img_copy.get_width() / 2), cary - int(img_copy.get_height() / 2)
    screen.blit(img_copy, (new_carx, new_cary))


    # Color Detection
    cosfront = math.cos(angle * 2 * math.pi / 360)
    sinfront = math.sin(angle * 2 * math.pi / 360)
    x_front = new_carx + 16 + (sinfront * 16)
    y_front = new_cary + 16 + (cosfront * 16)
    x_back = new_carx + 16 - (sinfront * 16)
    y_back = new_cary + 16 - (cosfront * 16)
    detected_color_front = img.getpixel((x_front, y_front))
    detected_color_back = img.getpixel((x_front, y_front))

    r, g, b = detected_color_front
    r2, g2, b2 = detected_color_back
    if g >155 and b < 100 or g2 > 155 and b2 < 100:
        player_out = True
    if r> 250 and g > 250 and b > 250 or r2 > 250 and g2 > 250 and b2 > 250:
        player_won = True
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
