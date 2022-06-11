import cv2
filepath ="mir4s.png"
image = cv2.imread(filepath,1)
cv2.imshow("PHOTO",image)
cv2.waitKey(0)
cv2.destroyAllWindows()