import numpy as np
from math import tan

class Projection:
    def __init__(self, app):
        near = app.camera.near_plane
        far = app.camera.far_plane
        right = tan(app.camera.h_fov / 2)
        left = -right
        top = tan(app.camera.v_fov / 2)
        bottom = -top

        m00 = 2 / (right - left)
        m11 = 2 / (top - bottom)
        m22 = (far + near) / (far - near)
        m32 = -2 * near * far / (far - near)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        hw, hh = app.hw, app.hh
        self.to_screen_matrix = np.array([
            [hw, 0, 0, 0],
            [0, -hh, 0, 0],
            [0, 0, 1, 0],
            [hw, hh, 0, 1]
        ])
