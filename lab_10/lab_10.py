import cv2
import matplotlib.pyplot as plt
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\psztefko\PycharmProjects\advanced-programming\lab_10\tesseract'
print(pytesseract.image_to_string(r'C:\Users\psztefko\PycharmProjects\advanced-programming\lab_10\pure.png'))