import cv2
import numpy as np

# open or read the images
img1 = cv2.imread('IoT/IMG_blank.jpg')
img2 = cv2.imread('IoT/IMG_stop.jpg')

print(img1.shape)
print(img2.shape)

# resize the images to speed up processing
img1 = cv2.resize(img1,(640,480))
img2 = cv2.resize(img2,(640,480))

# display resized images
#cv2.imshow("blank", img1)
#cv2.imshow("stopSign", img2)

# convert imags to grayscale. This reduces matrices from 3 (R, G, B) to just 1
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# disply grayscale images
#cv2.imshow("GrayBlank", gray1)
#cv2.imshow("GrayStop", gray2)

# blue the images to get rid of sharp edjes/outlines. This will improve the processing
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

# display blurred images
#cv2.imshow("Blur 1", gray1)
#cv2.imshow("Blur 2", gray2)

# obtain the difference between the two images & display the result
imgDelta = cv2.absdiff(gray1, gray2)
cv2.imshow("Delta", imgDelta)

# convert the difference into binary & display the result
thresh = cv2.threshold(imgDelta, 25, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Binary_Thresh", thresh)

# dilate the thresholded image to fill in holes & display the result
thresh = cv2.dilate(thresh, None, iterations=2)
cv2.imshow("Dilate", thresh)

# find contours or continuous white blobs in the image
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# find the index of the largest contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

# draw a bounding box/rectangle around the largest contour
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)

# display the original image for reference
cv2.imshow("OriginalStop",img2)

#wait for key press and then terminate all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()