import cv2
import numpy as np

lambo = cv2.imread("./arquivos/lambo.png")
lambo_redimensionada = cv2.resize(lambo, (300, 300))
lambo_recorte = lambo[:256, :256]


cv2.imshow("Lambo", lambo)
cv2.imshow("Lambo Redimensionada", lambo_redimensionada)
cv2.imshow("Lambo Redimensionada", lambo_recorte)

cv2.waitKey(0)