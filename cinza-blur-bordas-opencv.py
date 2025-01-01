import cv2
import numpy as np

lena = cv2.imread("arquivos/lena.png")
lena_cinza = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
lena_blur = cv2.GaussianBlur(lena, (15, 15), 0)
lena_bordas = cv2.Canny(lena, 100, 100)


cv2.imshow("Lena", lena)
cv2.imshow("Lena Cinza", lena_cinza)
cv2.imshow("Lena Blur", lena_blur)
cv2.imshow("Lena Bordas", lena_bordas)


cv2.waitKey(0)