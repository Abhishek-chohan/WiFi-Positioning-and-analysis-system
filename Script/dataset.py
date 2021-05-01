import sys
import os
import cv2
import numpy as np
import tensorflow as tf
import pandas as pd

# def _parse_image_function(example_proto):
#     features = tf.io.parse_single_example(example_proto, image_feature_description)
#     image = tf.io.decode_raw(features['image'], tf.uint8)
#     image.set_shape([3 * 224 * 224])
#     image = tf.reshape(image, [224, 224, 3])
#
#     label = tf.cast(features['label'], tf.int32)
#     label = tf.one_hot(label, 10)
#
#     return image, label
#
#
# def read_dataset(epochs, batch_size, channel, channel_name):
#
#     filenames = [os.path.join(channel, channel_name + '.tfrecords')]
#     dataset = tf.data.TFRecordDataset(filenames)
#
#     image_feature_description = {
#         'image': tf.io.FixedLenFeature([], tf.string),
#         'x': tf.io.FixedLenFeature([], tf.int64),
#         'y': tf.io.FixedLenFeature([], tf.int64),
#     }
#
#     dataset = dataset.map(_parse_image_function, num_parallel_calls=10)
#     dataset = dataset.prefetch(10)
#     dataset = dataset.repeat(epochs)
#     dataset = dataset.shuffle(buffer_size=10 * batch_size)
#     dataset = dataset.batch(batch_size, drop_remainder=True)
#
#     return dataset
# dataset = tf.data.TFRecordDataset(["train.tfrecords"])
# def decode_record(record):
#     image = tf.io.decode_raw(
#         record['image'], out_type=tf.string, little_endian=True, fixed_length=None, name=None
#     )
#     x = record['x']
#     y = record['y']
#     image = tf.reshape(image, (224,224,1))
#     return (image, x,y)
#
# def parse_record(record):
#     name_to_features = {
#         'image': tf.io.FixedLenFeature([], tf.string),
#         'x': tf.io.FixedLenFeature([], tf.int64),
#         'y': tf.io.FixedLenFeature([], tf.int64),
#     }
#     return tf.io.parse_single_example(record, name_to_features)
#
# for record in dataset:
#     parsed_record = parse_record(record)
#     decoded_record = decode_record(parsed_record)
#     image, x,y= decoded_record
#     print(image.shape, x,y)
#     break


import os
import cv2
import pandas as pd
import numpy as np


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
images = []
image = cv2.imread('Data/0004dd3cb11e50530676f77b55262d38.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(224,224,1))
images.append(image)
#cv2.imshow('image',image)
cv2.setMouseCallback('image', click_event)
image = cv2.imread('Data/001ecf3e8d3c74a76a6e8bceb9e963c6.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(224,224,1))
images.append(image)
images = np.array(images)
cv2.imshow('image',images[1,:,:])
# wait for a key to be pressed to exit
cv2.waitKey(0)

# close the window
cv2.destroyAllWindows()