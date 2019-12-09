#Tópico 2 – Abrir uma imagem colorida, transformar em níveis de cinza, visualizar e salvar imagem gerada.


import cv2
imagem = cv2.imread("flor.jpg",0)
cv2.imshow("imagem carregada",imagem)
cv2.imwrite("imagemsalva.jpg",imagem)
