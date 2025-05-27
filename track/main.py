import time

import ac
import usv
import smo
import backstep
import formation
import parameter
import plotting
import measure

'''
switch = 1:fls
switch = 2:smo
switch = 3:backstepping control
'''
switch = parameter.switch

begin = parameter.begin
end = parameter.end
foot = parameter.foot
delay = parameter.delay
n = parameter.n

ref = parameter.ref
pos = parameter.pos
speed = parameter.speed
T1 = parameter.T1
T2 = parameter.T2
Theta_a1 = parameter.Theta_a1
Theta_c1 = parameter.Theta_c1
Theta_a2 = parameter.Theta_a2
Theta_c2 = parameter.Theta_c2

e1a = measure.e1a
e2a = measure.e2a

Agent = []

for i in range(0, n):
    Agent.append(
        usv.Hunter(pos[i][0, 0], pos[i][1, 0], pos[i][2, 0], speed[i][0, 0], speed[i][1, 0], speed[i][2, 0]))

for t in range(begin, end, foot):
    formation.formation(t)

for t in range(begin, end, foot):
    for i in range(0, n):
        if switch == 1:
            T1[i], T2[i] = ac.fls_control_complete(Agent, t, Theta_a1[i], Theta_c1[i], Theta_a2[i], Theta_c2[i], T1[i],
                                                   T2[i], i,
                                                   ref[i][:, t - 1])
        elif switch == 2:
            smo.smo_control_complete(Agent, t, Theta_a1[i], Theta_c1[i], Theta_a2[i], Theta_c2[i], i, ref[i][:, t - 1])
        elif switch == 3:
            T1[i], T2[i] = backstep.backstepping(Agent, t, ref[i][:, t - 1], T1[i], T2[i], i)
    measure.calculate(t)
    print(t)
    for j in range(0, n):
        print(ref[j][:, t - 1])
        print(Agent[j].pos_hat)
    time.sleep(delay)

ref[1][:, 199] = ref[1][:, 198]
ref[2][:, 199] = ref[2][:, 198]
ref[3][:, 199] = ref[3][:, 198]

plotting.plot_tracking(pos, ref)
plotting.plot_speed(measure.uv)
plotting.plot_xgap(parameter.dx)
plotting.plot_ygap(parameter.dy)
plotting.plot_error(e1a, e2a)
plotting.plot_error_all()
