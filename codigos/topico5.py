"""Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada.
Apliquem os filtros passa baixa mediana (cv_median) e media (cv_blur),
visualizem os resultados e salvem.Obs: busquem compreender os resultados de
cada filtro."""

import cv2

# lendo imagem rgb
imagem = cv2.imread('flor.jpg')

# Transformando em escala de cinza

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Applicando filtros  mediana e media

mediana = cv2.medianBlur(imagem_cinza, ksize=5)
media = cv2.blur(imagem_cinza, ksize=(5, 5))

# mostrando imagem HSV e os canais
cv2.imshow('filtro mediana', mediana)
cv2.imshow('filtro media(blur)', media)

cv2.waitKey(0)

# Salvando os resultados
cv2.imwrite('mediana_resultado.jpg', mediana)
cv2.imwrite('media_resultado.jpg', media)
