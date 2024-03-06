# 现代控制系统 HW3

*21307289 刘森元*

## E3.13

可列方程
$$
L\frac{\text di}{\text dt}+Ri+v_c=v_{in}
$$
其中
$$
v_c=\frac1C\int i\ \text dt
$$
令状态变量 $x_1=v_c,\ x_2=i$ 有
$$
\dot x_1=\frac1Cx_2\\
\dot x_2=-\frac RLx_2-\frac1Lx_1+\frac1Lv_{in}
$$
可写成矩阵形式
$$
\mathbf{\dot x}=
\begin{bmatrix}
0 & 1/C\\
-1/L & -R/L
\end{bmatrix}\mathbf x+
\begin{bmatrix}
0\\1/L
\end{bmatrix}
v_{in}
$$
令 $C=0.001F,\ R=4\Omega,\ L=0.1H$ 有
$$
\mathbf x=\begin{bmatrix}
0 & 1000\\
-10 & -40
\end{bmatrix}\mathbf x+\begin{bmatrix}0\\10\end{bmatrix}v_{in}
$$

## P3.7

令 $K=1$ 有
$$
KG(s)\cdot\frac1s=\frac{(s+1)^2}{s(s^2+1)}
$$
可得闭环传递函数为
$$
T(s)=\frac{s^2+2s+1}{3s^3+5s^2+5s+1}=\frac{s^{-1}+2s^{-2}+s^{-3}}{3+5s^{-1}+5s^{-2}+s^{-3}}
$$
有状态变量模型
$$
\mathbf{\dot x}=\begin{bmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
-1/3 & -5/3 & -5/3
\end{bmatrix}\mathbf x+\begin{bmatrix}0\\0\\1/3\end{bmatrix}r\\
y=\begin{bmatrix}1&2&1\end{bmatrix}\mathbf x
$$

## P3.8

状态空间方程为
$$
\begin{align}
\dot x_1&=x_2\\
\dot x_2&=\frac{ku}{x_3}-g\\
\dot x_3&=u
\end{align}
$$
