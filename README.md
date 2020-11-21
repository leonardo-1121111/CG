# Computação gráfica
Leonardo M Silva
1121111

# OpenCV
Fazer o download do [OpenCV](https://opencv.org/), após extrair em um diretório.

### opencv_annotation
Primeiramente deve se utilizar o opencv_annotation para fazer a marcação dos objetos nas imagens positivas.
É desenhado retangulos em todos os objetos contidos na imagem.
São utilizados os seguintes comando no opencv_annotation:
- 'C' confirma o retangulo
- 'D' para refazer o retangulo
- 'N' avança para a proxima imagem
- 'ESC' para sair

Sairá automaticamente quando finalizar todas as anotações das imagens.

### opencv_createsamples
O metodo opencv_createsamples cria um vetor passando a quantidade de exemplos, a largura e a altura como parâmetros.
Também é possivel utiliza-lo para criar dataset maiores usando as imagens positivas como base e passando os parametros:
-maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5
para distorcer as imagens.

### opencv_traincascade
O classificador em cascata é treinado com o comando opencv_traincascade
que recebe como parâmetros um diretório onde o classificador será salvo, o arquivo de vetor gerado anteriormente,
a lista de imagens negativas, a quantidade de imagens positivas e negativas,
o número e estágios da cascata e as dimensões das imagens no vetor.

O tempo de treinamento varia de acordo com a capacidade de processamento do computador.

### Exemplo da execução
| Método | Exemplo |
| ------ | ------ |
| opencv_annotation | C:\Users\leo_l\Desktop\CG\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=positivas/ |
| opencv_createsamples | C:\Users\leo_l\Desktop\CG\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec |
| opencv_traincascade | C:\Users\leo_l\Desktop\CG\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 24 -h 24 |

Utilizei, nesse projeto, 4 dataset, um com imagens negativas, um dataset com imagens positivas de mãos,
um dataset com imagens positivas de pessoas e um dataset positiva com mouses.

Obrigado