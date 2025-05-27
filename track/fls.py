import numpy as np


def change_pos(speed_hat, r0, t1, p1, k1, pos_real, pos_obs, t):
    e = np.subtract(pos_real, pos_obs)
    e = e.reshape(1, -1)
    s = np.subtract(speed_hat, 0)
    s = s.reshape(1, -1)
    pos_obs_next = s @ r0 + k1 * e + (t1 @ p1).T
    pos_obs += pos_obs_next * t
    return pos_obs


def change_speed(u, t2, p2, k2, speed_obs, t):
    e = np.subtract(speed_obs, 0)
    e = e.reshape(-1, 1)
    speed_obs_next = np.add(np.subtract(u, k2 * e), t2 @ p2)
    speed_obs += speed_obs_next.T * t
    return speed_obs


def change_t1(p1, t1, pos_real, pos_obs, gamma_o1, t):
    e = np.subtract(pos_real, pos_obs)
    e = e.reshape(1, -1)
    t1_next = -gamma_o1 * t1 + (p1 @ e).T
    t1 += t1_next * t
    return t1


def change_t2(p2, t2, gamma_o2, t):
    t2_next = -gamma_o2 * (p2 @ p2.T @ t2.T).T
    t2 += t2_next * t
    return t2

