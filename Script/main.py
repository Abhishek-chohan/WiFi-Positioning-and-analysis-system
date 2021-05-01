# importing the module
import os
import cv2
import pandas as pd
import numpy as np
coordinates = []

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell

		print(x, ' ', y)
		coordinates.append([x, y])
		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)

	# checking for right mouse clicks
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)




# reading the image
images = list(os.listdir('Data'))
dataset = pd.DataFrame(np.zeros((len(images), 3)))
for i,image in enumerate(images):

	img = cv2.imread('Data/'+image, 1)
	img = cv2.resize(img,(224,224))
	# displaying the image
	cv2.imshow('image', img)

	# setting mouse hadler for the image
	# and calling the click_event() function
	cv2.setMouseCallback('image', click_event)

	# wait for a key to be pressed to exit
	cv2.waitKey(0)

	# close the window
	cv2.destroyAllWindows()
	print(f'{i+1}')

for i, image in enumerate(images):
	dataset[0][i] = image
	x,y = coordinates[i]
	dataset[1][i] = x
	dataset[2][i] = y

dataset.to_csv('out.csv',index = False)