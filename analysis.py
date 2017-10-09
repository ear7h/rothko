import os
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

DIR_NAME = 'images'

img_list = os.listdir(DIR_NAME)

# clear the bad files
img_list = [name for name in img_list if all(x not in name for x in ['chapel', '.DS', '?'])]

def avg_brightness(filename):
	img = mpimg.imread(DIR_NAME + "/" + filename)
	return np.mean(img)/255

def avg_saturation(filename):
	img = mpimg.imread(DIR_NAME + "/" + filename)
	pixel_line = np.reshape(img, [-1, 3])
	s = 0
	for px in pixel_line:
		s += max(px)/255
	return s/len(pixel_line)

def year_from_name(filename):
	return int(filename.split('-')[0])


bringhtness = []
saturation = []
years = []


i = 0
for file in img_list:
	print(i)
	i += 1
	saturation.append(avg_saturation(file))
	bringhtness.append(avg_brightness(file))
	years.append(year_from_name(file))

plt.plot(years, bringhtness, "o", label='bright')
plt.plot(years, saturation, "o", label='sat')
plt.legend()
plt.show()