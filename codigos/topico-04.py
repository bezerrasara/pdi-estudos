#Tópico 4 – Abrir uma imagem colorida, transformar em HSV, visualizar e salvar cada um dos canais separadamente. Obs: Busquem compreender o que significa cada um dos canais.


import cv2
image = cv2.imread("imgrgb.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow('HSV Image', hsv)
cv2.imshow('canal H',h)
cv2.imshow('canal S',s)
cv2.imshow('canal v',v)

cv2.waitKey(0)

cv2.imwrite('hsv_imagem.jpg', hsv)
cv2.imwrite('canal_h.jpg',h)
cv2.imwrite('canal_s.jpg',s)
cv2.imwrite('canal_v.jpg',v)

            

