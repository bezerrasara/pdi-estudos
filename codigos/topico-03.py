#Tópico 3 – Abrir uma imagem colorida em RGB, visualizar e salvar cada um dos canais separadamente. Obs: Busquem compreender o que significa cada um dos canais.



import cv2

imagem = cv2.imread("flor.jpg")
azul,verde,vermelho = cv2.split(imagem)
cv2.imshow("canal azul",azul)
cv2.imshow("canal verde",verde)
cv2.imshow("canal vermelho",vermelho)
#cv2.waitkey(0)
cv2.imwrite("canal_azul.jpg",azul)
cv2.imwrite("canal_verde.jpg",verde)
cv2.imwrite("canal_vermelho.jpg",vermelho)


