import cv2
import sys

print len(sys.argv)

for x in range(0, len(sys.argv)):
    print str(sys.argv[x])
im_gray = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite(sys.argv[2], im_bw)
