import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import parameter

n = parameter.n
switch = parameter.switch

mpl.rcParams['font.family'] = 'sans-serif'  # 无衬线字体
mpl.rcParams['font.sans-serif'] = ['Arial']  # 优先使用Arial
mpl.rcParams['axes.linewidth'] = 1  # 坐标轴边框粗细
mpl.rcParams['xtick.major.width'] = 1  # x轴主刻度线粗细
mpl.rcParams['ytick.major.width'] = 1  # y轴主刻度线粗细

# colors = ['#4B5EC2', '#D54C44', '#2A9D8F', '#8A6EAD', '#B08968']
colors = plt.cm.viridis(np.linspace(0, 1, n))  # 使用颜色映射来生成平滑的颜色

point1 = [15.5, 21.0, 26.6, 33.0, 38.0, 45.0, 56.0, 69.0, 80.0, 86.0, 97.5, 108.4, 116.8, 129.8]
y_point1 = [-6.5, -16.0, -22.4, -32.0, -37.6, -43.8, -50.0, -55.8, -58.0, -58.2, -57.2, -55.3, -52.2, -44.6]
point2 = [-14.0, -9.0, -5.0, -0.5, 4.0, 8.0, 14.0, 21.5, 26.0, 34.0, 59.0, 77.0, 91.0, 114.9]
y_point2 = [-6.0, -18.0, -24.8, -32.5, -40.5, -49.5, -60.0, -74.0, -78.0, -81.5, -85.0, -84.5, -82.6, -76.9]


