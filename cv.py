#!/usr/local/bin/python3
from PIL import Image
import imutils
import cv2
import pytesseract


def main(name):
    # read file
    img = cv2.imread(name)
    img = imutils.resize(img, width=800)
    img = imutils.rotate(img, 0.1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", gray)
    cv2.waitKey (0)
    # two value format
    ret, thresh1 = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
    cv2.imshow("Image", thresh1)
    cv2.waitKey (0)
    cv2.imwrite("test.jpg", thresh1)

    text = pytesseract.image_to_string(Image.open('test.jpg'), "chi_sim")
    return text


if __name__ == '__main__':
    info = main("2.png")
    print(info)
