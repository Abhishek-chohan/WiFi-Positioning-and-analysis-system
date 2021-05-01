import cv2
import pandas as pd
import numpy as np
import os
from sklearn.cluster import KMeans

path = ''
n = 0
global img
def updateVar(fpath,fn):
    global path,n
    path = fpath
    n = fn

coordinates = []
# function to display the coordinates of
# of the points clicked on the image

def click_event(event, x, y, flags, params):
    global img
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        #print(x, ' ', y)
        coordinates.append([x, y])

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img, str(x) + ',' +
        #             str(y), (x, y), font,
        #             1, (255, 0, 0), 1)
        cv2.circle(img, (x, y), radius=1, color=(0, 0, 255), thickness=5)
        cv2.imshow('image', img)

        # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]

        # cv2.putText(img, str(b) + ',' +
        #             str(g) + ',' + str(r),
        #             (x, y), font, 1,
        #             (255, 255, 0), 2)
        cv2.imshow('image', img)

    # driver function



def main():
    # reading the image
    global img
    img = cv2.imread(path, 1)
    img = cv2.resize(img, (370, 370))
    # displaying the image
    cv2.imshow('image', img)

    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()

    image = cv2.imread(path, 1)
    image = cv2.resize(image, (370, 370))

    for coordinate in coordinates:
        [x,y] = coordinate
        image = cv2.circle(image, (x,y), radius=1, color=(0, 0, 255), thickness=5)

    cv2.imshow('image', image)
    cv2.setMouseCallback('image', click_event)


    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    #n=1
    #n = int(input('Enter the number of Centers : '))
    Coordinates = pd.DataFrame(coordinates, columns=['x', 'y'])
    kmeans = KMeans(n_clusters=n).fit(Coordinates)
    centroids = kmeans.cluster_centers_
    print(centroids)

    for coordinate in coordinates:
        [x, y] = coordinate
        image = cv2.circle(image, (x, y), radius=1, color=(0, 0, 255), thickness=5)
    for centroid in centroids:
        [x, y] = centroid
        x = int(x)
        y = int(y)
        image = cv2.circle(image, (x, y), radius=1, color=(255, 0, 0), thickness=5)
    cv2.imwrite('image.jpg', image)
