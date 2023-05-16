import random
import math

class Perlin:
    def __init__(self,size,seed):
        self.permutation=list(range(size))
        self.size=size
        self.seed=seed
        self.ShufflePermutation()

    def ShufflePermutation(self):
        for i in range(self.size):
            random.seed(self.seed+i)
            idx=random.randint(0,self.size-1)
            self.permutation[i],self.permutation[idx]=self.permutation[idx],self.permutation[i]

    def Wrap(self,v):
        return v-math.floor(v/self.size)*self.size

    def ConstantVector(self,v):
        h=v%4
        if h==0:
            return 1,1
        elif h==1:
            return -1,1
        elif h==2:
            return -1,-1
        else:
            return 1,-1

    def Dot(self,v1,v2):
        return v1[0]*v2[0]+v1[1]*v2[1];

    def Fade(self,t):
        return ((6*t-15)*t+10)*t**3

    def Lerp(self,t,v1,v2):
        return v1+t*(v2-v1)

    def Noise2D(self,x,y):
        X=math.floor(x)%self.size
        Y=math.floor(y)%self.size

        #x and y must be from range [0,1] that why we multiply by frequency on input
        xf=x-math.floor(x)
        yf=y-math.floor(y)

        tR=xf-1,yf-1
        tL=xf,yf-1
        bR=xf-1,yf
        bL=xf,yf

        vTR=self.permutation[self.Wrap(self.permutation[self.Wrap(X+1)]+Y+1)]
        vTL=self.permutation[self.Wrap(self.permutation[self.Wrap(X)]+Y+1)]
        vBR=self.permutation[self.Wrap(self.permutation[self.Wrap(X+1)]+Y)]
        vBL=self.permutation[self.Wrap(self.permutation[self.Wrap(X)]+Y)]

        dotTR=self.Dot(tR,self.ConstantVector(vTR))
        dotTL=self.Dot(tL,self.ConstantVector(vTL))
        dotBR=self.Dot(bR,self.ConstantVector(vBR))
        dotBL=self.Dot(bL,self.ConstantVector(vBL))

        u=self.Fade(xf)
        v=self.Fade(yf)

        return self.Lerp(u, self.Lerp(v, dotBL, dotTL), self.Lerp(v, dotBR, dotTR))

    def Noise1D(self,x):
        X1=math.floor(x)%self.size
        X2=X1+1
        xf=x-math.floor(x)

        vX1=self.permutation[self.Wrap(X1)]
        vX2=self.permutation[self.Wrap(X2)]

        pX1=vX1*xf
        pX2=-vX2*(1-xf)

        u=self.Fade(xf)

        return self.Lerp(u, pX1, pX2)