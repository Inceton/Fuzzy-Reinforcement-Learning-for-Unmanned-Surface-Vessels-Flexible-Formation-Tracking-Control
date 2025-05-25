import numpy as np
import parameter

n = parameter.n
ref = parameter.ref
a = parameter.a
begin = parameter.begin
end = parameter.end
foot = parameter.foot
gamma = parameter.gamma
x = np.zeros((n - 2, 3))


def formation(b):
    for j in range(0, 20):
        for i in range(0, n - 2):
            if j == 0:
                x[i] = ref[i + 1][:, b - 1]
                if i == 0:
                    x[i] = x[i] + gamma * (ref[i][:, b] + x[i + 1] - 2 * x[i])
                elif i == n - 3:
                    x[i] = x[i] + gamma * (ref[i + 2][:, b] + x[i - 1] - 2 * x[i])
                else:
                    x[i] = x[i] + gamma * (x[i - 1] + x[i + 1] - 2 * x[i])
            elif j == 19:
                if b != parameter.end - parameter.foot:
                    if i == 0:
                        x[i] = x[i] + gamma * (ref[i][:, b] + x[i + 1] - 2 * x[i])
                    elif i == n - 3:
                        x[i] = x[i] + gamma * (ref[i + 2][:, b] + x[i - 1] - 2 * x[i])
                    else:
                        x[i] = x[i] + gamma * (x[i - 1] + x[i + 1] - 2 * x[i])
                    ref[i + 1][:, b] = x[i]
                else:
                    if i == 0:
                        x[i] = x[i] + gamma * (ref[i][:, b] + x[i + 1] - 2 * x[i])
                    elif i == n - 3:
                        x[i] = x[i] + gamma * (ref[i + 2][:, b] + x[i - 1] - 2 * x[i])
                    else:
                        x[i] = x[i] + gamma * (x[i - 1] + x[i + 1] - 2 * x[i])
            else:
                if i == 0:
                    x[i] = x[i] + gamma * (ref[i][:, b] + x[i + 1] - 2 * x[i])
                elif i == n - 3:
                    x[i] = x[i] + gamma * (ref[i + 2][:, b] + x[i - 1] - 2 * x[i])
                else:
                    x[i] = x[i] + gamma * (x[i - 1] + x[i + 1] - 2 * x[i])
