import numpy as np
import matplotlib.pyplot as plt

def hermite_interpolation(x, y, x_new):
    """
    分段Hermite插值

    参数:
    x -- 已知数据点的 x 坐标数组
    y -- 已知数据点的 y 坐标数组
    x_new -- 需要插值的新的 x 坐标点数组

    返回:
    y_new -- 对应于 x_new 的插值结果数组
    """
    x = np.array(x)  # 确保 x 是 NumPy 数组
    y = np.array(y)  # 确保 y 是 NumPy 数组
    
    def hermite_polynomial(x_val, x_i, x_ip1, y_i, y_ip1, dy_i, dy_ip1):
        """
        计算Hermite多项式在x_val处的值
        """
        # 计算间隔长度
        h = x_ip1 - x_i
        
        # 计算Hermite基多项式
        h00 = (1 + 2 * (x_val - x_i) / h) * ((x_ip1 - x_val) / h) ** 2
        h10 = (x_val - x_i) * ((x_ip1 - x_val) / h) ** 2
        h01 = (1 + 2 * (x_ip1 - x_val) / h) * ((x_val - x_i) / h) ** 2
        h11 = (x_val - x_ip1) * ((x_val - x_i) / h) ** 2
        
        # 构造并返回Hermite多项式
        return (h00 * y_i + h01 * y_ip1 + h10 * dy_i * h + h11 * dy_ip1 * h)

    n = len(x)
    if n != len(y):
        raise ValueError("x and y must be the same length")

    # 计算一阶导数dy/dx
    dy = np.zeros(n)
    dy[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2]) / 2  # 中间点的一阶导数
    dy[0] = (y[1] - y[0]) / (x[1] - x[0])  # 第一个点的导数
    dy[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])  # 最后一个点的导数

    y_new = []
    for x_val in x_new:
        for i in range(n - 1):
            if x[i] <= x_val <= x[i + 1]:
                y_new.append(hermite_polynomial(x_val, x[i], x[i + 1], y[i], y[i + 1], dy[i], dy[i + 1]))
                break
        else:
            if x_val < x[0]:
                y_new.append(y[0])
            elif x_val > x[-1]:
                y_new.append(y[-1])

    return y_new

def main():
    x_points = np.array([0, 1, 2, 3, 4, 5])
    y_points = np.array([0, 0.5, 0.5, 2, 2, 0])

    # 需要插值的新的 x 坐标点
    x_new = np.linspace(0, 5, 100)

    # 计算插值结果
    y_new = hermite_interpolation(x_points, y_points, x_new)

    # 绘制结果
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_points, 'o', label='Data Points')
    plt.plot(x_new, y_new, '-', label='Hermite Interpolation')
    plt.legend()
    plt.grid(True)
    plt.title("Hermite Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

if __name__ == '__main__':
    main()
