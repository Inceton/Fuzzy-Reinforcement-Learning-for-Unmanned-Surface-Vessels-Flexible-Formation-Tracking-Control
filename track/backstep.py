import numpy as np
import parameter
import usv
import fls

ref = parameter.ref
dot_ref = parameter.dot_ref
foot = parameter.foot
delay = parameter.delay

gamma_1 = parameter.gamma_1
gamma_a1 = parameter.gamma_a1
gamma_c1 = parameter.gamma_c1
gamma_2 = parameter.gamma_2
gamma_a2 = parameter.gamma_a2
gamma_c2 = parameter.gamma_c2
gamma_o1 = parameter.gamma_o1
gamma_o2 = parameter.gamma_o2
k1 = parameter.k1
k2 = parameter.k2
P1 = parameter.P1
P2 = parameter.P2
Pc1 = parameter.Pc1
Pa2 = parameter.Pa2
pos = parameter.pos
speed = parameter.speed

kp = np.diag([0.005, 0.005, 0.005])  # 位置跟踪增益
kv = np.diag([0.005, 0.005, 0.005])  # 速度跟踪增益

M = np.asmatrix(np.array([[200, 0, 0], [0, 250, 0], [0, 0, 80]]))
C = 0
D = np.asmatrix(np.array([[70, 0, 0], [0, 100, 0], [0, 0, 50]]))

alpha1_prev = np.zeros((1, 3))


def backstepping_control(j, t, R, k1, k2, t1, t2, p1, p2, pos, nu, posi):
    e1 = usv.cal_err1(posi, pos)
    if t == 0:
        dot_ref[j][:, t] = (-3 * ref[j][:, t] + 4 * ref[j][:, t + 1] - ref[j][:, t + 2]) / (4 * foot)
    elif t == 1 or t == 198:
        dot_ref[j][:, t] = (ref[j][:, t + 1] - ref[j][:, t - 1]) / (2 * foot)
    elif t == 199:
        dot_ref[j][:, t] = (3 * ref[j][:, t] - 4 * ref[j][:, t - 1] + ref[j][:, t - 2]) / (4 * foot)
    else:
        dot_ref[j][:, t] = (-ref[j][:, t - 2] + 8 * ref[j][:, t - 1] - 8 * ref[j][:, t + 1] + ref[j][:, t + 2]) / (
                12 * foot)
    alpha1 = R.T @ (-kp * e1.reshape(-1, 1) + k1 * pos.reshape(-1, 1) - (t1 @ p1) + dot_ref[j][:, t].reshape(-1, 1))
    e2 = usv.cal_err2(alpha1, nu)
    dot_alpha1 = (alpha1 - alpha1_prev.reshape(-1, 1)) / foot
    u = -kv * e2.reshape(-1, 1) - R @ e1.reshape(-1, 1) + k2 * nu.reshape(-1, 1) - (t2 @ p2)  # + dot_alpha1
    return u, alpha1


def backstepping(Agent, b, posi, t1, t2, j):
    U, alpha1_prev = backstepping_control(j, b, Agent[j].R, k1, k2, t1, t2, P1[j], P2[j],
                                          Agent[j].pos_hat, Agent[j].speed_hat, posi)

    Agent[j].pos_hat = fls.change_pos(Agent[j].speed_hat, Agent[j].R, t1, P1[j], k1, posi,
                                      Agent[j].pos_hat, delay)
    Agent[j].speed_hat = fls.change_speed(U, t2, P2[j], k2, Agent[j].speed_hat, delay)
    t1 = fls.change_t1(P1[j], t1, posi, Agent[j].pos_hat, gamma_o1, delay)
    t2 = fls.change_t2(P2[j], t2, gamma_o2, delay)

    pos[j][:, b] = Agent[j].pos_hat[0, :]
    speed[j][:, b] = Agent[j].speed_hat[0, :]
    usv.Hunter.__init__(Agent[j], pos[j][0, b], pos[j][1, b], pos[j][2, b], speed[j][0, b], speed[j][1, b],
                        speed[j][2, b])
    return t1, t2
