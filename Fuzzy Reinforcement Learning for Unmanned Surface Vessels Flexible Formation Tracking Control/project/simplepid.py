import usv
import parameter
import fls

k1 = parameter.k1
k2 = parameter.k2
P1 = parameter.P1
P2 = parameter.P2
gamma_o1 = parameter.gamma_o1
gamma_o2 = parameter.gamma_o2
pos = parameter.pos
speed = parameter.speed
delay = parameter.delay


class PIDController:
    def __init__(self, Kp=1.0, Ki=0.1, Kd=0.01, setpoint=0, output_limits=(None, None)):
        """
        PID控制器初始化
        :param Kp: 比例系数
        :param Ki: 积分系数
        :param Kd: 微分系数
        :param setpoint: 设定值（目标值）
        :param output_limits: 输出限制元组（最小值, 最大值）
        """
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.output_limits = output_limits

        self.last_error = 0.0
        self.integral = 0.0
        self.last_time = None

    def update(self, e, dt):
        """
        更新PID输出
        :param current_value: 当前测量值
        :param dt: 时间间隔（秒），若为None则自动计算
        :return: 控制输出值
        """
        # 比例项
        p_term = self.Kp * e

        # 积分项（带抗饱和机制）
        self.integral += e * dt
        i_term = self.Ki * self.integral

        # 微分项（带噪声抑制的一阶差分）
        if dt > 0:
            d_term = self.Kd * (e - self.last_error) / dt
        else:
            d_term = 0.0
        self.last_error = e

        # 总输出
        output = p_term + i_term + d_term
        output = output.reshape(-1, 1)

        # 应用输出限制
        '''
        min_output, max_output = self.output_limits
        if min_output is not None and output < min_output:
            output = min_output
        if max_output is not None and output > max_output:
            output = max_output
        '''

        return output


def pid(Agent, pos, j):
    controller = PIDController()
    e1 = usv.cal_err1(pos, Agent[j].pos_hat)
    alpha1 = controller.update(e1, delay)
    e2 = usv.cal_err2(alpha1, Agent[j].speed_hat)
    tau = controller.update(e2, delay)
    return tau


def pid_control(Agent, b, t1, t2, posi, j):
    U = pid(Agent, posi, j)
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
