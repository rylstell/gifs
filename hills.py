import pygame
import math
from random import randint
from opensimplex import OpenSimplex




def main():

    WIDTH, HEIGHT = 500, 500
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    FPS = 30

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    num_frames = 120
    frame_count = 0
    output_dir = "hills_output"
    save_imgs = False

    center = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
    sim = OpenSimplex(seed=randint(0, 2_000_000_000))
    noise_scale = 0.015
    noise_strength_max = 250
    pts_per_line = 80
    num_lines = 60
    line_spacing = HEIGHT / num_lines
    circle_radius = 220


    while running:

        angle = frame_count / num_frames * math.pi * 2

        lines = []
        for i in range(num_lines + 1):
            y = line_spacing * i
            if i == num_lines:
                y -= 1
            line_pts = []
            for j in range(pts_per_line):
                x = j / (pts_per_line - 1) * WIDTH
                pt = pygame.Vector2(x, y)
                dist = pt.distance_to(center)
                if dist > circle_radius:
                    dist = circle_radius
                noise_strength = (1 - dist / circle_radius) * noise_strength_max
                noise_offset = noise_strength * sim.noise4((x + i * 100) * noise_scale, (y + i * 100) * noise_scale, math.cos(angle), math.sin(angle))
                pt.y += noise_offset
                line_pts.append(pt)
            line_pts.append(pygame.Vector2(WIDTH + 1, HEIGHT + 1))
            line_pts.append(pygame.Vector2(-1, HEIGHT + 1))
            lines.append(line_pts)

        window.fill(BLACK)
        for line_pts in lines:
            pygame.draw.polygon(window, BLACK, line_pts, width=0)
            pygame.draw.lines(window, WHITE, False, line_pts, width=1)
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
