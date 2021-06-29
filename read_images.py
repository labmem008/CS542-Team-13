import os
import cv2

def get_images(category, path):
	if (not os.path.exists(path)):
		print("path does not exist")
		return
	folder=os.path.join(path, category)
	images=[os.path.join(folder,file) for file in os.listdir(folder)]
	return images

def read_image(image_path):
	image = cv2.imread(image_path, cv2.IMREAD_COLOR)
	image = cv2.resize(image, (300,200), interpolation=cv2.INTER_CUBIC)
	return image

# Test get_images and read_images
# dolphin_folder = get_images('dolphin','./data')
# img=read_image(dolphin_folder[0])
# cv2.imshow('Testing...',img)
# cv2.waitKey(0)
