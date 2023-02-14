import cv2
import numpy as np

arr = cv2.imread('')
print(set( tuple(v) for m2d in arr for v in m2d))
arr = np.where(arr == [1,1,1], [255,255,255], arr)
arr = np.where(arr == [2,2,2], [255,0,0], arr)
print(set( tuple(v) for m2d in arr for v in m2d))
