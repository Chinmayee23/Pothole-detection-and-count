import numpy as np
import cv2 as cv
import scipy.misc, scipy.ndimage
#reading image
img = cv.imread('E:/pothole-detection-source-code-master/test6.png',0)
edge = cv.Canny(img,100,200)     

A=np.reshape(edge, (edge.size,-1))
np.savetxt("t6.csv", A, delimiter=",")