def plot_tracking(pos, ref):
    plt.figure(1, figsize=(8, 6))
    plt.scatter(point1, y_point1, marker='o', facecolors='none', edgecolors='green', s=10, label='Inflection Points')
    plt.scatter(point2, y_point2, marker='o', facecolors='none', edgecolors='green', s=10)

    plt.plot(ref[0][0], ref[0][1], color=colors[4], linewidth=1.5, label='Planned Path')
    plt.plot(ref[n - 1][0], ref[n - 1][1], color=colors[4], linewidth=1.5)

    for i in range(0, n):
        if i == 0:
            plt.plot(pos[i][0], pos[i][1], linestyle='-.', linewidth=0.5, color=colors[1], label='Tracking Path')
        else:
            plt.plot(pos[i][0], pos[i][1], linestyle='-.', linewidth=0.5, color=colors[1])
    plt.xlabel('X (m)', fontsize=12)
    plt.ylabel('Y (m)', fontsize=12)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.legend(prop={'size': 10}, frameon=False, loc='upper right', bbox_to_anchor=(1, 1), handlelength=1.5)
    # plt.show()
    if switch == 1:
        plt.savefig(f'usv_track_fls_n={n}.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 2:
        plt.savefig(f'usv_track_smo.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 3:
        plt.savefig(f'usv_track_backstepping.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 4:
        plt.savefig(f'usv_track_pid.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图


def plot_speed(v):
    plt.figure(2, figsize=(8, 6))
    ax = plt.gca()
    for i in range(0, n):
        plt.plot(v[i, :], alpha=0.8, color=colors[i], label=f'USV{i + 1}')
    plt.xlabel('Times (s)', fontsize=12)
    plt.ylabel('Speed of USVs (m/s)', fontsize=12)
    plt.xticks(fontsize=10)  # 刻度字体大小
    plt.yticks(fontsize=10)
    ax.grid(True, color='lightgrey', linestyle='--', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.legend(prop={'size': 10}, frameon=False, loc='upper right', bbox_to_anchor=(1, 1), handlelength=1.5)
    # plt.show()
    if switch == 1:
        plt.savefig(f'usv_speed_fls_n={n}.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 2:
        plt.savefig(f'usv_speed_smo.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 3:
        plt.savefig(f'usv_speed_backstepping.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 4:
        plt.savefig(f'usv_speed_pid.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图


def plot_xgap(x):
    plt.figure(3, figsize=(8, 6))
    ax = plt.gca()
    for i in range(0, n - 1):
        plt.plot(x[i, :], color=colors[i], linewidth=1.5, label=f'USV{i + 1} to USV{i + 2}', alpha=0.9)
    plt.xlabel('Time (s)', fontsize=12)  # 规范标签表述
    plt.ylabel('X-gap between USVs (m)', fontsize=12)  # 补充USV复数形式
    plt.xticks(fontsize=10)  # 刻度字体大小
    plt.yticks(fontsize=10)
    ax.grid(True, color='lightgrey', linestyle='--', linewidth=0.5)  # 浅灰色虚线网格
    ax.spines['top'].set_visible(False)  # 隐藏顶部边框
    ax.spines['right'].set_visible(False)  # 隐藏右侧边框
    plt.legend(prop={'size': 10}, frameon=False, loc='upper right', bbox_to_anchor=(1, 1), handlelength=1.5)  # 图例线条长度匹配
    plt.tight_layout()  # 自动调整边距
    # plt.show()
    if switch == 1:
        plt.savefig(f'usv_xgap_fls_n={n}.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 2:
        plt.savefig(f'usv_xgap_smo.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 3:
        plt.savefig(f'usv_xgap_backstepping.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 4:
        plt.savefig(f'usv_xgap_pid.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图


def plot_ygap(y):
    plt.figure(4, figsize=(8, 6))
    ax = plt.gca()
    for i in range(0, n - 1):
        plt.plot(y[i, :], color=colors[i], linewidth=1.5, label=f'USV{i + 1} to USV{i + 2}', alpha=0.9)
    plt.xlabel('Times (s)', fontsize=12)
    plt.ylabel('Y-gap between USV (m)', fontsize=12)
    plt.xticks(fontsize=10)  # 刻度字体大小
    plt.yticks(fontsize=10)
    ax.grid(True, color='lightgrey', linestyle='--', linewidth=0.5)  # 浅灰色虚线网格
    ax.spines['top'].set_visible(False)  # 隐藏顶部边框
    ax.spines['right'].set_visible(False)  # 隐藏右侧边框
    plt.legend(prop={'size': 10}, frameon=False, loc='upper right', bbox_to_anchor=(1, 1), handlelength=1.5)  # 图例线条长度匹配
    plt.tight_layout()  # 自动调整边距
    # plt.show()
    if switch == 1:
        plt.savefig(f'usv_ygap_fls_n={n}.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 2:
        plt.savefig(f'usv_ygap_smo.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 3:
        plt.savefig(f'usv_ygap_backstepping.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 4:
        plt.savefig(f'usv_ygap_pid.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图


def plot_error(e1, e2):
    plt.figure(5, figsize=(8, 6))
    ax = plt.gca()
    plt.plot(e1[1], color=colors[1], label='Error of USV1')
    plt.plot(e2[1], color=colors[2], label=f'Error of USV{n}')
    plt.xlabel('Times (s)', fontsize=12)
    plt.ylabel('Tracking error (m)', fontsize=12)
    plt.xticks(fontsize=10)  # 刻度字体大小
    plt.yticks(fontsize=10)
    ax.grid(True, color='lightgrey', linestyle='--', linewidth=0.5)  # 浅灰色虚线网格
    ax.spines['top'].set_visible(False)  # 隐藏顶部边框
    ax.spines['right'].set_visible(False)  # 隐藏右侧边框
    plt.legend(prop={'size': 10}, frameon=False, loc='upper right', bbox_to_anchor=(1, 1), handlelength=1.5)  # 图例线条长度匹配
    plt.tight_layout()  # 自动调整边距
    # plt.show()
    if switch == 1:
        plt.savefig(f'usv_error_fls_n={n}.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 2:
        plt.savefig(f'usv_error_smo.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 3:
        plt.savefig(f'usv_error_backstepping.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    elif switch == 4:
        plt.savefig(f'usv_error_pid.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图


def plot_error_all():
    df = pd.read_csv(r'..\error.csv')
    ax = plt.gca()
    plt.figure(figsize=(8, 6))
    plt.plot(df['1'], color=colors[0], label='FLS')
    plt.plot(df['2'], color=colors[2], label='SMO')
    plt.plot(df['3'], color=colors[4], label='Backstepping')
    plt.xlabel('Times(s)', fontsize=12)
    plt.ylabel('Tracking error of different schemes of USV1 (m)', fontsize=12)
    ax.grid(True, color='lightgrey', linestyle='--', linewidth=0.5)  # 浅灰色虚线网格
    ax.spines['top'].set_visible(False)  # 隐藏顶部边框
    ax.spines['right'].set_visible(False)  # 隐藏右侧边框
    plt.legend(prop={'size': 10}, frameon=False, loc='upper right', bbox_to_anchor=(1, 1), handlelength=1.5)  # 图例线条长度匹配
    plt.tight_layout()  # 自动调整边距
    plt.savefig(f'tracking_error.pdf', dpi=300, bbox_inches='tight')  # 保存高分辨率矢量图
    #plt.show()
