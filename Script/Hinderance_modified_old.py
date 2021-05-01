import tensorflow as tf
import cv2
import numpy as np

path = ''
n = -1
hinderance = []
global img


def updateVar(fpath, fn, fhinderance):
    global path, n, hinderance
    path = fpath
    n = fn
    hinderance = fhinderance


coordinates = []


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    global img,n
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        # print(x, ' ', y)
        coordinates.append([x, y])

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.circle(img, (x, y), radius=1, color=(255, 0, 0), thickness=5)
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

        cv2.circle(img, (x, y), radius=1, color=(255, 0, 0), thickness=5)
        cv2.imshow('image', img)


# driver function
def main():
    global img
    model = tf.keras.models.load_model('TPU_Trained_model.h5')
    image = cv2.imread(path)

    print(image.shape)
    image = np.reshape(image, [1, 224, 224, 3])
    prediction = model.predict(image)
    [[x, y]] = prediction

    image = cv2.imread(path)
    cv2.circle(image, (int(x), int(y)), radius=1, color=(0, 255, 0), thickness=5)

    # image = cv2.imread(path, 1)
    # # prediction = [[111,100]]
    #
    # print(f'X : {x}  , Y : {y}')
    # img = cv2.imread(path, 1)
    # img = cv2.circle(img, (int(x), int(y)), radius=1, color=(0, 0, 255), thickness=5)
    # # displaying the image
    #
    cv2.imshow('image', image)
    cv2.waitKey(0)
    # # close the window
    cv2.destroyAllWindows()
    cv2.imwrite('image.png', image)

    # n = int(input('Enter the number of hinderances'))
    hinderances = []
    depletion = [0.5, 0.75, 0.25, 0.2, 0.1]
    for i,hinderance_type in enumerate(hinderance):

        # hinderance_type = int(input("Enter the type of hinderance 1)Metal Door 2)Concrete Wall 3)Brick Wall 4)Wood window 5)Glass window"))
        img = cv2.imread('image.png', 1)
        #img = np.reshape(img, [1, 224, 224, 3])
        # displaying the image
        cv2.imshow('image', img)

        # setting mouse hadler for the image
        # and calling the click_event() function
        cv2.setMouseCallback('image', click_event)

        # wait for a key to be pressed to exit
        cv2.waitKey(0)

        # close the window
        cv2.destroyAllWindows()
        cv2.imwrite('image.png', img)
        hinderances.append([coordinates[i], hinderance_type])


    for i in range(n):
        [x2, y2], hinderance_id = hinderances[i]
        dist = np.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
        x = x + depletion[hinderance_id] *dist
        y = y + depletion[hinderance_id] *dist
    # displaying the image

    img = cv2.imread('image.png', 1)

    img = cv2.circle(img, (int(x), int(y)), radius=1, color=(0, 0, 255), thickness=5)
    cv2.imwrite('image.jpg', img)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

