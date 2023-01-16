# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:53:06 2023

@author: jasweeney
"""
#z=x+i*y, c=a+i*b
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageDraw

def mandel_it(x,y,a,b):
    return(x**2-y**2+a,2*x*y+b)

def mandel(a,b,n):
    run_0=[a,b]
    for j in range(1,n+1):
        if run_0[0]>350 or run_0[1]>350:
            return(0)
        run_1=mandel_it(run_0[0],run_0[1],a,b)
        run_0=run_1
    return run_1

width=5000
height=5000

start=-2
end=1.5

im = Image.new('RGB', (width,height),(0,0,0))
draw = ImageDraw.Draw(im)

for x_v in range(0,width):
    for y_v in range(0,height):
        x_val=start+(x_v/width)*(end-start)
        y_val=start+(y_v/height)*(end-start)
        for n in range(1,76):
            if mandel(x_val,y_val,n)==0:
                break
            else:
                color=int(0.9*(255-(n*255/75)))
        if color==0:
            draw.point([x_v,y_v], (0,0,0))
        else:
            draw.point([x_v,y_v], (255-color,0,color))

im.save('output.png','PNG')

#fig = plt.figure()
#ax = fig.add_subplot()
#plt.scatter(to_plot_x,to_plot_y, s=0.001)
#ax.set_aspect('equal')
#plt.savefig('Mandelbrot.png', dpi=1200)
#plt.show()