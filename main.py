import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from Perlin import Perlin


if __name__ == "__main__":

    seed=18
    perlinSize=512

    perlin=Perlin(perlinSize,seed)

    imageSize=256
    frequency=0.01
    amplitude=0.5

    # 1D Perlin Noise Plot 
    x = np.arange(0.0, 3.0, 0.01)
    y = np.zeros(len(x))

    for i in range(len(x)):
        y[i]=perlin.Noise1D(x[i])*amplitude

    plt.plot(x,y)
    plt.show()


    # 2D Perlin Noise Image
    data = np.zeros( (imageSize,imageSize,3), dtype=np.uint8)

    for x in range(imageSize):
        for y in range(imageSize):
            n=perlin.Noise2D(x*frequency, y*frequency)

            #Change value from range [-sqrt[d]/2,sqrt[d]/2] to value in range [0.0,1.0]
            n+=1
            n/=2

            #Change to RGB range
            c=round(255*n)
            data[x,y]=[c,c,c]


    img=Image.fromarray(data)
    img.show()