import numpy as np
import peakutils
import matplotlib.pyplot as plt
from scipy import signal
from peakdetect import peakdetect
xs = np.arange(0, 4*np.pi, 0.05)
data = np.sin(xs)
peakind = signal.find_peaks_cwt(data, np.arange(1,10))
print(peakind, xs[peakind], data[peakind])
peaks = peakdetect(data, lookahead=100)
# print(peaks)
indexes = peakutils.indexes(data, thres=0.02/max(data), min_dist=100)
print(indexes)
plt.plot(xs, data)
print(data[indexes])
plt.show()