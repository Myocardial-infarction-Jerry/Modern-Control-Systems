# 现代控制系统 HW6

*21307289 刘森元*

## E5.10

$$
T(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}\\\\
(a)\ P.O.\leq5\%\Rightarrow s\geq0.69\\\\
(b)\ T_s<4\Rightarrow \omega_n\zeta>1\\\\
(c)\ T_p<1\Rightarrow\omega_n\sqrt{1-\zeta^2}>\pi
$$

## P5.22

闭环传递函数为
$$
T(s)=\frac{2(2s+\tau)}{(s+0.2K)(2s+\tau)+4}
$$

- 若 $R(s)=1/s$，有阶跃响应
  $$
  Y(s)=\frac{2(2s+\tau)}{(s+0.2K)(2s+\tau)+4}\frac1s
  $$
  由终值定理有
  $$
  y_{ss}=\lim_{s\rightarrow0}sY(s)=\frac{2\tau}{0.2K\tau+4}
  $$
  令 $K=10-20/\tau$，有 $y_{ss}=1$

- 特征方程为
  $$
  (s+0.2K)(2s+\tau)+4=2s^2+(0.4K+\tau)s+0.2K\tau+4=0
  $$
  令 $K=10-20/\tau$，有
  $$
  \omega_n=\sqrt\tau\quad\text{and}\quad\zeta=\frac{\tau^2+4\tau-8}{4\tau^{3/2}}
  $$
  故有
  $$
  T_p=\frac\pi{\omega_n\sqrt{1-\zeta^2}}\quad\text{and}\quad P.O.=100e^{-\zeta\pi\sqrt{1-\zeta^2}}\\
  \tau>2\sqrt3-2\approx1.4642
  $$
  

