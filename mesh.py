import pygame
import math
from random import randint, random
from opensimplex import OpenSimplex



class Point(pygame.Vector2):
    def __init__(self, x, y, center_dist):
        super().__init__(x, y)
        self.center_dist = center_dist



def main():

    WIDTH, HEIGHT = 500, 500
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    GRAY_220 = pygame.Color(220, 220, 220)

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    num_frames = 120
    frame_count = 0
    save_imgs = False
    output_dir = "mesh_output"

    center = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
    sim = OpenSimplex(seed=randint(0, 2_000_000_000))
    noise_scale = 0.015
    circle_radius = 200
    point_radius = 200
    num_points = 10000
    points = []

    for _ in range(num_points):
        angle = random() * math.pi * 2
        r = circle_radius * math.sqrt(random())
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        point = pygame.Vector2(x, y)
        points.append(Point(x, y, r))


    while running:

        noise_angle = math.pi * 2 * (frame_count / num_frames)

        draw_points = []
        for pt in points:
            noise_point = pt * noise_scale
            noise_strength = (1 - pt.center_dist / circle_radius) * point_radius
            nosie_offset = noise_strength * pygame.Vector2(
                sim.noise4(noise_point.x, noise_point.y, math.cos(noise_angle), math.sin(noise_angle)),
                sim.noise4(noise_point.x + 50, noise_point.y + 50, math.cos(noise_angle), math.sin(noise_angle))
            )
            pixel_pos = pt + nosie_offset
            draw_points.append(pygame.Vector2(pixel_pos.x, pixel_pos.y))

        window.fill(BLACK)
        pygame.draw.circle(window, GRAY_220, center, circle_radius, width=1)
        for pt in draw_points:
            x, y = pt + center
            window.set_at((int(x), int(y)), GRAY_220)
        pygame.display.update()

        if save_imgs and frame_count < num_frames:
            print("frame:", frame_count + 1)
            pygame.image.save(window, f"{output_dir}/img-{frame_count:0>3}.png")
        frame_count += 1
        if save_imgs and frame_count >= num_frames:
            print("done")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
