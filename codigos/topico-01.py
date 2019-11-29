#Tópico 1 – Abrir uma imagem colorida, visualizar e salvar.

import cv2
imagem = cv2.imread("flor.jpg")
cv2.imshow("imagemcarregada",imagem)
#cv2.waitkey(0)
cv2.imwrite("imagemsalva.jpg",imagem)
