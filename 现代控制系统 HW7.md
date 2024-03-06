# 现代控制系统 HW7

*21307289 刘森元*

## E11.11

系统有如下描述
$$
\mathbf{\dot x}=\mathbf{Ax+B}u\\
y=\mathbf{Cx+D}u
$$
其中有
$$
\mathbf A=\begin{bmatrix}0&1&0\\0&0&1\\-2&0&-7\end{bmatrix},\ 
\mathbf B=\begin{bmatrix}0\\0\\1\end{bmatrix},\ 
\mathbf C=\begin{bmatrix}1&2&0\end{bmatrix},\ 
\mathbf D=[1]
$$
能控矩阵为
$$
\mathbf P_c=\begin{bmatrix}\mathbf B&\mathbf{AB}&\mathbf{A^2B} \end{bmatrix}=
\begin{bmatrix}0&0&1\\0&1&-7\\1&-7&49\end{bmatrix}
$$
其行列式 $\text{det}\ \mathbf P_c=-1\neq0$，系统可控

能观矩阵为
$$
\mathbf P_o=\begin{bmatrix}\mathbf C\\\mathbf{CA}\\\mathbf{CA^2}\end{bmatrix}=
\begin{bmatrix}
1&2&0\\
0&1&2\\
-4&0&-13
\end{bmatrix}
$$
其行列式 $\text{det}\ \mathbf P_o=29\neq0$，系统可观

## P11.11

令 	
$$
u=-k_1x_1-k_2x_2+\alpha r
$$
其中 $r(t)$ 为输入指令，一个状态变量表达为
$$
\begin{align}
\mathbf{\dot x}&=\begin{bmatrix}-5&-2\\2&0 \end{bmatrix}\mathbf x+\begin{bmatrix}0.5\\0 \end{bmatrix}u\\
y&=\begin{bmatrix}0&1\end{bmatrix}\mathbf x+[0]u
\end{align}
$$
闭环传递函数为
$$
T(s)=\frac\alpha{s^2+(k_1/2+5)s+4+k_2}
$$
要令性能满足条件，要有 $\omega_n=4.8,\ \zeta=0.826$，故有特征多项式
$$
q(s)=s^2+2(0.826)4.8s+23=s^2+8s+23
$$
可得 $k_1=6,\ k_2=19$

令 $\alpha=23$ 使得稳态误差对于阶跃响应为 $0$

## P11.13

若要使得 $K_v=35$，令 $K=2450$，一个状态变量表达为
$$
\mathbf{\dot x}=\begin{bmatrix}0&1\\0&-70\end{bmatrix}\mathbf x+\begin{bmatrix}0\\2450\end{bmatrix}u\\
y=\begin{bmatrix}1&0\end{bmatrix}\mathbf x
$$
令
$$
u=-k_1x_1-k_2x_2
$$
则有闭环特征方程为
$$
q(s)=s^2+(2450k_2+70)s+2450k_1=0
$$
理想的特征方程为
$$
s^2+72.73s+2644.63=0
$$
故令 $\zeta=0.707,\ \omega_n=51.42$，可解得 $k_1=1.08,\ k_2=0.0011$

## P11.27

能观矩阵为
$$
\mathbf P_o=\begin{bmatrix}\mathbf C\\\mathbf{CA}\end{bmatrix}=\begin{bmatrix}1&0\\1&0\end{bmatrix}
$$
其行列式 $\text{det}\ \mathbf P_o=0$，故该系统不完全可观，无法找到一个观察增益矩阵