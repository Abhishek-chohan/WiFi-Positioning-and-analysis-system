import pandas as pd
import numpy as np
import tqdm
import cv2

data = pd.read_csv('masterfile.csv')

img= data['0']

dir = 'Data/'
addresses  = [dir + addr for addr in img ]

img_arr = []
data = pd.read_csv('masterfile.csv')

img = data['0']

dir = 'Data/'
addresses = [dir + addr for addr in img]

img_arr = []

for n, address in enumerate(addresses):

    if n % 1000 == 0:
        print(f'{n + 1} / 14954')
    image = cv2.imread(address)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_CUBIC)
    img_arr.append(image)
#     image_path = address
#     image = tf.io.read_file(image_path)
#     image = tf.image.decode_png(image)
#     image = tf.image.convert_image_dtype(image,tf.float32)
#     image = tf.make_ndarray(image)
#     img_arr.append(image)


img_arr = np.array(img_arr)
#cv2.imshow('img',img_arr[1,:,:])