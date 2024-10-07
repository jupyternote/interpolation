# 插值法
    本项目实现了范德蒙德多项式插值、拉格朗日插值、牛顿插值、分段插值、分段三次Hermite插值五种插值方式，调用代码能够绘制插值函数图像、并计算平均误差(声明：请使用专用查看工具查看readme,否则.md文件特有的格式会干扰阅读)

## 结果展示
![alt text](image-1.png)

![alt text](image-2.png)

## 项目安装  
1.安装python环境 Python 3.12.3  
2.创建虚拟环境 conda create -n interpolation -v python=3.12.3  
3.进入虚拟环境并安装依赖 pip install matplotlib  
4.运行main函数并获得结果  

## 代码结构
<pre>
main.py --调用--> |-----> Vandermond.py  
                  |-----> Lagrange.py  
                  |-----> Newtown.py
                  |-----> Linear.py
                  |-----> Hermite.py
</pre>

## 安装
git clone https://github.com/jupyternote/interpolation.git

## 参数修改和调试
main函数中param_dict存储了相关参数，在此处进行修改  
1.left,right:插值区间的左右端点  
2.num_node:使用多少个点进行函数图像绘制（默认参数1000足够，不需要修改）  
3.num_use:使用多少个点求解插值函数  
4.calculate_loss:使用多少个点计算损失  
5.init_param:标准函数的参数

func:被插值的标准函数，如果需要可以进行修改。
