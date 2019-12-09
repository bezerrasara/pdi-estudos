"""Abrir uma imagem colorida, transformar em tom de cinza,
visualizar imagem de entrada.
Apliquem uma limiarização (thresholding),
visualizem os resultados e salvem.
Obs: busquem compreender os resultados da técnica."""

import cv2

imagem = cv2.imread('flor.jpg')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Applicando o threshold
ret, threshold_imagem = cv2.threshold(imagem_cinza, 70, 255, cv2.THRESH_BINARY)

# Show the input image
cv2.imshow('Input grayscale image', imagem_cinza)

# Show the result of the threshold
cv2.imshow('Canny filter result', threshold_imagem)

cv2.waitKey(0)

# Save the results
cv2.imwrite('canny_filter_result.jpg', threshold_imagem)
