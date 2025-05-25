import usv
import fls
import parameter

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
delay = parameter.delay

def actor_critic(Agent, ps1, tc1, ta1, ps2, tc2, ta2, j, pos, r):
    e1 = usv.cal_err1(pos, Agent[j].pos_hat)
    alpha1 = usv.cal_actor_critic(e1, ps1, tc1, ta1, gamma_1, r, 1)
    Tc1, Ta1 = usv.train_T(e1, ps1, tc1, ta1, gamma_c1, gamma_a1, delay)
    e2 = usv.cal_err2(alpha1, Agent[j].speed_hat)
    U = usv.cal_actor_critic(e2, ps2, tc2, ta2, gamma_2, r, 0)
    Tc2, Ta2 = usv.train_T(e2, ps2, tc2, ta2, gamma_c2, gamma_a2, delay)
    return U, Tc1, Ta1, Tc2, Ta2


def fls_control_complete(Agent, b, tc1, ta1, tc2, ta2, t1, t2, j, posi):
    U, tc1, ta1, tc2, ta2 = actor_critic(Agent, Pc1[j], tc1, ta1, Pa2[j], tc2, ta2, j, posi, Agent[j].R)
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
