import matplotlib.pyplot as plt
import numpy as np

x,y = np.random.randn(2,100)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=False, lw=2)
ax1.grid(True)
ax1.axhline(0, color='black', lw=2)


plt.show()

