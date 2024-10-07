import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y):
    """
    使用拉格朗日插值法构造插值多项式

    参数:
    x -- 插值基点的 x 坐标数组
    y -- 插值基点的 y 坐标数组

    返回:
    返回一个函数，该函数接受一个 x 值并返回对应的插值结果
    """
    def L(i, x_val):
        """
        计算第 i 个拉格朗日基多项式在 x_val 处的值
        """
        # 初始化乘积为1
        term = 1
        for j, x_j in enumerate(x):
            if j != i:
                # 计算乘积中的每一个因子
                term *= (x_val - x_j) / (x[i] - x_j)
        return term

    def interpolation_function(x_val):
        """
        插值函数
        """
        total = 0
        for i in range(len(x)):
            total += y[i] * L(i, x_val)
        return total

    return interpolation_function

# test
def main():
    x_points = np.array([0, 1, 2, 3])
    y_points = np.array([1, 3, 1, -1])

    # 获取插值函数
    interpolation_function = lagrange_interpolation(x_points, y_points)

    # 使用插值函数计算新的 x 值
    x_new = np.linspace(0, 3, 100)
    y_new = [interpolation_function(xi) for xi in x_new]

    # 绘制结果
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_points, 'o', label='Data Points')
    plt.plot(x_new, y_new, '-', label='Lagrange Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    main()