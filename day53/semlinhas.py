import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
#rodando no google colab em https://colab.research.google.com/drive/1EkWy1CG0W7HDUchE1HL-Ef9l3W8I_keF?usp=sharing

imagem_upload = files.upload()

image = cv2.imread(list(imagem_upload.keys())[0])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.title('Imagem em tons de cinza')
plt.axis("off")
plt.show()

bordas = cv2.Canny(gray, 100, 200)
plt.imshow(bordas, cmap='gray')
plt.title("Removendo bordas")
plt.axis("off")
plt.show()

cv2.imwrite("sem_bordas.png", bordas)
files.download("sem_bordas.png")

from PIL import Image

altura, largura = bordas.shape
print(altura, largura)

# cria uma imagem com canal alpha, matriz de imagem RGBA
transparente = np.zeros((altura, largura, 4), dtype=np.uint8)

#para cara pixel há uma borda (ou o valor nao é 0), coloque a cor branca com o fundo opaco e deixe visivel na imagem
transparente[bordas != 0] = [255, 255, 255, 255]

cv2.imwrite("transparente.png", transparente)
