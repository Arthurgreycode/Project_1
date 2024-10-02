import cv2
import cv2.data
image = cv2.imread("./image.jpg")


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.rectangle(image, (100, 100), (250, 250), (0,255,255), 2)




while True:
    cv2.imshow("Image_open", image)
    # cv2.imshow("GRAY IMAGE", gray_image)
    if cv2.waitKey(1) == ord("x"):
        break