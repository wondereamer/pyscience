# encoding:UTF-8
from util import read_signal
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import util
import numpy as np

def plot_wavefile(fname, target_rate=None):
    """ 绘制wav文件
    
    Args:
        fname (str): 文件名
        target_rate (int.): 信号的绘图采样率, 可选
    """
    rate,  signal = read_signal(fname)
    if not target_rate:
        target_rate = rate 
    signal = util.set_frame_rate(signal, rate, target_rate)
    #signal = util.slice(signal, 1000, 60*10, 60*15)
    plot_signal(signal, target_rate)

def plot_signal(signal, rate=None):
    def display_time(x, y):
        """""" 
        if rate:
            x = x/float(rate)
        return  "%s,    %s" % (x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.format_coord = display_time
    ax.plot(signal, 'k')
    plt.show()

def plot_intervals(axes, signal, intervals):
    """ 画出区间的高亮背景""" 
    upper, lower = int(max(signal)),  int(min(signal))
    color = ['green', 'red']
    for i, interval in enumerate(intervals):
        beginx, endx = interval[0], interval[1]
        p = patches.Rectangle((beginx, lower), endx-beginx, 
                            upper-lower, alpha=0.5,
                            fc =color[i%2], linewidth=0)
        axes.add_patch(p)

def plot_chunk_features(signal, multi_features, colors, labels, chunk_size, twinx=True):
    """ 绘制信号，及块状特征值。 """
    if multi_features:
        x = [i*chunk_size for i in range(len(multi_features[0]))]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(signal, c='gray', label='signal', alpha=0.5)
    for i, features in enumerate(multi_features):
        if twinx:
            ax = ax1.twinx()
        else:
            ax = ax1
        if labels:
            ax.plot(x, features, '-',  c=colors[i], label=labels[i])
        else:
            ax.plot(x, features, '-', c=colors[i])
    if labels:
        plt.legend()
    return ax1


def plot_feature_comparing(features, intervals):
    """ 绘制两类特征片段的值。 
    一个数据源，当中夹杂着两类数据，区间不一样。 
    """
    speech_features = util.intervals_data(features, intervals)
    noise_intervals = util.intervals_completion(len(features), intervals)
    noise_features = util.intervals_data(features, noise_intervals)

    #n, bins =  np.histogram(speech_features, 40)
    plt.hist(speech_features, bins=40, histtype='stepfilled', normed=True,
            cumulative=False, color='b', label='speech', alpha = 0.5)

    plt.hist(noise_features, bins=40, normed=True,
            cumulative=False, color='r', label='noise', alpha=0.5)

    print np.std(noise_features, ddof=1) # same as matlab
    print np.std(noise_features)
    print np.std(speech_features)

    plt.legend()
    plt.show()


def plot_3d():
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt

    fig, ax1 = plt.subplots(1, 1, subplot_kw={'projection': '3d'})
    X, Y, Z = axes3d.get_test_data(0.05)
    ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
    ax1.set_title("Column stride 0")
    plt.show()


    plt.tight_layout()
    plt.show()
    return


def plot_color_matrix(ax, A, colorbar=False):
    #A = np.random.rand(5, 5)
    ax.imshow(A.transpose(), interpolation='none', cmap='gray')
    ax.imshow(A.transpose(), interpolation='none')
    if colorbar:
        plt.colorbar()
    plt.grid(True)


def plot_signal_matrix(signal, matrix):
    """ 绘制两类特征片段的值。 
    一个数据源，当中夹杂着两类数据，区间不一样。 
    """
    fig, (ax0, ax1) = plt.subplots(nrows=2)
    #fig = plt.figure()
    #ax0 = fig.add_subplot(111)
    ax0.plot(signal)
    ax0.set_xlim((0, len(signal)))
    plot_color_matrix(ax1, matrix, False)


def plot_freq(signal):
    ff = 5;   # frequency of the signal

    Fs = 150.0;  # sampling rate
    Ts = 1.0/Fs; # sampling interval
    t = np.arange(0,1,Ts) # time vector
    signal = np.sin(2*np.pi*ff*t)
    signal[0:len(signal)/2] += np.sin(2*np.pi*ff*2*t)[0:len(signal)/2]

    ps = np.abs(np.fft.fft(signal))**2
    time_step = 1 / 30.0
    freqs = np.fft.fftfreq(signal.size, time_step)
    idx = np.argsort(freqs)
    plt.plot(freqs[idx], ps[idx])


def plot_overlay_signal_matrix():
    """ 在一个矩形区域上添加曲线。 """
    fig, axs = plt.subplots(1,1,figsize=(15,10))
    axs.imshow(np.random.rand(50,100) ,cmap='gray', interpolation='none', alpha=0.3)
    nplots = 50
    fig.canvas.draw()
    box = axs._position.bounds
    height = box[3] / nplots

    for i in range(nplots):
	tmpax = fig.add_axes([box[0], box[1] + i * height, box[2], height])
	tmpax.set_axis_off()
	tmpax.plot(np.sin(np.linspace(0,np.random.randint(20,1000),1000))*0.4)
	tmpax.set_ylim(-1,1)


if __name__ == '__main__':
    plot_overlay_signal_matrix()
    plt.show()
