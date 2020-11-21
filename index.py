# Detecção dos objetos treinados na camera

import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Inicializa o WindowCapture
wincap = WindowCapture('Camera')

# Carrega o modelo treinado
cascade_limestone = cv.CascadeClassifier('result.xml')

# Carregue uma classe Vision
vision_limestone = Vision(None)

loop_time = time()
while(True):

    # get an updated image of the game
    imagem = wincap.get_screenshot()

    # Detecção de objetos
    rectangles = cascade_limestone.detectMultiScale(imagem)

    # Desenha os resultados da detecção na imagem original
    detection_image = vision_limestone.draw_rectangles(imagem, rectangles)

    # Exibe a imagem
    cv.imshow('Imagem', detection_image)

    loop_time = time()

    key = cv.waitKey(1)
    # presionar Q para fecahr
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    # F para salvar iamgem como positiva
    elif key == ord('f'):
        cv.imwrite('positiva/{}.jpg'.format(loop_time), imagem)
    # D para salvar iamgem como negativa
    elif key == ord('d'):
        cv.imwrite('negativa/{}.jpg'.format(loop_time), imagem)
        