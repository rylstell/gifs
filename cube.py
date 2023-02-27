import pygame
import math
from random import randint
import numpy as np




class Color:
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    GRAY_100 = pygame.Color(100, 100, 100)
    GRAY_240 = pygame.Color(240, 240, 240)




class Face:
    def __init__(self):
        self.points = []
        self.normal = None
        self.color = Color.WHITE





def create_box_faces():
    faces = []

    left_face = Face()
    left_face.points.append(np.array([-0.5, -0.5, -0.5]))
    left_face.points.append(np.array([-0.5, -0.5, 0.5]))
    left_face.points.append(np.array([-0.5, 0.5, 0.5]))
    left_face.points.append(np.array([-0.5, 0.5, -0.5]))
    left_face.normal = np.array([-1, 0, 0])
    faces.append(left_face)

    right_face = Face()
    right_face.points.append(np.array([0.5, -0.5, -0.5]))
    right_face.points.append(np.array([0.5, -0.5, 0.5]))
    right_face.points.append(np.array([0.5, 0.5, 0.5]))
    right_face.points.append(np.array([0.5, 0.5, -0.5]))
    right_face.normal = np.array([1, 0, 0])
    right_face.color = pygame.Color(230, 228, 181)
    faces.append(right_face)

    top_face = Face()
    top_face.points.append(np.array([0.5, -0.5, -0.5]))
    top_face.points.append(np.array([0.5, -0.5, 0.5]))
    top_face.points.append(np.array([-0.5, -0.5, 0.5]))
    top_face.points.append(np.array([-0.5, -0.5, -0.5]))
    top_face.normal = np.array([0, -1, 0])
    top_face.color = pygame.Color(126, 186, 180)
    faces.append(top_face)

    bottom_face = Face()
    bottom_face.points.append(np.array([0.5, 0.5, -0.5]))
    bottom_face.points.append(np.array([0.5, 0.5, 0.5]))
    bottom_face.points.append(np.array([-0.5, 0.5, 0.5]))
    bottom_face.points.append(np.array([-0.5, 0.5, -0.5]))
    bottom_face.normal = np.array([0, 1, 0])
    faces.append(bottom_face)

    front_face = Face()
    front_face.points.append(np.array([0.5, -0.5, -0.5]))
    front_face.points.append(np.array([0.5, 0.5, -0.5]))
    front_face.points.append(np.array([-0.5, 0.5, -0.5]))
    front_face.points.append(np.array([-0.5, -0.5, -0.5]))
    front_face.normal = np.array([0, 0, -1])
    front_face.color = pygame.Color(63, 85, 129)
    faces.append(front_face)

    back_face = Face()
    back_face.points.append(np.array([0.5, -0.5, 0.5]))
    back_face.points.append(np.array([0.5, 0.5, 0.5]))
    back_face.points.append(np.array([-0.5, 0.5, 0.5]))
    back_face.points.append(np.array([-0.5, -0.5, 0.5]))
    back_face.normal = np.array([0, 0, 1])
    faces.append(back_face)

    return faces





def create_identity_mat():
    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

def rotation_mat_x(angle):
    return np.array([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ])

def rotation_mat_y(angle):
    return np.array([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])

def rotation_mat_z(angle):
    return np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
        [0, 0, 1],
    ])





