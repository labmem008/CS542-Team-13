import os
import cv2
import operator
import pprint

def get_images(category, path):
	if (not os.path.exists(path)):
		print("path does not exist")
		return
	folder=os.path.join(path, category)
	images=[os.path.join(folder,file) for file in os.listdir(folder)]
	return images

def read_image(image_path):
	image=cv2.imread(image_path, cv2.IMREAD_COLOR)
	image=cv2.resize(image, (300,200), interpolation=cv2.INTER_CUBIC)
	return image

# Testing......
# dolphin_folder = get_images('dolphin','./data')
# img=read_image(dolphin_folder[0])
# cv2.imshow('Testing...',img)
# cv2.waitKey(0)

def images_per_class(path):
	categories=os.listdir(path)
	dict={}
	for category in categories:
		dict[category]=len(os.listdir(path+'/'+category))
	dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
	return dict

# Testing......
# pprint.pprint(images_per_class('./data'))
# print(len(images_per_class('./data')))

