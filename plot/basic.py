import matplotlib.pyplot as plt

def plot_line(data, *args, **kwargs):
    #def display_time(x, y):
        #"""""" 
        #if rate:
            #x = x/float(rate)
        #return  "%s,    %s" % (x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.format_coord = display_time
    ax.plot(data, *args, **kwargs)
    plt.show()

if __name__ == '__main__':
    import numpy as np
    data = np.linspace(0, 100, 100)
    plot_line(data, c = 'b')
