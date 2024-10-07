import numpy as np
import matplotlib.pyplot as plt

# 包含所有插值工具
from Vandermond import vandermonde_interpolation
from Largrange import lagrange_interpolation
from Newtown import newton_interpolation
from Linear import piecewise_linear_interpolation
from Hermite import hermite_interpolation

# 参数字典，便于调用参数
param_dict = {
    'left': 0,
    'right': np.pi,
    'num_node': 1000,
    'num_use': 10,
    'calculate_loss': 100,  # 增加计算误差的点数
    'title': 'Function Interpolation',
    'init_param': {
        'c': 3,
        'd': 1,
        'e': 3,
        'f': 2,
    }
}

# 一个用于存储结果的字典
plt_dict = {}

# 被拟合函数
def func(x):
    global param_dict
    y = param_dict['init_param']['c'] * np.sin(param_dict['init_param']['d'] * x) + param_dict['init_param']['e'] * np.cos(param_dict['init_param']['f'] * x)
    return y

# 在全局作用域中定义插值函数变量
vandermonde_func = None
lagrange_func = None
newton_func = None
piecewise_linear_func = None
hermite_func = None

def interpolation(x_use):
    global plt_dict, vandermonde_func, lagrange_func, newton_func, piecewise_linear_func, hermite_func
    
    # 生成自变量的值，用于绘图
    x_draw = np.linspace(param_dict['left'], param_dict['right'], param_dict['num_node'])

    plt_dict['func'] = func(x_use)

    # 把范德蒙德拟合结果放进去
    vandermonde_func = vandermonde_interpolation(x_use, plt_dict['func'])
    plt_dict['vandermonde'] = [vandermonde_func(xi) for xi in x_draw]

    # 把拉格朗日结果放进去
    lagrange_func = lagrange_interpolation(x_use, plt_dict['func'])
    plt_dict['lagrange'] = [lagrange_func(xi) for xi in x_draw]

    # 把牛顿插值结果放进去
    newton_func = newton_interpolation(x_use, plt_dict['func'])
    plt_dict['newton'] = [newton_func(xi) for xi in x_draw]

    # 把线性插值结果放进去
    plt_dict['linear'] = piecewise_linear_interpolation(x_use, plt_dict['func'], x_draw)

    # 把分段三次埃米尔特插值放进去
    plt_dict['hermite'] = hermite_interpolation(x_use, plt_dict['func'], x_draw)

def draw():
    global plt_dict, vandermonde_func, lagrange_func, newton_func, piecewise_linear_func, hermite_func
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    # 生成x的值，从a到b，共1000个点
    x_draw = np.linspace(param_dict['left'], param_dict['right'], param_dict['num_node'])
    plt.plot(x_draw, [func(xi) for xi in x_draw], label='Original Function')
    plt.plot(x_draw, plt_dict['vandermonde'], label='Vandermonde Interpolation')
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

# 计算误差
def calculate_errors(x_points, y_true, interpolations):
    errors = {}
    for method, y_pred in interpolations.items():
        # 计算每个插值方法的误差
        mse = np.mean((y_true - y_pred) ** 2)
        errors[method] = mse
        print(f"{method} MSE: {mse:.4f}")
    return errors

def calculate_variances(x_points, y_true, interpolations):
    errors = {}
    for method, y_pred in interpolations.items():
        # 计算每个插值方法的方差
        variance = np.var(y_true - y_pred)
        errors[method] = variance
        print(f"{method} Variance: {variance:.4f}")
    return errors

def calculate_interpolation_errors(x_use):
    global vandermonde_func, lagrange_func, newton_func, piecewise_linear_func, hermite_func
    
    x_loss = np.linspace(param_dict['left'], param_dict['right'], param_dict['calculate_loss'])
    y_true_loss = func(x_loss)
    y_vandermonde_loss = [vandermonde_func(xi) for xi in x_loss]
    y_lagrange_loss = [lagrange_func(xi) for xi in x_loss]
    y_newton_loss = [newton_func(xi) for xi in x_loss]
    y_linear_loss = piecewise_linear_interpolation(x_use, plt_dict['func'], x_loss)
    y_hermite_loss = hermite_interpolation(x_use, plt_dict['func'], x_loss)

    interpolations = {
        'vandermonde': y_vandermonde_loss,
        'lagrange': y_lagrange_loss,
        'newton': y_newton_loss,
        'linear': y_linear_loss,
        'hermite': y_hermite_loss
    }

    errors = calculate_errors(x_loss, y_true_loss, interpolations)
    variances = calculate_variances(x_loss, y_true_loss, interpolations)
    return errors, variances

# 确保先进行插值计算再绘图
x_use = np.linspace(param_dict['left'], param_dict['right'], param_dict['num_use'])
interpolation(x_use)
draw()
errors, variances = calculate_interpolation_errors(x_use)