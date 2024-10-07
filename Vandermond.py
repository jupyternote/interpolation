import numpy as np

def vandermonde_interpolation(x_data, y_data):
    """
    使用范德蒙德插值法构造插值多项式

    参数:
    x_data -- 插值基点的 x 坐标数组
    y_data -- 插值基点的 y 坐标数组

    返回:
    返回一个函数，该函数接受一个 x 值并返回对应的插值结果
    """
    # 创建范德蒙德矩阵
    V = np.vander(x_data, len(x_data), increasing=True)

    # 解线性方程求系数
    coefficients = np.linalg.solve(V, y_data)

    def interpolation_function(x_val):
        """
        插值函数
        """
        # 计算多项式在 x_val 处的值
        return np.polyval(coefficients[::-1], x_val)

    return interpolation_function


def main():
    # 示例使用
    x_data = np.array([0, 1, 2, 3])
    y_data = np.array([1, 3, 0, -1])

    # 获取插值函数
    interpolation_function = vandermonde_interpolation(x_data, y_data)

    # 计算特定点的插值
    x_val = 2.5
    y_val = interpolation_function(x_val)
    print(f"The interpolated value at x = {x_val} is y = {y_val}")

    # 绘制插值结果
    import matplotlib.pyplot as plt

    x_points = np.linspace(min(x_data), max(x_data), 100)
    y_points = [interpolation_function(x) for x in x_points]

    plt.plot(x_points, y_points, label='Vandermonde Interpolation')
    plt.scatter(x_data, y_data, color='red', label='Data Points')
    plt.legend()
    plt.title('Vandermonde Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

if __name__=="__main__":
    main()
    