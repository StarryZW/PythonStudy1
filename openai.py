x = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
y = [3, 5, 4, 7, 11, 8, 12, 16, 20, 18]
import matplotlib.pyplot as plt

plt.plot(x, y, 'bo-')
plt.show()
import scipy.signal as sig

y_smooth = sig.savgol_filter(y, window_length=5, polyorder=2)

plt.plot(x, y, 'bo-', label='original data')
plt.plot(x, y_smooth, 'r-', label='smoothed data')
plt.legend()
plt.show()
