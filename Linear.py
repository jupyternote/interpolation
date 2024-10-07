import numpy as np
import matplotlib.pyplot as plt

def piecewise_linear_interpolation(x, y, x_new):
    """
    分段线性插值

    参数:
    x -- 已知数据点的 x 坐标数组
    y -- 已知数据点的 y 坐标数组
    x_new -- 需要插值的新的 x 坐标点数组

    返回:
    y_new -- 对应于 x_new 的插值结果数组
    """
    y_new = []
    for x_val in x_new:
        for i in range(len(x) - 1):
            if x[i] <= x_val <= x[i + 1]:
                # 计算插值
                y_new.append(y[i] + (y[i + 1] - y[i]) * (x_val - x[i]) / (x[i + 1] - x[i]))
                break
        else:
            # 如果x_val在x的最大值之外，则取最后一个y值
            if x_val > x[-1]:
                y_new.append(y[-1])
            # 如果x_val在x的最小值之外，则取第一个y值
            elif x_val < x[0]:
                y_new.append(y[0])
    
    return y_new

# test
def main():
    x_points = np.array([0, 1, 2, 3, 4, 5])
    y_points = np.array([0, 0.5, 0.5, 2, 2, 0])

    # 需要插值的新的 x 坐标点
    x_new = np.linspace(0, 5, 100)

    # 计算插值结果
    y_new = piecewise_linear_interpolation(x_points, y_points, x_new)

    # 绘制结果
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_points, 'o', label='Data Points')
    plt.plot(x_new, y_new, '-', label='Piecewise Linear Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__=="__main__":
    main()