import numpy
import matplotlib
import pylab
from numba import autojit

@autojit
def iterMandel(x, y, iterMax):
    """
    Dadas las partes real e imaginaria de un numero complejo,
    determina la iteracion en la cual el candidato al conjunto
    de Mandelbrot se escapa.
    """
    c = complex(x, y)
    z = 0.0j
    for i in range(iterMax):
        z = z**2 + c
        if abs(z) >= 2:
            return i
    
    return iterMax

@autojit
def crearFractal(minX, maxX, minY, maxY, imagen, iteraciones):
    """
    Dada la region de la grafica que se quiere obtener, y el
    tamano de la imagen, determina el valor numerico de cada
    pixel en la grafica y determina si es parte o no del conjunto
    de Mandelbrot.
    """
    altura = imagen.shape[0]
    ancho  = imagen.shape[1]
    
    pixelX = (maxX - minX) / ancho
    pixelY = (maxY - minY) / altura
    
    for x in range(ancho):
        real = minX + x*pixelX
        for y in range(altura):
            imag = minY + y*pixelY
            color = iterMandel(real, imag, iteraciones)
            imagen[y, x] = color

anc = 16.0
alt = 9.0

inicio_x = -1.465
inicio_y = -0.15

escala = 0.004

fin_x = inicio_x + escala*anc
fin_y = inicio_y + escala*alt

imagen = numpy.zeros((alt*300, anc*300), dtype = numpy.uint8)
crearFractal(inicio_x, fin_x, inicio_y, fin_y, imagen, 100)

ax = pylab.imshow(imagen, cmap="Spectral")

ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

ax.axes.spines["right"].set_color("none")
ax.axes.spines["left"].set_color("none")
ax.axes.spines["top"].set_color("none")
ax.axes.spines["bottom"].set_color("none")

fig = pylab.gcf()
fig.savefig("mandel6.png", dpi=300, pad_inches=0.0, bbox_inches='tight', figsize=(16,9))