class Box:

    def __init__(self):
        self.faces = create_box_faces()
        self.translate_vec = np.array([0, 0, 0], dtype=np.float64)
        self.scale_mat = create_identity_mat()
        self.rotation_mat = create_identity_mat()
        self.post_trans_rotation_mat = create_identity_mat()

    def get_position(self):
        return np.array(self.translate_vec)

    def translate(self, vec):
        self.translate_vec += vec

    def translate_x(self, val):
        self.translate_vec[0] += val

    def translate_y(self, val):
        self.translate_vec[1] += val

    def translate_z(self, val):
        self.translate_vec[2] += val

    def set_size(self, size):
        self.scale_mat = np.array([
            [size, 0, 0],
            [0, size, 0],
            [0, 0, size]
        ])

    def set_size_x(self, size):
        self.scale_mat[0][0] = size

    def set_size_y(self, size):
        self.scale_mat[1][1] = size

    def set_size_z(self, size):
        self.scale_mat[2][2] = size

    def rotate(self, mat):
        self.rotation_mat = np.matmul(mat, self.rotation_mat)

    def rotate_x(self, angle):
        mat = rotation_mat_x(angle)
        self.rotation_mat = np.matmul(mat, self.rotation_mat)

    def rotate_y(self, angle):
        mat = rotation_mat_y(angle)
        self.rotation_mat = np.matmul(mat, self.rotation_mat)

    def rotate_z(self, angle):
        mat = rotation_mat_z(angle)
        self.rotation_mat = np.matmul(mat, self.rotation_mat)

    def post_trans_rotate_x(self, angle):
        mat = rotation_mat_x(angle)
        self.post_trans_rotation_mat = np.matmul(mat, self.post_trans_rotation_mat)

    def post_trans_rotate_y(self, angle):
        mat = rotation_mat_y(angle)
        self.post_trans_rotation_mat = np.matmul(mat, self.post_trans_rotation_mat)

    def post_trans_rotate_z(self, angle):
        mat = rotation_mat_z(angle)
        self.post_trans_rotation_mat = np.matmul(mat, self.post_trans_rotation_mat)

    def draw(self, window, camera, center2d):
        mat = np.matmul(self.rotation_mat, self.scale_mat)
        for face in self.faces:
            normal = np.matmul(self.post_trans_rotation_mat, np.matmul(self.rotation_mat, face.normal))
            if camera.dot(normal) > 0:
                draw_face_pts = []
                for pt in face.points:
                    draw_pt = np.matmul(self.post_trans_rotation_mat, np.matmul(mat, pt) + self.translate_vec)
                    draw_face_pts.append(np.array([draw_pt[0], draw_pt[1]]) + center2d)
                pygame.draw.polygon(window, face.color, draw_face_pts, width=0)




def main():

    WIDTH, HEIGHT = 500, 500
    FPS = 30

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    center2d = np.array([WIDTH / 2, HEIGHT / 2])
    running = True
    frame_count = 0

    save_fames = False
    total_frames = 60
    output_dir = "cube_output"
    camera = np.array([0, 0, -200])
    total_size = 300
    grid_size = 16
    min_box_height = 70
    max_box_height = 270

    box_size = total_size / grid_size
    boxes = []
    for i in range(grid_size):
        for j in range(grid_size):
            x = -total_size / 2 + box_size / 2 + i * box_size
            z = -total_size / 2 + box_size / 2 + j * box_size
            pos = np.array([x, 0, z])
            box = Box()
            box.set_size(box_size)
            box.translate(pos)
            box.post_trans_rotate_y(math.pi / 4)
            box.post_trans_rotate_x(math.pi / 5)
            boxes.append(box)

    boxes.sort(key=lambda b: b.get_position()[2], reverse=True)
    max_pos = np.array([-total_size / 2 + box_size / 2, -total_size / 2 + box_size / 2])
    max_mag_squared = max_pos.dot(max_pos)


    while running:

        clock.tick(FPS)

        t = -math.pi * 2 * frame_count / total_frames

        for box in boxes:
            pos = box.get_position()
            mag_squared = pos.dot(pos)
            angle = t + math.pi * 2 * (mag_squared / max_mag_squared)
            box.set_size_y(70 + 200 * (math.sin(angle) + 1) / 2)

        window.fill(Color.GRAY_240)
        for box in boxes:
            box.draw(window, camera, center2d)
        pygame.display.update()

        if save_fames and frame_count < total_frames:
            pygame.image.save(window, f"{output_dir}/img-{frame_count:0>3}.png")
            if frame_count == total_frames - 1:
                print("done")
        frame_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
