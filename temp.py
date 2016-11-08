import numpy as np
import matplotlib
matplotlib.use("TKAgg")

g_lines = []

def plot_3d(lines):
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    fig, ax1 = plt.subplots(1, 1, subplot_kw={'projection': '3d'})


    for i, line in enumerate(lines):
        pline = ax1.plot(range(len(line)), line, i, picker = 1)
        g_lines.append(pline)
        print type(pline)
        print pline

    def on_pick(event):
        '''docstring for on_motion''' 
        for i,line in enumerate(g_lines):
            if line != event.artist:
                line.set_visible(False)
            else:
                global sline_index
                sline_index = i

    def on_button_release(event):
        for line in g_lines:
            print type(line)
            line.set_visible(True)
        fig.canvas.draw_idle()


    fig.canvas.mpl_connect('pick_event', on_pick)
    fig.canvas.mpl_connect('button_release_event', on_button_release)

    #X, Y, Z = axes3d.get_test_data(0.05)
    #d = ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)

    #for i in range(len(X)):
        #ax1.scatter([X[i]]*len(Y[i]), Z[i], z[i], color=['red']*len(y[i]), picker=1)

    #ax1.set_ylim3d(min(y), max(y))
    #ax1.set_zlim3d(min(z), max(z))

    ax1.set_xlabel('X')
    #ax.set_xlim(-40, 40)
    ax1.set_ylabel('Y')
    #ax.set_ylim(-40, 40)
    ax1.set_zlabel('Z')

    ax1.set_title("Column stride 0")
    plt.show()
    return


plot_3d([[1,2,3,4,5,6], [2,2,2,3,3,4]])
