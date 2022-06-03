import cv2
from cv2 import waitKey,destroyAllWindows,imread,imshow
Img = imread("python.png")
imshow("TEST",Img)
waitKey(0)
destroyAllWindows()
height,width,channels = Img.shape[:3]

print(height)
print(width)
print(channels)

