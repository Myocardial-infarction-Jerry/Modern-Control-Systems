import numpy as np
import matplotlib.pyplot as plt
import os

# 定义时间范围
t = np.linspace(0, 10, 1000)

# 定义常数值
A = 0.9655
B = -1.0275
C_real = 0.0310
C_imag = -0.0390
D_real = 0.0310
D_imag = 0.0390

# 计算y(t)
y = A + B * np.exp(-5 * t) + C_real * np.exp(-20 * t) * np.cos(
    50 * t) - C_imag * np.exp(-20 * t) * np.sin(50 * t) + D_real * np.exp(
        -20 * t) * np.cos(50 * t) + D_imag * np.exp(-20 * t) * np.sin(50 * t)

# 绘制y(t)图像
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('y(t) Graph')
plt.grid(True)
plt.savefig(os.path.dirname(__file__) + '/P2-50_Figure-d.png', dpi=300)
plt.show()
