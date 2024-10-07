# 包含所有插值工具
from Vandermond import vandermonde_interpolation
from Largrange import lagrange_interpolation
from Newtown import newton_interpolation
from Linear import piecewise_linear_interpolation
from Hermite import hermite_interpolation

# 引入绘图工具和相关库
import numpy as np
import matplotlib.pyplot as plt

# 参数字典，便于调用参数
param_dict={
    'left':0,
    'right':3*np.pi,
    'num_node':200,
    'num_use':10,
    'title':'function',
    'init_param':{
        'c':3,
        'd':1,
        'e':3,
        'f':2,
    }
}

# 一个用于存储结果的字典
plt_dict=dict()

# 被拟合函数
def func(x):
    global param_dict
    y = param_dict['init_param']['c'] * np.sin(param_dict['init_param']['d'] * x) + param_dict['init_param']['e'] * np.cos(param_dict['init_param']['f'] * x)
    return y

def interpolation():
    # 生成自变量的值，用于插值
    x_use = np.linspace(param_dict['left'], param_dict['right'], param_dict['num_use'])
    # 生成自变量的值，用于绘图
    x_draw = np.linspace(param_dict['left'], param_dict['right'], param_dict['num_node'])

    global plt_dict
    plt_dict['func'] = func(x_use)

    # 把范德蒙德拟合结果放进去
    vandermonde_func=vandermonde_interpolation(x_use.tolist(),plt_dict['func'])
    plt_dict['vandermonde'] = [vandermonde_func(xi) for xi in x_draw.tolist()]

    # 把拉格朗日结果放进去
    lagrange_func = lagrange_interpolation(x_use.tolist(), plt_dict['func'])
    plt_dict['lagrange'] = [lagrange_func(xi) for xi in x_draw.tolist()]

    # 把牛顿插值结果放进去
    newton_func = newton_interpolation(x_use.tolist(), plt_dict['func'])
    plt_dict['newton'] = [newton_func(xi) for xi in x_draw.tolist()]

    # 把线性插值结果放进去
    plt_dict['linear'] = piecewise_linear_interpolation(x_use.tolist(), plt_dict['func'], x_draw.tolist())

    #把分段三次埃米尔特插值放进去
    plt_dict['hermite']=hermite_interpolation(x_use.tolist(),plt_dict['func'],x_draw.tolist())

def draw():
    # 创建图形
    plt.figure(figsize=(10, 6))
    # 生成x的值，从a到b，共1000个点
    x_draw = np.linspace(param_dict['left'], param_dict['right'], param_dict['num_node'])
    plt.plot(x_draw, [func(xi) for xi in x_draw], label='Original Function')
    plt.plot(x_draw, plt_dict['vandermonde'], label='vandermonde Interpolation')
    plt.plot(x_draw, plt_dict['lagrange'], label='Lagrange Interpolation')
    plt.plot(x_draw, plt_dict['newton'], label='Newton Interpolation')
    plt.plot(x_draw, plt_dict['linear'], label='Piecewise Linear Interpolation')
    plt.plot(x_draw, plt_dict['hermite'], label='Hermite Interpolation')
    plt.legend()
    plt.title(param_dict['title'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# 确保先进行插值计算再绘图
interpolation()
draw()