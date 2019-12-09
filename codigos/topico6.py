"""Tópico 6 – Abrir uma imagem colorida, transformar em tom de cinza,
visualizar imagem de entrada. Apliquem os filtros passa alta de canny (cv_canny),
visualizem os resultados e salvem. Obs:
busquem compreender os resultados do filtro."""

import cv2

# Apply Canny filter (change the inferior and superior limit and see the difference)
imagem = cv2.imread("flor.jpg")
grayscale_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(grayscale_image, 80, 180)



# Show the HSV image and its channels
# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)

# Show the result of the canny filter
cv2.imshow('Canny filter result', canny_image)

cv2.waitKey(0)
