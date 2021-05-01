import numpy as np
import math
from PIL import  Image
import matplotlib
import matplotlib.pyplot as plt
from Script.HeatMap import HeatMap

path = ''
x=-1
y=-1
def updateVar(ipath,ix,iy):
    global path,x,y
    path = ipath
    x=ix
    y=iy

def main():
    #heat_map values for the demo image(8X4)
    max = 0
    #x= float(input('Enter X cordinate (8x8):'))
    #y= float(input('Enter Y cordinate (8x8):'))
    b=([1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1])
    for i in range(8):
        for j in range(8):
            b[i][j] = math.sqrt(((i-x)**2)+((j-y)**2))
            if(b[i][j]>max):
                max=b[i][j]

    for i in range(8):
        for j in range(8):
            b[i][j]= max - b[i][j] +1
            b[i][j]= 100*(b[i][j])



    heat_map = np.array([[b[0][0], b[0][1], b[0][2], b[0][3], b[0][4],b[0][5],b[0][6],b[0][7]],
                         
                         [b[1][0], b[1][1], b[1][2], b[1][3],b[1][4],b[1][5],b[1][6],b[1][7]],
                       
                         [b[2][0], b[2][1], b[2][2] , b[2][3],b[2][4],b[2][5],b[2][6],b[2][7]],
                        
                         [b[3][0], b[3][1], b[3][2], b[3][3],b[3][4],b[3][5],b[3][6],b[3][7]],
                         [b[4][0], b[4][1], b[4][2], b[4][3],b[4][4],b[4][5],b[4][6],b[4][7]],
                         [b[5][0], b[5][1], b[5][2], b[5][3],b[5][4],b[5][5],b[5][6],b[5][7]],
                         [b[6][0], b[6][1], b[6][2], b[6][3],b[6][4],b[6][5],b[6][6],b[6][7]],
                         [b[7][0], b[7][1], b[7][2], b[7][3],b[7][4],b[7][5],b[7][6],b[7][7]]])
                         


    hm = HeatMap(path,heat_map)
    image = Image.open(path)
    image = np.asarray(image)
    hm = HeatMap(image,heat_map)
    hm.plot()

    # simple save
    hm.save('heatmap1')

    # customised save
    hm.save('heatmap2','png',
            transparency=0.6,
            color_map='seismic',
            show_axis=True,
            show_original=True,
            show_colorbar=True,
            width_pad=-10)
