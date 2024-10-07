def divided_diff(x, y):
    """
    计算差商表
    """
    n = len(x)
    coef = y.copy()  # 差商表的第一列
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def newton_poly(x_points, coefficients, x):
    """
    计算牛顿插值多项式在 x 处的值
    """
    n = len(x_points)
    result = coefficients[0]  # 从第一个系数开始
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_points[j])
        result += term
    return result

def newton_interpolation(x, y):
    """
    使用牛顿插值法构造插值多项式，并返回该插值多项式作为函数
    """
    if len(x) != len(y):
        raise ValueError("x and y must be the same length")
    if not all(x[i] <= x[i+1] for i in range(len(x)-1)):
        raise ValueError("x values must be sorted in ascending order")

    coef = divided_diff(x, y)
    
    def interpolation_function(n):
        """
        插值函数
        """
        return newton_poly(x, coef, n)
    
    return interpolation_function

def main():
    # 示例数据点
    x_points = [0, 1, 2, 3]
    y_points = [1, 3, 1, -1]

    # 获取插值函数
    interpolation_function = newton_interpolation(x_points, y_points)

    # 使用插值函数计算新的 x 值
    x_new = [0, 0.5, 1.5, 2.5, 3]  # 示例 x 值数组
    y_new = [interpolation_function(xi) for xi in x_new]

    # 打印插值结果
    for xi, yi in zip(x_new, y_new):
        print(f"Interpolated value at x={xi} is y={yi}")

if __name__ == '__main__':
    main()
