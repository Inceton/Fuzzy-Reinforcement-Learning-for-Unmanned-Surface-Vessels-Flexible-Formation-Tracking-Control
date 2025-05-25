import numpy as np
import ac
import usv
import parameter

rho1 = 10
rho2 = 10
k = 4
epsilon = 0.1
integral = np.zeros(3)
M = np.asmatrix(np.array([[200, 0, 0], [0, 250, 0], [0, 0, 80]]))
C = 0
D = np.asmatrix(np.array([[70, 0, 0], [0, 100, 0], [0, 0, 50]]))

k1 = parameter.k1
k2 = parameter.k2
P1 = parameter.P1
P2 = parameter.P2
Pc1 = parameter.Pc1
Pa2 = parameter.Pa2
pos = parameter.pos
speed = parameter.speed
delay = parameter.delay

def update(tau, zeta_hat, nu_hat, zeta_ref, dt, R):
    # 转换为列向量
    nu_hat_col = nu_hat.reshape(-1, 1)
    zeta_hat_col = zeta_hat.reshape(-1, 1)
    integral_col = integral.reshape(-1, 1)
    zeta_ref_col = zeta_ref.reshape(-1, 1)

    # 计算s和sat
    s = zeta_hat_col - zeta_ref_col + k * integral_col
    sat = np.clip(s / epsilon, -1.0, 1.0)

    zeta_dot = R @ nu_hat_col - rho1 * sat
    zeta_hat_col += zeta_dot * dt
    zeta_hat = zeta_hat_col.reshape(1, -1)

    nu_dot = np.linalg.inv(M) @ (tau.reshape(-1, 1) - (C * nu_hat).reshape(-1, 1) - D @ nu_hat_col) - rho2 * sat
    nu_hat_col += nu_dot * dt
    nu_hat = nu_hat_col.reshape(1, -1)

    return zeta_hat, nu_hat

def smo_control_complete(Agent, b, tc1, ta1, tc2, ta2, j, posi):
    U, tc1, ta1, tc2, ta2 = ac.actor_critic(Agent, Pc1[j], tc1, ta1, Pa2[j], tc2, ta2, j, posi, Agent[j].R)
    Agent[j].pos_hat, Agent[j].speed_hat = update(U, Agent[j].pos_hat, Agent[j].speed_hat, posi, delay, Agent[j].R)

    pos[j][:, b] = Agent[j].pos_hat[0, :]
    speed[j][:, b] = Agent[j].speed_hat[0, :]
    usv.Hunter.__init__(Agent[j], pos[j][0, b], pos[j][1, b], pos[j][2, b], speed[j][0, b], speed[j][1, b],
                        speed[j][2, b])