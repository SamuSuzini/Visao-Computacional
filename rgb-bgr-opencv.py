import cv2
import numpy as np

#Criando a imagem (512 pixel por 512, com 3 slot para as cores BGR)
img_np = np.zeros((512, 512, 3), np.uint8)
print(img_np)

# RGB -> red, green, blue
# BGR -> blue, green, red

img_np[:256] = 255, 0, 0
img_np[256:] = 0, 255, 0
img_np[:,:256] = 0, 0, 255


cv2.imshow("Imagem", img_np)
cv2.waitKey(0)