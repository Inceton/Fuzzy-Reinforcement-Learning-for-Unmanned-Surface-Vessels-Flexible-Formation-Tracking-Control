import numpy as np
from math import sin, cos


class Hunter:

    def __init__(self, x_hat, y_hat, ang_hat, u_hat, v_hat, r_hat):
        self.x_hat = x_hat
        self.y_hat = y_hat
        self.ang_hat = ang_hat
        self.u_hat = u_hat
        self.v_hat = v_hat
        self.r_hat = r_hat
        self.pos_hat = np.asmatrix(np.array([x_hat, y_hat, ang_hat]))
        self.speed_hat = np.asmatrix(np.array([u_hat, v_hat, r_hat]))
        self.R = np.asmatrix(np.array([[cos(ang_hat), -sin(ang_hat), 0], [sin(ang_hat), cos(ang_hat), 0], [0, 0, 1]]))


class Invader:

    def __init__(self, x, y, ang):
        self.x = x
        self.y = y
        self.ang = ang
        self.pos = np.array([x, y, ang]).T


class Follower:

    def __init__(self, x, y, ang):
        self.x = x
        self.y = y
        self.ang = ang
        self.pos = np.asmatrix(np.array([x, y, ang]))


# 计算位置观测与实际的误差
def cal_err1(pos_reference, pos):
    p = np.subtract(pos, 0)
    p = p.reshape(1, -1)
    pr = np.subtract(pos_reference, 0)
    pr = pr.reshape(1, -1)
    e1 = np.subtract(p, pr)
    return e1


# 计算速度观测与实际的误差
def cal_err2(actor1, speed):
    s = np.subtract(speed, 0)
    s = s.reshape(1, -1)
    actor1 = actor1.reshape(1, -1)
    e2 = np.subtract(s, actor1)
    return e2


# 计算actor与critic的值
def cal_actor_critic(e, ps, tc, ta, g, r, i):
    e = e.reshape(-1, 1)
    ps = np.array(ps)
    ps = ps.reshape(-1, 1)
    tc = tc.reshape(3, -1)
    ta = ta.reshape(3, -1)
    critic = 2 * g * e + tc @ ps
    if i == 0:
        actor = (-g * e) - 0.5 * (ta @ ps)
    else:
        actor = (-g * (r @ e)) - 0.5 * r @ (ta @ ps)
    return actor


# 训练Tc和Ta
def train_T(e, ps, tc, ta, gc, ga, t):
    e = e.reshape(-1, 1)
    ps = ps.reshape(-1, 1)
    tc = tc.reshape(3, -1)
    ta = ta.reshape(3, -1)
    Tc_next = -0.5 * (ps @ e.T) - np.multiply(((ps @ ps.T) @ tc.T), gc)
    tc = np.add(Tc_next.T*t, tc)
    Ta_next = - ga * (ps @ ps.T) @ (ta - tc).T
    ta = np.add(Ta_next.T*t, ta)
    return tc, ta


