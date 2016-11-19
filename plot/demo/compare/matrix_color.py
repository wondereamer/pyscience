import matplotlib.pyplot as plt
import numpy as np
#                   r   c    b     te    ao
matrix = np.array([[0.1, 0.5, 1, 0.55, 0.38],
                   [1,   0.1, 0.6,  0.3, 0.5],
                   [1, 1,   0,    0.7, 0.45],
                   [1, 1, 1,      0.13,   0.56],
                   [1, 1, 1,      1,   0.23]])
txt = None
pfig = plt.figure(1)
plt.imshow(matrix, interpolation = 'nearest',cmap = plt.cm.Greys_r, vmin = 0, vmax = 1)
##imshow(A, interpolation = 'nearest',cmap =  cm.Greys_r)
##imshow(A, interpolation = 'nearest')
##grid(True)
plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.show()
#*************************************************************************
#def my_imshow(my_img,ax=None,**kwargs):
    #if ax is None:
        #ax = gca()
    #def format_coord(x, y):
        #x = int(x + 0.5)
        #y = int(y + 0.5)
        #try:
            #return "%s @ [%4i, %4i]" % (my_img[y, x], x, y)
        #except IndexError:
            #return ""
    #ax.imshow(my_img,**kwargs)
    #ax.format_coord = format_coord
    #show()

#my_imshow(A, interpolation = 'nearest' )

#*************************************************************************
#from matplotlib import pyplot as plt
#import numpy as np

#im = plt.imshow(np.random.rand(10,10)*255, interpolation='nearest')
#fig = plt.gcf()
#ax = plt.gca()

#class EventHandler:
    #def __init__(self):
        #fig.canvas.mpl_connect('button_press_event', self.onpress)

    #def onpress(self, event):
        #if event.inaxes!=ax:
            #return
        #xi, yi = (int(round(n)) for n in (event.xdata, event.ydata))
        #value = im.get_array()[xi,yi]
        #color = im.cmap(im.norm(value))
        #print xi,yi,value,color

#handler = EventHandler()

#plt.show()

#*************************************************************************

#def onclick(event):
    #global txt
    #txt = plt.text(event.xdata, event.ydata, 'TESTTEST', fontsize=8)
    #fig.canvas.draw()

#def offclick(event):
    ##txt.remove()
    ##fig.canvas.draw()
    #pass

#fig.canvas.mpl_connect('button_press_event', onclick)
#fig.canvas.mpl_connect('button_release_event', offclick) 

#plt.show()
