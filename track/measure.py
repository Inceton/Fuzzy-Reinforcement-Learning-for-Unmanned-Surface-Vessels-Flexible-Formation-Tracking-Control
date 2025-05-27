import numpy as np
import pandas as pd
import math
import parameter

a = parameter.a
n = parameter.n
pos = parameter.pos
speed = parameter.speed
ref = parameter.ref
switch = parameter.switch

e1a = np.zeros((3, a - 1))
e2a = np.zeros((3, a - 1))
uv = np.zeros((n, a))


def calculate(b):
    e1a[:, b - 1] = abs(pos[0][:, b] - ref[0][:, b])
    e2a[:, b - 1] = abs(pos[n - 1][:, b] - ref[n - 1][:, b])
    for i in range(0, n):
        if b >= 1:
            speed[i][:, b] = pos[i][:, b] - pos[i][:, b - 1]
            uv[i, b] = math.sqrt(speed[i][0, b] ** 2 + speed[i][1, b] ** 2)
        if i < n - 1:
            parameter.dx[i, b] = pos[i + 1][0, b] - pos[i][0, b]
            parameter.dy[i, b] = pos[i + 1][1, b] - pos[i][1, b]
        uv[i, 0] = uv[i, 1]


def save_data_to_csv(data):
    column=[3]
    df = pd.DataFrame(columns = column,data = data[1])
    df.to_csv('backstepping.csv', index=False)