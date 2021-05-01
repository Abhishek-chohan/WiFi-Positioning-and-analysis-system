import tensorflow as tf
import cv2
import numpy as np

path = ''
def updateVar(fpath):
    global path
    path = fpath


def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell

		print(x, ' ', y)

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


def main():
	model  = tf.keras.models.load_model('TPU_Trained_model.h5')


	# print(model.summary())

	image = cv2.imread(path)
	# img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
	# img = np.reshape(img,[1,224,224,1])
	# print(img.shape)
	# img = np.array(img)
	# img = tf.cast(img, dtype=tf.float32)
	# img = img/255.0
	# tup = model.predict(img)
	# [[x,y]] = tup
	# x = int(x)
	# y = int(y)
	image = cv2.imread(path)

	print(image.shape)
	image = np.reshape(image,[1,224,224,3])
	prediction = model.predict(image)
	[[x,y]] = prediction

	print(f'X : {x}  , Y : {y}')


	img = cv2.imread(path,1)
	img = cv2.resize(img,(224,224))
	img = cv2.circle(img , (int(x),int(y)), radius=1, color=(0, 0, 255), thickness=5)
		# displaying the image
	cv2.imwrite('image.jpg',img)
	# cv2.imshow('image', img)
	#
	#
	#
	#
# cv2.waitKey(0)
#
# 	# close the window
# cv2.destroyAllWindows()



