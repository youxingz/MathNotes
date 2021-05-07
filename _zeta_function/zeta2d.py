# See more information at:
# http://pyevolve.sourceforge.net/wordpress/?p=1079
# By Christian S. Perone <christian.perone@gmail.com>

# I used mencoder to create a video from all png's created
# mencoder mf://@list.txt -mf w=800:h=600:fps=%1:type=png -ovc copy -oac copy -o output.avi
# The list.txt are a list with filenames separated by line break
# The output.avi is the video output.

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpmath import zeta, zetazero

def calc_zeta(re, img_name):
    X,Y,Z = [], [], []

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in np.arange(0.1, 50.0, 0.1):
        compl = zeta(complex(re, i))
        X.append(compl.real)
        Y.append(compl.imag)
        Z.append(i)

    ax.grid(True)
    ax.plot(Z,X, label='Im(v)', lw=0.8)
    ax.plot(Z,Y, label='Re(v)', lw=0.8)
    ax.set_title("Riemann Zeta function - re(s)=%.3f" % re)
    ax.set_xlabel("Im(s)")
    ax.set_ylabel("Re(v) and Im(v)")

    leg = ax.legend(shadow=True)   
    for t in leg.get_texts():
        t.set_fontsize('small')

    for l in leg.get_lines():
        l.set_linewidth(2.0)

    # Plot the zeroes of zeta
    for i in range(1, 11):
        zero = zetazero(i)
        ax.plot(zero.imag, [0.0], "ro")

    # Comment this line for autoscale
    ax.set_ylim(12, -12)
    plt.savefig(img_name)
    print("Plot %s !" % img_name)
    plt.close()

if __name__ == "__main__":
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    file_index = 0
    for i in np.arange(0.01, 10.0, 0.01):
        file_index += 1
        calc_zeta(i, "./_zeta_function/zeta2d_result/zeta_plot_Re(s)=%s.png" % i)
