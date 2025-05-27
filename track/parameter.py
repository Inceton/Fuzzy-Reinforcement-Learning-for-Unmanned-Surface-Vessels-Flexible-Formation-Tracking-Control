import math
import numpy as np
import pandas as pd

switch = 1
n = 5

k1 = 10
k2 = 10
gamma_1 = 2
gamma_c1 = 4
gamma_a1 = 2
gamma_o1 = 2.4
gamma_2 = 1
gamma_c2 = 3
gamma_a2 = 2
gamma_o2 = 2.4
gamma = 0.55

begin = 1
end = 200
foot = 1
a = math.floor((end - begin) / foot) + 1
delay = 0.05


ref = [None] * n
dot_ref = [None] * n
pos = [None] * n
speed = [None] * n
T1 = [None] * n
T2 = [None] * n
P1 = [None] * n
P2 = [None] * n
Pc1 = [None] * n
Pa2 = [None] * n
Theta_a1 = [None] * n
Theta_c1 = [None] * n
Theta_a2 = [None] * n
Theta_c2 = [None] * n

d = np.array(np.zeros(n))
dx = np.zeros((n - 1, a))
dy = np.zeros((n - 1, a))

for i in range(0, n):
    ref[i] = np.zeros((3, a))
    dot_ref[i] = np.zeros((3, a))
    pos[i] = np.zeros((3, a))
    speed[i] = np.zeros((3, a))
    T1[i] = np.asmatrix(np.array([[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]]))
    T2[i] = np.asmatrix(np.array([[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]]))
    P1[i] = np.asmatrix(np.array([[0.5, 0.5, 0.5, 0.5, 0.5]])).T
    P2[i] = np.asmatrix(np.array([[0.5, 0.5, 0.5, 0.5, 0.5]])).T
    Pc1[i] = np.asmatrix(np.array([[0.5, 0.5, 0.5, 0.5, 0.5]])).T
    Pa2[i] = np.asmatrix(np.array([[0.5, 0.5, 0.5, 0.5, 0.5]])).T
    Theta_a1[i] = np.asmatrix(
        np.array([[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]]))
    Theta_c1[i] = np.asmatrix(
        np.array([[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]]))
    Theta_a2[i] = np.asmatrix(
        np.array([[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]]))
    Theta_c2[i] = np.asmatrix(
        np.array([[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]]))

r1_values = pd.read_excel(r'..\data.xlsx')
ref[0] = r1_values.values
r2_values = pd.read_excel(r'..\data2.xlsx')
ref[n - 1] = r2_values.values

if n == 5:
    pos[4][:, 0] = [-11.78, 1.67, np.random.uniform(-np.pi, np.pi)]
    pos[3][:, 0] = [-4.1, -0.5, np.random.uniform(-np.pi, np.pi)]
    pos[2][:, 0] = [1.67, 1.9, np.random.uniform(-np.pi, np.pi)]
    pos[1][:, 0] = [8.55, -3.3, np.random.uniform(-np.pi, np.pi)]
    pos[0][:, 0] = [12.4, -4.9, np.random.uniform(-np.pi, np.pi)]

    dx[:, 0] = [7.68, 5.77, 6.88, 3.85]
    dy[:, 0] = [2.17, 2.4, -5.2, -1.6]

elif n == 7:
    pos[6][:, 0] = [-11.78, 1.67, np.random.uniform(-np.pi, np.pi)]
    pos[5][:, 0] = [-9.1, 1.7, np.random.uniform(-np.pi, np.pi)]
    pos[4][:, 0] = [-4.1, -0.5, np.random.uniform(-np.pi, np.pi)]
    pos[3][:, 0] = [1.67, 1.9, np.random.uniform(-np.pi, np.pi)]
    pos[2][:, 0] = [4.47, 0.9, np.random.uniform(-np.pi, np.pi)]
    pos[1][:, 0] = [8.55, -3.3, np.random.uniform(-np.pi, np.pi)]
    pos[0][:, 0] = [12.4, -4.9, np.random.uniform(-np.pi, np.pi)]

    dx[:, 0] = [2.68, 5, 5.77, 2.8, 4.08, 3.85]
    dy[:, 0] = [0.03, -2.2, 2.4, -1, -4.2, -1.6]

elif n == 9:
    pos[8][:, 0] = [-11.78, 1.67, np.random.uniform(-np.pi, np.pi)]
    pos[7][:, 0] = [-9.1, 1.7, np.random.uniform(-np.pi, np.pi)]
    pos[6][:, 0] = [-6.5, 0.3, np.random.uniform(-np.pi, np.pi)]
    pos[5][:, 0] = [-4.1, -0.5, np.random.uniform(-np.pi, np.pi)]
    pos[4][:, 0] = [1.67, 1.9, np.random.uniform(-np.pi, np.pi)]
    pos[3][:, 0] = [4.47, 0.9, np.random.uniform(-np.pi, np.pi)]
    pos[2][:, 0] = [6.33, -1.2, np.random.uniform(-np.pi, np.pi)]
    pos[1][:, 0] = [8.55, -3.3, np.random.uniform(-np.pi, np.pi)]
    pos[0][:, 0] = [12.4, -4.9, np.random.uniform(-np.pi, np.pi)]

    dx[:, 0] = [2.68, 2.6, 2.4, 5.77, 2.8, 1.86, 2.22, 3.85]
    dy[:, 0] = [0.03, -1.4, -0.8, 2.4, -1, -2.1, -2.1, -1.6]


ref[1][:, 0] = pos[1][:, 0]
ref[2][:, 0] = pos[2][:, 0]
ref[3][:, 0] = pos[3][:, 0]
