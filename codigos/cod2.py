import cv2
imagem = cv2.imread("flor.jpg",0)
cv2.imshow("imagemcarregada",imagem)
cv2.imwrite("imagemsalva.jpg",imagem)
