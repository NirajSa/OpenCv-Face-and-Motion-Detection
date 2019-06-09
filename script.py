import cv2

img  = cv2.imread("abcd.jpg",0)

resized_image = cv2.resize(img,(100,50))
cv2.imshow("abcd",resized_image)
cv2.imwrite("abcd_r.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
